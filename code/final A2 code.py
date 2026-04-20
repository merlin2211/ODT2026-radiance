import network
import socket
import json
import time
from machine import Pin
from neopixel import NeoPixel

#setting up the leds
NUM_LEDS = 24
np = NeoPixel(Pin(12), NUM_LEDS)  #assigning pins for the led

COLUMN_DELAY_MS = 800  #the duration of time 1 led column is being flashed on
led_last_time = 0
current_column = 0
columns = []
led_running = False
brightness = 0.1  #the brightness factor that will be multiplied in the r g b bracket

def start_led_sequence(new_columns):  #the code for resetting and starting the led flashing
    global columns, current_column, led_running, led_last_time
    columns = new_columns
    current_column = 0
    led_running = True
    led_last_time = time.ticks_ms()

def update_led():  #the led flashes different columns of the pixel art after a certain amout of time
    global current_column, led_last_time, led_running

    if not led_running:
        return

    if time.ticks_diff(time.ticks_ms(), led_last_time) >= COLUMN_DELAY_MS:  #setting up the duration of the led flashes

        if current_column >= len(columns):
            led_running = False
            clear_led()
            return

        col = columns[current_column]

        for i in range(NUM_LEDS):  #flash the led unless the colour sent is black
            try:
                r,g,b = col[i]
                np[i] = (int(r * brightness), int(g * brightness), int(b * brightness))
            except:
                np[i] = (0,0,0)

        np.write()
        current_column += 1
        led_last_time = time.ticks_ms()

def clear_led(): 
    for i in range(NUM_LEDS):
        np[i] = (0,0,0)
    np.write()

#sassigning pins to the switches
stop_switch    = Pin(21, Pin.IN, Pin.PULL_UP)
reverse_switch = Pin(4, Pin.IN, Pin.PULL_UP)

#assigning pins to the motor
in1 = Pin(25, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(27, Pin.OUT)

STEP_DELAY_US = 800  #the time it takes for NEMA to complete 1 cycle

stepSequenceCW = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

stepSequenceACW = [
    [1,0,0,1],
    [0,0,1,1],
    [0,1,1,0],
    [1,1,0,0],
]

motor_step_index = 0
motor_last_time  = 0

def stop_motor(): 
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

def step_motor(seq):
    global motor_step_index, motor_last_time

    if time.ticks_diff(time.ticks_us(), motor_last_time) >= STEP_DELAY_US:
        s = seq[motor_step_index % 4]
        in1.value(s[0])
        in2.value(s[1])
        in3.value(s[2])
        in4.value(s[3])
        motor_step_index += 1
        motor_last_time = time.ticks_us()

#setting up the wifi
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="LED_Controller", password="12345678")

while not ap.active():
    pass

print("WiFi Ready:", ap.ifconfig()[0])

#creating a local server using the wifi
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 80))
s.listen(1)

print("Server Ready")

#whenever the esp32 receives data through wifi, the motor needs to start moving and the leds need to start flashing the received data independently. Once the plate hits the reverse switch, it will stop and start travelling back. 
while True:
    print("\nWaiting for drawing data...")
    conn, addr = s.accept()
    print("Connected from", addr)

    try:
        req = b""

        #read the headers of the data
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            req += chunk
            if b"\r\n\r\n" in req:
                break

        parts = req.split(b"\r\n\r\n", 1)
        headers = parts[0]
        body = parts[1] if len(parts) > 1 else b""

        #content length of the pixel art data
        content_length = 0
        for line in headers.split(b"\r\n"):
            if b"Content-Length" in line:
                content_length = int(line.split(b":")[1].strip())

        while len(body) < content_length:
            body += conn.recv(1024)

        print("Body:", len(body), "/", content_length)

        if b"POST /upload" in headers:
            print("POST RECEIVED")

            try:
                data = json.loads(body)
                received_columns = data.get("columns", [])
                print("Columns:", len(received_columns))

                #the reponse before connectiung
                conn.send(
                    "HTTP/1.1 200 OK\r\n"
                    "Access-Control-Allow-Origin: *\r\n"
                    "Content-Type: text/plain\r\n\r\nOK"
                )
                conn.close()

                #the motion starts along with the leds flashes, but the 2 happen independently
                started = False

                while True:
                    step_motor(stepSequenceACW)

                    if not started:
                        start_led_sequence(received_columns)
                        started = True

                    update_led()

                    if reverse_switch.value() == 0:
                        stop_motor()
                        break

                time.sleep(2)

                #the motor changes direction of roation and the baseplate and neopixel move backwards
                while True:
                    if stop_switch.value() == 0:
                        stop_motor()
                        break

                    step_motor(stepSequenceCW)

                print("Cycle complete")

            except Exception as e:
                print("JSON ERROR:", e)

    except Exception as e:
        print("ERROR:", e)

    finally:
        try:
            conn.close()
        except:
            pass