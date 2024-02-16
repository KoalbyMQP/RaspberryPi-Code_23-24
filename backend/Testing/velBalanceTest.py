import sys, time, math 
sys.path.append("./")
from backend.KoalbyHumanoid.Robot import Robot
from backend.KoalbyHumanoid import trajPlannerTime

is_real = False

robot = Robot(is_real)

print("Setup Complete")

motionTime = 2.5
setPointsTimes = [[0],[motionTime], [motionTime*2]]
setPointsAngles = [[0], [math.radians(90)], [0]]
setPointsVels = [[0], [0], [0]]
setPointsAccels = [[0], [0], [0]]
tjTime = trajPlannerTime.TrajPlannerTime(setPointsTimes, setPointsAngles, setPointsVels, setPointsAccels)

robot.motors[1].target = (math.radians(80), 'P')
robot.motors[6].target = (math.radians(-80), 'P')

simStartTime = time.time()
while time.time() - simStartTime < 1:
    robot.updateAllMotorAngles()
    robot.updateBalancePoint()
    robot.updateRobotCoM()
    robot.moveAllToTarget()
    robot.VelBalance(robot.balancePoint)
while True:
    startTime = time.time()
    while time.time() - startTime < motionTime*2:
        loopTime = time.time()
        robot.updateAllMotorAngles()
        robot.updateBalancePoint()
        robot.updateRobotCoM()
        point = tjTime.getQuinticPositions(time.time() - startTime)
        robot.motors[0].target = (point[0], 'P')
        robot.motors[5].target = (-point[0], 'P')
        robot.moveAllToTarget()
        robot.VelBalance(robot.balancePoint)
        print(time.time() - loopTime)

