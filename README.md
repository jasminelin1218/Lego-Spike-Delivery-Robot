# LEGO SPIKE Autonomous Delivery Robot

This project implements a simple autonomous delivery robot using the LEGO SPIKE Prime kit.  
The robot simulates a restaurant food delivery scenario, where it detects the color of a food order and navigates through a corridor to deliver it to the correct location based on matching floor color.  
It uses multiple sensors for object detection and basic environment awareness, and is programmed using Python in a procedural style.


## Hardware Components
- LEGO SPIKE Prime
- 3x Motors (left wheel, right wheel, lifting arm)
- 2x Color Sensors  
  - **Top-facing**: reads color of the carried item  
  - **Bottom-facing**: reads color of the floor at each destination
- 1x Distance Sensor: detects nearby customers and halts movement


## Project Features
- **Autonomous navigation** using coordinated dual-motor control for forward movement and turning.
- **Color-based delivery logic**: identifies the color of the carried item (top sensor) and compares it with the destination color (bottom sensor).
- **Obstacle-aware execution**: halts robot movement when a nearby customer is detected, and resumes when the path is clear.
- **Conditional path logic**: delivers the item only when the destination color matches the item; otherwise, continues a predefined search pattern alternating left and right.


## Behavior Flow
1. Pick up an item and detect its color.
2. Move down the corridor, stopping at checkpoints to check the destination floor color.
3. If the color matches, deliver the item by releasing the arm and return to base.
4. If not matched, turn and continue searching until a match is found.
5. During all actions, the robot will pause if a customer is detected.

## Limitations
- The robot completes only one delivery per execution

## Demo
https://youtube.com/shorts/WxnP9flsiNM?feature=share

## Future work
- Refactor logic into a class-based modular design