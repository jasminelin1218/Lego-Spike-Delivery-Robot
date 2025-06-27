import time, math
from hub import port, light_matrix
import color_sensor
import distance_sensor
import motor
import color

COLOR_SENSOR_TOP = port.F
COLOR_SENSOR_DOWN = port.C
ROTATE_MOTOR_L = port.B
ROTATE_MOTOR_R = port.A
DISTANCE_SENSOR = port.D
LIFT_MOTOR = port.E

GOODS_COLOR = color.AZURE
Count = 0
position = 0

def wait_until_clear():
    while distance_sensor.distance(DISTANCE_SENSOR) < 200 and distance_sensor.distance(DISTANCE_SENSOR) != -1:
        print("⚠️ Passenger ahead! Hault...")
        time.sleep(0.2)

def item_check(a, b,position):
    global Count
    print("Count",Count)
    if a == b:
        wait_until_clear()
        motor.run_for_degrees(LIFT_MOTOR, 300, 150)# release item
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #backward
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        if position == 0:
            wait_until_clear()
            motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #left turn
            motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
            time.sleep(3)
        elif position == 1:
            wait_until_clear()
            motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #right turn
            motor.run_for_degrees(ROTATE_MOTOR_R, -270, 0)
            time.sleep(3)

        wait_until_clear()
        print("Countt",Count)
        motor.run_for_degrees(ROTATE_MOTOR_L, -500* Count, 150) #return to aisle entry
        print("Counttt",Count)
        motor.run_for_degrees(ROTATE_MOTOR_R, 500* Count, 150)
        time.sleep(3*Count)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #left turn (face ID check)
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
        time.sleep(3)
        return True
    return False

def get_ball():
    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -100, 250) #aisle entry to ID check
    motor.run_for_degrees(ROTATE_MOTOR_R, 100, 250)
    time.sleep(3)

    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, 100, 250) #return to aisle entry
    motor.run_for_degrees(ROTATE_MOTOR_R, -100, 250)
    time.sleep(3)

    global GOODS_COLOR
    GOODS_COLOR = color_sensor.color(COLOR_SENSOR_TOP)
    time.sleep(3)

    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #face aisle
    motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450) 
    time.sleep(3)

def Do():

    global Count, position
    get_ball()
        
    for i in range(3): 
        Count = i + 1 
        print(Count)
        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 250) #forward 1 unit
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 250) 
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #left turn
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450) 
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 150) #forward
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 150)
        time.sleep(3)

        DETECT = color_sensor.color(COLOR_SENSOR_DOWN) #compare color
        time.sleep(3)

        position = 0
        if item_check(GOODS_COLOR, DETECT,0): return 

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #backward (color mismatch)
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #right turn
        motor.run_for_degrees(ROTATE_MOTOR_R, 470, 0)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #right turn
        motor.run_for_degrees(ROTATE_MOTOR_R, 470, 0)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 150) #forward
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 150)
        time.sleep(3)

        DETECT = color_sensor.color(COLOR_SENSOR_DOWN) #compare color
        time.sleep(3)

        position = 1
        if item_check(GOODS_COLOR, DETECT,1): return 

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #backward (color mismatch)
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #left turn
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
        time.sleep(3)


def main():
    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -100, 150) #forward
    motor.run_for_degrees(ROTATE_MOTOR_R, 100, 150)
    time.sleep(3)
    Do()
main()

