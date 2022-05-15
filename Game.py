import numpy as np
import pygame
import pyglet

from Drawer import Drawer
from Globals import displayHeight, displayWidth
from PygameAdditionalMethods import *
from ShapeObjects import *

drawer = Drawer()
vec2 = pygame.math.Vector2


class Game:
    no_of_actions = 9
    state_size = 15

    def __init__(self):
        trackImg = pyglet.image.load('images/track.png')
        self.trackSprite = pyglet.sprite.Sprite(trackImg, x=0, y=0)
        self.trackSprite.update(scale=0.6)
        # initiate car

        # initiate walls
        self.walls = []
        self.gates = []

        self.set_walls()
        self.set_gates()
        self.firstClick = True

        self.car = Car(self.walls, self.gates)

    def set_walls(self):
        self.walls.append(Wall(164, 538, 123, 355))
        self.walls.append(Wall(119, 346, 132, 238))
        self.walls.append(Wall(131, 236, 183, 152))
        self.walls.append(Wall(183, 152, 331, 103))
        self.walls.append(Wall(331, 103, 708, 132))
        self.walls.append(Wall(711, 134, 713, 237))
        self.walls.append(Wall(713, 237, 463, 357))
        self.walls.append(Wall(463, 357, 661, 338))
        self.walls.append(Wall(665, 340, 823, 255))
        self.walls.append(Wall(1031, 450, 1004, 344))
        self.walls.append(Wall(1033, 450, 899, 577))
        self.walls.append(Wall(907, 576, 207, 570))
        self.walls.append(Wall(199, 569, 159, 539))
        self.walls.append(Wall(161, 536, 121, 356))
        self.walls.append(Wall(823, 256, 883, 250))
        self.walls.append(Wall(882, 250, 968, 289))
        self.walls.append(Wall(968, 289, 1006, 344))
        self.walls.append(Wall(823, 256, 883, 250))
        self.walls.append(Wall(882, 250, 968, 289))
        self.walls.append(Wall(968, 289, 1006, 344))
        self.walls.append(Wall(225, 498, 185, 333))
        self.walls.append(Wall(185, 333, 191, 246))
        self.walls.append(Wall(191, 246, 333, 170))
        self.walls.append(Wall(347, 162, 643, 184))
        self.walls.append(Wall(643, 185, 357, 354))
        self.walls.append(Wall(357, 354, 365, 429))
        self.walls.append(Wall(365, 429, 681, 397))
        self.walls.append(Wall(681, 397, 819, 318))
        self.walls.append(Wall(819, 318, 914, 328))
        self.walls.append(Wall(914, 328, 961, 422))
        self.walls.append(Wall(961, 422, 869, 506))
        self.walls.append(Wall(869, 506, 231, 495))
        self.walls.append(Wall(231, 495, 195, 336))

        

    def set_gates(self):
        self.gates.append(RewardGate(193, 197, 147, 183))
        self.gates.append(RewardGate(187, 235, 137, 221))
        self.gates.append(RewardGate(178, 260, 128, 265))
        self.gates.append(RewardGate(131, 323, 175, 315))
        self.gates.append(RewardGate(153, 373, 180, 357))
        self.gates.append(RewardGate(183, 430, 215, 387))
        self.gates.append(RewardGate(276, 469, 299, 429))
        self.gates.append(RewardGate(351, 481, 351, 453))
        self.gates.append(RewardGate(424, 481, 425, 443))
        self.gates.append(RewardGate(523, 478, 515, 439))
        self.gates.append(RewardGate(618, 465, 601, 429))
        self.gates.append(RewardGate(704, 425, 657, 417))
        self.gates.append(RewardGate(642, 343, 594, 372))
        self.gates.append(RewardGate(558, 303, 527, 331))
        self.gates.append(RewardGate(511, 277, 473, 308))
        self.gates.append(RewardGate(456, 255, 420, 265))
        self.gates.append(RewardGate(459, 229, 449, 195))
        self.gates.append(RewardGate(511, 231, 520, 201))
        self.gates.append(RewardGate(561, 239, 575, 205))
        self.gates.append(RewardGate(634, 249, 645, 215))
        self.gates.append(RewardGate(692, 262, 714, 235))
        self.gates.append(RewardGate(742, 289, 760, 265))
        self.gates.append(RewardGate(788, 314, 809, 287))
        self.gates.append(RewardGate(847, 335, 849, 288))
        self.gates.append(RewardGate(919, 325, 909, 291))
        self.gates.append(RewardGate(976, 287, 943, 245))
        self.gates.append(RewardGate(999, 211, 963, 197))
        self.gates.append(RewardGate(987, 118, 944, 141))
        self.gates.append(RewardGate(917, 59, 879, 83))
        self.gates.append(RewardGate(800, 37, 785, 81))
        self.gates.append(RewardGate(666, 38, 667, 82))
        self.gates.append(RewardGate(568, 35, 563, 91))
        self.gates.append(RewardGate(442, 35, 447, 87))
        self.gates.append(RewardGate(337, 37, 345, 87))
        self.gates.append(RewardGate(247, 41, 261, 99))
        self.gates.append(RewardGate(179, 53, 217, 90))

    def new_episode(self):
        self.car.reset()


    def get_state(self):
        return self.car.getState()
        

    def make_action(self, action):
        # returns reward
        actionNo = np.argmax(action)
        self.car.updateWithAction(actionNo)
        return self.car.reward

    def is_episode_finished(self):
        return self.car.dead

    def get_score(self):
        return self.car.score

    def get_lifespan(self):
        return self.car.lifespan

    def render(self):
        glPushMatrix()
        #
        # glTranslatef(-1, -1, 0)
        # glScalef(1 / (displayWidth / 2), 1 / (displayHeight / 2), 1)

        # self.clear()
        self.trackSprite.draw()
        self.car.show()

        for w in self.walls:
            w.draw()
        for g in self.gates:
            g.draw()

        glPopMatrix()


class Wall:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = displayHeight - y1
        self.x2 = x2
        self.y2 = displayHeight - y2

        self.line = Line(self.x1, self.y1, self.x2, self.y2)
        self.line.setLineThinkness(2)

    """
    draw the line
    """

    def draw(self):
        self.line.draw()

    """
    returns true if the car object has hit this wall
    """

    def hitCar(self, car):
        global vec2
        cw = car.width
        # since the car sprite isn't perfectly square the hitbox is a little smaller than the width of the car
        ch = car.height - 4
        rightVector = vec2(car.direction)
        upVector = vec2(car.direction).rotate(-90)
        carCorners = []
        cornerMultipliers = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        carPos = vec2(car.x, car.y)
        for i in range(4):
            carCorners.append(carPos + (rightVector * cw / 2 * cornerMultipliers[i][0]) +
                              (upVector * ch / 2 * cornerMultipliers[i][1]))

        for i in range(4):
            j = i + 1
            j = j % 4
            if linesCollided(self.x1, self.y1, self.x2, self.y2, carCorners[i].x, carCorners[i].y, carCorners[j].x,
                             carCorners[j].y):
                return True
        return False


"""
class containing all the game logic for moving and displaying the car
"""


class RewardGate:

    def __init__(self, x1, y1, x2, y2):
        global vec2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.active = True

        self.line = Line(self.x1, self.y1, self.x2, self.y2)
        self.line.setLineThinkness(1)
        self.line.setColor([0, 255, 0])

        self.center = vec2((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)

    """
    draw the line
    """

    def draw(self):
        if self.active:
            self.line.draw()

    """
    returns true if the car object has hit this wall
    """

    def hitCar(self, car):
        if not self.active:
            return False

        global vec2
        cw = car.width
        # since the car sprite isn't perfectly square the hitbox is a little smaller than the width of the car
        ch = car.height - 4
        rightVector = vec2(car.direction)
        upVector = vec2(car.direction).rotate(-90)
        carCorners = []
        cornerMultipliers = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        carPos = vec2(car.x, car.y)
        #print("Car Pos x/y: " + str(car.x) + str(car.y))
        #print("Next Reward Gate: " + str(self.x1) + str(self.y1))
        for i in range(4):
            carCorners.append(carPos + (rightVector * cw / 2 * cornerMultipliers[i][0]) +
                              (upVector * ch / 2 * cornerMultipliers[i][1]))

        for i in range(4):
            j = i + 1
            j = j % 4
            if linesCollided(self.x1, self.y1, self.x2, self.y2, carCorners[i].x, carCorners[i].y, carCorners[j].x,
                             carCorners[j].y):
                return True
        return False


class Car:

    def __init__(self, walls, rewardGates):
        global vec2
        self.x = 174
        self.y = 141
        self.vel = 0
        self.direction = vec2(0, 1)
        self.direction = self.direction.rotate(180 / 12)
        self.acc = 0
        self.scalefactor = 0.6
        self.width = int(40*self.scalefactor)
        self.height = int(30*self.scalefactor)
        self.turningRate = 5.0 / self.width
        self.friction = 0.98
        self.maxSpeed = self.width / 4.0
        self.maxReverseSpeed = -1 * self.maxSpeed / 2.0
        self.accelerationSpeed = self.width / 160.0
        self.dead = False
        self.driftMomentum = 0
        self.driftFriction = 0.87
        self.lineCollisionPoints = []
        self.collisionLineDistances = []
        self.vectorLength = 300
        self.rewardAdditional = 0

        self.carPic = pyglet.image.load('images/car.png')
        self.carSprite = pyglet.sprite.Sprite(self.carPic, x=self.x, y=self.y)
        self.carSprite.update(rotation=0, scale_x=self.width / self.carSprite.width,
                              scale_y=self.height / self.carSprite.height)

        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False
        self.walls = walls
        self.rewardGates = rewardGates
        self.rewardNo = 0

        self.directionToRewardGate = self.rewardGates[self.rewardNo].center - vec2(self.x, self.y)
        #print("X Coordinate of first Gate:" + str(self.rewardGates[self.rewardNo].y1))

        self.reward = 0

        self.score = 0
        self.lifespan = 0
    """
    draws the car to the screen
    """

    def reset(self):
        global vec2
        self.x = 174
        self.y = 141
        self.vel = 0
        self.direction = vec2(0, 1)
        self.direction = self.direction.rotate(180 / 12)
        self.acc = 0
        self.dead = False
        self.driftMomentum = 0
        self.lineCollisionPoints = []
        self.collisionLineDistances = []

        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False
        self.rewardNo = 0
        self.reward = 0
        self.rewardAdditional = 0

        self.lifespan = 0
        self.score = 0
        for g in self.rewardGates:
            g.active = True

    def show(self):
        # first calculate the center of the car in order to allow the
        # rotation of the car to be anchored around the center
        upVector = self.direction.rotate(90)
        drawX = self.direction.x * self.width / 2 + upVector.x * self.height / 2
        drawY = self.direction.y * self.width / 2 + upVector.y * self.height / 2
        self.carSprite.update(x=self.x - drawX, y=self.y - drawY, rotation=-get_angle(self.direction))
        self.carSprite.draw()
        # self.showCollisionVectors()

    """
     returns a vector of where a point on the car is after rotation 
     takes the position desired relative to the center of the car when the car is facing to the right
    """

    def getPositionOnCarRelativeToCenter(self, right, up):
        global vec2
        w = self.width
        h = self.height
        rightVector = vec2(self.direction)
        rightVector.normalize()
        upVector = self.direction.rotate(90)
        upVector.normalize()

        return vec2(self.x, self.y) + ((rightVector * right) + (upVector * up))

    def updateWithAction(self, actionNo):
        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False

        if actionNo == 0:
            self.turningLeft = True
        elif actionNo == 1:
            self.turningRight = True
        elif actionNo == 2:
            self.accelerating = True
        elif actionNo == 3:
            self.reversing = True
        elif actionNo == 4:
            self.accelerating = True
            self.turningLeft = True
        elif actionNo == 5:
            self.accelerating = True
            self.turningRight = True
        elif actionNo == 6:
            self.reversing = True
            self.turningLeft = True
        elif actionNo == 7:
            self.reversing = True
            self.turningRight = True
        elif actionNo == 8:
            pass
        totalReward = 0

        for i in range(1):
            if not self.dead:
                self.lifespan+=1
                self.move()
                self.updateControls()

                if self.hitAWall():
                    self.dead = True
                    # return
                self.checkRewardGates()
                #print(self.rewardAdditional)
                #print(totalReward)
                #print(totalReward)
                #print("totalReward: " + str(totalReward))
                #print("totalAdditional Reward: " + str(self.rewardAdditional))
                #print("self.reward: " + str(self.reward))
                
        #print(self.reward)
        self.setVisionVectors()

        # self.update()

        self.reward += totalReward

    """
    called every frame
    """

    def update(self):
        if not self.dead:
            self.updateControls()
            self.move()

            if self.hitAWall():
                self.dead = True
                # return
            self.checkRewardGates()
            self.setVisionVectors()

    def checkRewardGates(self):
        global vec2
        self.rewardPenalty = -1
        self.rewardAdditional = 0
        if self.rewardGates[self.rewardNo].hitCar(self):
            #print("Hit a gate!")
            self.rewardGates[self.rewardNo].active = False
            self.rewardNo += 1
            self.score += 1
            self.rewardAdditional += 50 # This works, it's actually 9
            #print("rewardAdditional after hittting gate: " + str(self.rewardAdditional))
            if self.rewardNo == len(self.rewardGates):
                self.rewardNo = 0
                for g in self.rewardGates:
                    g.active = True
        self.reward = self.reward + self.rewardAdditional + self.rewardPenalty

        self.directionToRewardGate = self.rewardGates[self.rewardNo].center - vec2(self.x, self.y)

    """
    changes the position of the car to account for acceleration, velocity, friction and drift
    """

    def move(self):
        global vec2
        self.vel += self.acc
        self.vel *= self.friction
        self.constrainVel()

        driftVector = vec2(self.direction)
        driftVector = driftVector.rotate(90)

        addVector = vec2(0, 0)
        addVector.x += self.vel * self.direction.x
        addVector.x += self.driftMomentum * driftVector.x
        addVector.y += self.vel * self.direction.y
        addVector.y += self.driftMomentum * driftVector.y
        self.driftMomentum *= self.driftFriction

        if addVector.length() != 0:
            addVector.normalize()

        addVector.x * abs(self.vel)
        addVector.y * abs(self.vel)

        self.x += addVector.x
        self.y += addVector.y

    """
    keeps the velocity of the car within the maximum and minimum speeds
    """

    def constrainVel(self):
        if self.maxSpeed < self.vel:
            self.vel = self.maxSpeed
        elif self.vel < self.maxReverseSpeed:
            self.vel = self.maxReverseSpeed

    """
    changes the cars direction and acceleration based on the users inputs
    """

    def updateControls(self):
        multiplier = 1
        if abs(self.vel) < 5:
            multiplier = abs(self.vel) / 5
        if self.vel < 0:
            multiplier *= -1

        driftAmount = self.vel * self.turningRate * self.width / (9.0 * 8.0)
        if self.vel < 5:
            driftAmount = 0

        if self.turningLeft:
            self.direction = self.direction.rotate(radiansToAngle(self.turningRate) * multiplier)

            self.driftMomentum -= driftAmount
        elif self.turningRight:
            self.direction = self.direction.rotate(-radiansToAngle(self.turningRate) * multiplier)
            self.driftMomentum += driftAmount
        self.acc = 0
        if self.accelerating:
            if self.vel < 0:
                self.acc = 3 * self.accelerationSpeed
            else:
                self.acc = self.accelerationSpeed
        elif self.reversing:
            if self.vel > 0:
                self.acc = -3 * self.accelerationSpeed
            else:
                self.acc = -1 * self.accelerationSpeed

    """
    checks every wall and if the car has hit a wall returns true    
    """

    def hitAWall(self):
        for wall in self.walls:
            if wall.hitCar(self):
                return True

        return False

    """
    returns the point of collision of a line (x1,y1,x2,y2) with the walls, 
    if multiple walls are hit it returns the closest collision point
    """

    def getCollisionPointOfClosestWall(self, x1, y1, x2, y2):
        global vec2
        minDist = 2 * displayWidth
        closestCollisionPoint = vec2(0, 0)
        for wall in self.walls:
            collisionPoint = getCollisionPoint(x1, y1, x2, y2, wall.x1, wall.y1, wall.x2, wall.y2)
            if collisionPoint is None:
                continue
            if dist(x1, y1, collisionPoint.x, collisionPoint.y) < minDist:
                minDist = dist(x1, y1, collisionPoint.x, collisionPoint.y)
                closestCollisionPoint = vec2(collisionPoint)
        return closestCollisionPoint

    """
    by creating lines in many directions from the car and getting the closest collision point of that line
    we create  "vision vectors" which will allow the car to 'see' 
    kinda like a sonar system
    """

    def getState(self):
        self.setVisionVectors()
        normalizedVisionVectors = [1 - (max(1.0, line) / self.vectorLength) for line in self.collisionLineDistances]

        normalizedForwardVelocity = max(0.0, self.vel / self.maxSpeed)
        normalizedReverseVelocity = max(0.0, self.vel / self.maxReverseSpeed)
        if self.driftMomentum > 0:
            normalizedPosDrift = self.driftMomentum / 5
            normalizedNegDrift = 0
        else:
            normalizedPosDrift = 0
            normalizedNegDrift = self.driftMomentum / -5

        normalizedAngleOfNextGate = (get_angle(self.direction) - get_angle(self.directionToRewardGate)) % 360
        if normalizedAngleOfNextGate > 180:
            normalizedAngleOfNextGate = -1 * (360 - normalizedAngleOfNextGate)

        normalizedAngleOfNextGate /= 180

        normalizedState = [*normalizedVisionVectors, normalizedForwardVelocity, normalizedReverseVelocity,
                           normalizedPosDrift, normalizedNegDrift, normalizedAngleOfNextGate]
        return np.array(normalizedState)

    def setVisionVectors(self):
        h = self.height - 4
        w = self.width
        self.collisionLineDistances = []
        self.lineCollisionPoints = []
        self.setVisionVector(w / 2, 0, 0)
        self.setVisionVector(w / 2, -h / 2, -180 / 16)
        self.setVisionVector(w / 2, -h / 2, -180 / 4)
        self.setVisionVector(w / 2, -h / 2, -4 * 180 / 8)

        self.setVisionVector(w / 2, h / 2, 180 / 16)
        self.setVisionVector(w / 2, h / 2, 180 / 4)
        self.setVisionVector(w / 2, h / 2, 4 * 180 / 8)

        self.setVisionVector(-w / 2, -h / 2, -6 * 180 / 8)
        self.setVisionVector(-w / 2, h / 2, 6 * 180 / 8)
        self.setVisionVector(-w / 2, 0, 180)

    """
    calculates and stores the distance to the nearest wall given a vector 
    """

    def setVisionVector(self, startX, startY, angle):
        collisionVectorDirection = self.direction.rotate(angle)
        collisionVectorDirection = collisionVectorDirection.normalize() * self.vectorLength
        startingPoint = self.getPositionOnCarRelativeToCenter(startX, startY)
        collisionPoint = self.getCollisionPointOfClosestWall(startingPoint.x, startingPoint.y,
                                                             startingPoint.x + collisionVectorDirection.x,
                                                             startingPoint.y + collisionVectorDirection.y)
        if collisionPoint.x == 0 and collisionPoint.y == 0:
            self.collisionLineDistances.append(self.vectorLength)
        else:
            self.collisionLineDistances.append(
                dist(startingPoint.x, startingPoint.y, collisionPoint.x, collisionPoint.y))
        self.lineCollisionPoints.append(collisionPoint)

    """
    shows dots where the collision vectors detect a wall 
    """

    def showCollisionVectors(self):
        global drawer
        for point in self.lineCollisionPoints:
            drawer.setColor([255, 0, 0])
            drawer.circle(point.x, point.y, 5)
