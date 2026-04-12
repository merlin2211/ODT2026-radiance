# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Radiance`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Anish Baxi` | `Coding, Photography` | `App` | `Strong understanding of code logic, syntax and debugging, photography skills` |
| `Tejas Kulkarni` | `Electronics, Assembly` | `Fabrication, Documentation` | `Strong skills in CAD software and laser cutting, 3D printing. Comprehensive documentation and organization skills` |

## 1.3 Project Title
`Light Printer`

## 1.4 One-Line Pitch
`A moving neopixel strip displaying an image pattern, captured through exposure photography`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`A user draws a simple colour image on the MITapp. The line data for each column is converted into a grid for a neopixel strip. The strip is mounted on a mechanism which uses the SC8UU ball bearings, metal and threaded rods and a stepper motor to provide linear motion. The camera captures the image of the neopixel in real time through exposure photography. It provides the experience of a user seeing an image come to life in a medium they have never seen before. It hinges on anticipation and confusion of the seemingly random pattern the NeoPixel displays one after another to invest the user, and deliver a satisying payoff when they see the complete image.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`The project not only invites interaction, but allows active participation of the user through drawing by engaging imagination. The central experience is the visualization of the users drawing in a unique medium. The anticipation creates buildup and excitement as the data is converted. As the NP starts moving the user is confused by the flashing pattern of the NeoPixel. Once they see the final image formed on the camera, confusion turns into satisfaction. Now that they know ho the printer works, they will be excited to try out new drawings. `

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making an interactive experience for a mixed audience`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Object` | `Living Mirror - https://www.youtube.com/watch?v=aJeB7yPpRAY` | `The unique method of using light as a medium through electronics.` |
| `Website` | `Eric Staller - https://lightpaintingphotography.com/eric-staller/` | `The scope of exposure lighting and light painting` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`The idea of light painting has always been reserved for the people with a expert knowledge of photography and creative visualization. Through this project, we want to democratise light painting by aligning it with the basic ability to draw with your fingers, making it accessible to everyone.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`imagine → draw → anticipate → neopixel moves → bewilderment → camera captures movement → reacts → repeat`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `mixed audiences` |
| Age range | `12-70` |
| Solo or multiplayer | `solo` |
| Expected duration of one round | `45-50 seconds` |
| What should the player feel? | `imagination, anticipation, confusion, amazement ` |
| Is explanation required before use? | `Yes. Basic instructions regarding what sort of drawing might be best suited and how exposure photography works` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The player steps into a dark/dimly lit room`
2. **Start:** `The player is intrigued by the setup of the LEDs, camera and drawing screen.`
3. **First Action:** `The player begins by looking at an empty canvas and imagining what can be drawn.`
4. **Main Interaction:** `Player draws simple pixel art using different colours`
5. **System Response:** `The systems task is to convert the drawing taken into accurae neopixel data, and execute neopixel and motor precisely, to form an accurate and recognizable drawing.`
6. **Win / Lose / End Condition:** `When the camera captures the exposure photo, and it is seen by the user.`
7. **Reset:** `Motor moves to reset NP to original position, camera resets to photography mode. A new or same userbegins another drawing on the screen. `

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `NA (It is a drawing canvas)`
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `The camera captures a clear image through exposure photography.`
- [ ] `The NP pattern displayed is a comprehensible representation of what the user expects to see.`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`The user selects from a collection of pre made patterns, which is then displayed by the NeoPixel. The core experience of anticipation, confusion and satisfaction still stays. Only the form of input from the user's side is altered.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Custom casing to keep phone in`
- `RGB colour data instead of single colour`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [ ] Sensor-based
- [x] App-connected
- [x] Motorized
- [ ] Sound-based
- [x] Light-based
- [x] Screen/UI-based
- [x] Fabricated structure
- [ ] Game logic based
- [ ] Installation / tabletop experience
- [x] Other: `Photography based`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`The user draws an image on MIT App inventor where the screen is made up of a grid of buttons in the same proportion as the NP strip. Various control buttons allow them to erase, change colour, etc. the RGB value for each button is sent to the ESP 32 as an array. The ESP32 drives the NeoPixel strip, lighting each LED according to the column data, while simultaneously controlling a stepper motor that moves the strip laterally along a linear rail using metal rods, linear ball bearings and holders. A camera set to long-exposure mode captures the full sweep of the moving NeoPixel strip in a single frame, reconstructing the original drawing as a light painting. As the strip reaches the end, a limit switch is activated, which is programed to move the stepper in the opposite direction, resetting the NeoPixel plate to it's original position. `

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `App` | Input | `Allows user to draw pixel art, sends to ESP32` |
| `ESP32` | Processing | `Takes RGB array and turns into NeoPixel instructions, controls motor` |
| `Stepper Motor` | Output | `Drives rotational motion` |
| `NeoPixel strip` | Output | `Shows drawing pattern for each column` |
| `Limit Switch` | Input | `Controls when the stepper is to be stopped and reset` |
| `Linear Shaft Rail` | Physical Action | `Allows smooth, precise lateral motion` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
<img src="light-printer-build-sketch-exploded-view.jpeg" alt="Build sketch" width="400">

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [x] Shafts
- [ ] Springs
- [x] Bearings
- [ ] Wheels
- [x] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`The main mechanism is a linear rail shaft used to smoothly move a neopixel plate in 1 axis. It is made up of 2 metal rods of lengh 400 mm mounted on 2 SK8 linear rail shaft supports each. 2 SC8UU linear ball bearings are mounted on each shaft, which allow for frictionless movement. A MDF plate sits on top of the SC8UUs on which the NeoPixel strip is placed. The plate is attached to a threaded rod using a bolt. The threaded is connected to a NEMA stepper motor on one side, and a rotational ball bearing on the other. The ball bearing and the motor are held upright using laser cut brackets.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`Movement is driven by a NEMA 17 stepper attached to thethreaded rod. The bolt attached to the plate converts rotational motion into translational displacement. As the bolt moves, the NP plate moves as well, guided by the linear shaft rail. It moves laterally till it reaches the end of the shaft. Travel speed is calculated to match the camera's shutter speed, too fast produces motion blur within each column, too slow makes the exposure too long and risks ambient light contamination. `

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `Blender` | `` | `The exact placement of mechanical components. How exactly rotational motion of the stepper is converted into translational.` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`We realized we had no concrete plan on how to mount the threaded rod. After research, we found out we will need a bracket to attach the stepper to the base plate along with a radial ball bearing to freely rotate the threaded rod while keeping it stable.`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `ESP32` | `1` | `Main controller` |
| `Neo-Pixel strip (8 bit RGB)` | `3` | `Creating a column of 24 LEDs which will display image pattern` |
| `Nema17 Stepper Motor` | `1` | `Driving the main motion at a high RPM` |
| `LM2596` | `1` | `Step down buck converter to adjust voltage given to the stepper motor.` |
| `L298Ndual H-bridge` | `1` | `To drive stepper motor` |
| `Limit Switch` | `2` | `To stop the motor as soon as the NP plate reaches the end of the rod and reset it back to original position.` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Write here]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[Write here]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`The app is the main input took for the user. It is a canvas which allows the user to draw pixel art using their finger.`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `ESP32` | `1` | `Yes` | `No` | `0` | `NA` | `Microcontroller taught in class` |
| `NeoPixel Strip` | `3` | `No` | `No` | `NA` | `8 bit RGB` | `LED's are moe closely packed together` |
| `Metal rod` | `2` | `No` | `Yes` | `364` | `8mm diamter, 400mm length` | `Form axis along which NP plate will move` |
| `Linear Ball Bearing Slide` | `2` | `No` | `Yes` | `428` | `SC8UU` | `Allows for smooth linear motion along metal rod` |
| `Linear Ball Bearing support` | `4` | `No` | `Yes` | `452` | `SK8` | `To hold the rods stably` |
| `Nema17 Stepper Motor` | `1` | `No` | `Yes` | `711` | `JK42HS40-1204AF-02 NEMA17 4.2 kg-cm` | `It provides a higher RPM required to rapidly rotate threaded rod` |
| `Threaded rod` | `1` | `No` | `Yes` | `150-250` | `200mm length, 1mm pitch` | `Attached to stepper motor to attach brass nut on` |
| `Radial ball bearing` | `1` | `No` | `No` | `NA` | `625ZZ` | `To allow free rotation of threaded rod driven by sepper motor` |
| `Brass nut` | `1` | `No` | `Yes` | `20-70` | `Threaded brass nut` | `Component attached to NP plate to turn rotational motion into translational` |
| `Limit switch` | `2` | `Yes` | `No` | `NA` | `NA` | `When activated, acts as input to control stepper` |
| `MDF base plate` | `2` | `No` | `No` | `NA` | `laser cut` | `2 base plates, bigger one as base for entire build, smaller one mounted on SC8UUs which NeoPixel is kept on` |
| `Phone stand` | `1` | `No` | `No` | `NA` | `laser cut` | `To keep the phone upright as the user draws on it.` |
| `Stepper motor bracket` | `1` | `No` | `No` | `NA` | `laser cut` | `To hold the stepper in place at perpendicular angle.` |
| `Ball bearing holder` | `1` | `No` | `No` | `NA` | `laser cut` | `To stably hold radial ball bearing at perpendicular angle` |


## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`1. Usng laser cut MDF as base plate, allows us to engrave precise placements of all components to eliminate human error.
 2. SC8UU + SK8 + 8mm rod over plain holes: Ball bearings eliminate friction and slop, ensuring smooth, consistent carriage travel.
 3. NEMA 17 stepper over DC/servo: 1024 steps allow precise control and smoothness. Provides higher RPM than stepper in kit
 4. Threaded rod + brass nut over belt drive: 1mm pitch leadscrew provides fine, slip-free linear resolution directly tied to step count.
 6. 8-bit RGB over NeoPixel strip: LEDs are more closely packed together, so they offer higher resolution`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`Tasks are divided by core strength: Anish does coding and photography (laptop script, image processing, camera setup), and Tejas does electronics and fabrication (wiring, motor assembly, CAD). Both contribute equally to testing and playtesting. Decisions are made jointly during class time. If a disagreement arises, we try out both approaches quickly and choose based on result. Progress is reviewed at the start of each class session with the weekly milestone checklist, and there are regular meetups assigned for planning and strategizing. If a task is delayed, the other member provides support and the milestone log is updated honestly. Documentation is maintained continuously by both the members. Tejas handles fabrication photos and CAD files, Anish handles code notes and testing logs.`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `Finalize concept and system architecture` | `Both` | `2` | `Week 2` | `None` | `Done` |
| T2 | `Complete BOM and place component orders` | `Tejas` | `1` | `Week 3` | `T1` | `Done` |
| T3 | `Test NeoPixel strip with ESP32 (basic colour control)` | `Anish` | `2` | `Week 3` | `None` | `Done` |
| T4 | `Test stepper motor + driver (basic movement)` | `Both` | `4` | `Week 3` | `T1` | `To Do` |
| T5 | `MicroPython image capture + column extraction script` | `Anish` | `4` | `Week 3` | `T1, T3` | `To Do` |
| T6 | `CAD design + base plate` | `Tejas` | `3` | `Week 4` | `T2` | `To Do` |
| T7 | `Assemble linear shaft` | `Both` | `5` | `Week 4` | `T6` | `To Do` |
| T8 | `Camera long-exposure setup and testing` | `Both` | `2` | `Week 4` | `T1-6` | `To Do` |
| T9 | `[Final documentation, photos]` | `Tejas` | `5` | `Week 4` | `T1-7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `Both` | `N/A` |
| Electronics | `Tejas` | `Anish` |
| Coding | `Anish` | `Tejas` |
| App | `N/A` | `N/A` |
| Mechanical build | `Tejas` | `Anish` |
| Photography | `Anish` | `Tejas` |
| Testing | `Both` | `N/A` |
| Documentation | `Tejas` | `Anish` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [ ] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [x] CAD / structure planning completed
- [x] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Finalize concept` | `Finalize concept` | `Changes in the mechanism of the motor assembly, talks with faculty to optimise different pieces` | `complete BOM` |
| Week 2 | `test basic NeoPixel, setting up of camera and tweaking settings` | `Neopixel worked, but led to newer insights, camera worked` | `An idea to pivot from the original idea of drawing to a photo booth stylized selfie` | `write image processing script` |
| Week 3 | `Build linear rail assembly, camera exposure sync` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `Playtesting, refinements, full documentation, final build` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `Camera shutter speed and motor speed are not synchronized ` | `Technical` | `High` | `High` | `Calibrate motor steps-per-column against shutter speed` | `Anish` |
| `Ambient light contamination ruins long-exposure capture` | `Environment` | `Medium` | `High` | `Use a dark booth or fabric enclosure around the user and printer during the exposure.` | `Both` |
| `Laser cut MDF parts do not fit together correctly` | `Mechanical` | `Low` | `Medium` | `Build a test cut of one joint panel before committing to the full sheet` | `Tejas` |
| `Components delayed in shipping` | `Time` | `Low` | `High` | `identify local suppliers as backup for critical items ` | `Tejas` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`The precise synchronization between motor travel speed and camera shutter speed is the biggest unknown. The quality of the final light-print image depends entirely on each NeoPixel column being displayed for exactly the right duration as the carriage traverses one column-width of distance. If the timing is even slightly off, columns will overlap or leave gaps, making the output image unrecognizable.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
