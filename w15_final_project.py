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

##by GPT DETECT = color.YELLOW
GOODS_COLOR = color.AZURE
Count = 0
position = 0

def wait_until_clear():
    while distance_sensor.distance(DISTANCE_SENSOR) < 200 and distance_sensor.distance(DISTANCE_SENSOR) != -1:
        print("⚠️ 行人靠近，暫停中...")
        time.sleep(0.2)

def item_check(a, b,position):
    global Count
    print("Count",Count)
    if a == b:
        wait_until_clear()
        motor.run_for_degrees(LIFT_MOTOR, 300, 150)# 放開
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #後退
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        if position == 0:
            wait_until_clear()
            motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #左轉
            motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
            time.sleep(3)
        elif position == 1:
            wait_until_clear()
            motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #右轉
            motor.run_for_degrees(ROTATE_MOTOR_R, -270, 0)
            time.sleep(3)

        wait_until_clear()
        print("Countt",Count)
        motor.run_for_degrees(ROTATE_MOTOR_L, -500* Count, 150) #前進到入口
        print("Counttt",Count)
        motor.run_for_degrees(ROTATE_MOTOR_R, 500* Count, 150)
        time.sleep(3*Count)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #(擺向面球方)左轉
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
        time.sleep(3)
        #Do() ##無限遞迴風險?
        return True ##by GPT
    return False #by GPT

def get_ball():
    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -100, 250) #1前進到item
    motor.run_for_degrees(ROTATE_MOTOR_R, 100, 250)
    time.sleep(3)

    #拿球
    #motor.run_for_degrees(LIFT_MOTOR, 150, 150)# 夾起
    #time.sleep(3)

    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, 100, 250) #item退回1
    motor.run_for_degrees(ROTATE_MOTOR_R, -100, 250)
    time.sleep(3)

    global GOODS_COLOR
    GOODS_COLOR = color_sensor.color(COLOR_SENSOR_TOP)
    time.sleep(3)

    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #面向道路
    motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450) ##方向?
    time.sleep(3)

def Do():

    global Count, position
    get_ball()
    #Count = 1 ##好像沒有必要?
    #while distance_sensor.distance(DISTANCE_SENSOR) > 45 or distance_sensor.distance(DISTANCE_SENSOR) == -1:
        
    for i in range(3): ##這樣Count是從零開始數? 如果第一次就符合的話最後的move for degree(-150*Count)就不會動了吧?
        Count = i + 1 #修改成從1開始
        print(Count)
        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 250) #前進
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 250) ##一次只前進一格吧?這樣的話這行如果i變大->會前進太多格
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #左轉
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450) 
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 150) #前進
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 150)
        time.sleep(3)

        DETECT = color_sensor.color(COLOR_SENSOR_DOWN) #比對顏色
        time.sleep(3)

        position = 0
        if item_check(GOODS_COLOR, DETECT,0): return #修改處

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #後退(顏色不一)
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #右轉
        motor.run_for_degrees(ROTATE_MOTOR_R, 470, 0)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -500, 450) #右轉
        motor.run_for_degrees(ROTATE_MOTOR_R, 470, 0)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -150, 150) #前進
        motor.run_for_degrees(ROTATE_MOTOR_R, 150, 150)
        time.sleep(3)

        DETECT = color_sensor.color(COLOR_SENSOR_DOWN) #比對顏色
        time.sleep(3)

        position = 1
        if item_check(GOODS_COLOR, DETECT,1): return #修改處

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150, 150) #後退(顏色不一)
        motor.run_for_degrees(ROTATE_MOTOR_R, -150, 150)
        time.sleep(3)

        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, -270, 0) #左轉
        motor.run_for_degrees(ROTATE_MOTOR_R, 500, 450)
        time.sleep(3)
        '''
        wait_until_clear()
        motor.run_for_degrees(ROTATE_MOTOR_L, 150 * Count, 150) #後退到1
        motor.run_for_degrees(ROTATE_MOTOR_R, -150 * Count, 150) ##這邊好像是多餘的了(變成說每次的do()都會走到#1)
        time.sleep(3)
        '''

def main():
    wait_until_clear()
    motor.run_for_degrees(ROTATE_MOTOR_L, -100, 150) #前進
    motor.run_for_degrees(ROTATE_MOTOR_R, 100, 150)
    time.sleep(3)
    Do()
main()

