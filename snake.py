from turtle import *
import findPrimes as fp
import random

# Plotting Fibbonacci
# fibb=fp.generate_fibbonacci(200)
# print(fibb)
speed(0)
# for i in fibb:
#     circle(radius=i/100, extent=240)
#     x,y=pos()
#     setx(x)
#     sety(y)
#
# while True:
#     pass


# Writing Snake game
''' 
1. Having a Canvas Size.
2. Showing snake in a the canvas DOT.
3. Food generation
'''
# window_height()
# window_width()
# textinput("Player Name", "Name of first player:")


class Snake:
    # to run the snake on and off the screen
    screenMax=320
    # this is to define the speed of plot
    speed=0
    # keep tab of how many food are eaten
    score=0
    # this to jumps in any direction snake takes i.e can be used for speed of snake
    movementVal=10

    playerName=''
    # snake head size
    snakeHeadSize=30
    snakeHeadColor='cyan'
    snakeColor='black'
    # X and Y coordinates on screen
    x,y= 0,0
    # initialisation of head coordinates
    headX=x
    headY=y
    # Tail length
    tailLength=0
    # initialisation of tail coordinates
    tailX=[x]
    tailY=[y]
    # Food Size
    foodSize=40
    foodColor='red'
    isFoodOnScreen=False
    foodX=2000
    foodY=2000

    screenCanvas=getcanvas()
    snakeTurtle = RawTurtle(screenCanvas)
    foodTurtle = RawTurtle(screenCanvas)
    keyUp='Up'
    keyDown='Down'
    keyLeft='Left'
    keyRight='Right'
    snakeScreen=snakeTurtle.getscreen()
    foodScreen=foodTurtle.getscreen()
    keyAction=snakeScreen.listen()

    turningAngle=90

    def startGame(self):
        # screensize(500, 500)
        self.playerName=textinput("Player Name", "Name of first player:")

        # print(playerName)
        self.snakeTurtle.ht()
        self.snakeTurtle.dot(self.snakeHeadSize, self.snakeHeadColor)
        ht()
        # self.snakeTurtle.ht()
        self.foodTurtle.ht()


    def generateFood(self):
        # Dot function on a random location on canvas
        self.foodX=random.randint(-self.screenMax,self.screenMax)
        self.foodY =random.randint(-self.screenMax, self.screenMax)
        self.foodTurtle.pu()
        self.foodTurtle.setx(self.foodX)
        self.foodTurtle.sety(self.foodY)
        self.foodTurtle.pd()
        self.foodTurtle.dot(self.foodSize,self.foodColor)
        self.isFoodOnScreen=True



    def move(self):
        # printing position
        # print(self.snakeTurtle.pos())
        self.x,self.y=self.snakeTurtle.pos()



        for i in range(len(self.tailX)):
            self.snakeTurtle.pu()
            self.snakeTurtle.setx(self.tailX[i])
            self.snakeTurtle.sety(self.tailY[i])
            self.snakeTurtle.pd()
            if(i==0):
                self.snakeTurtle.pu()
                self.snakeTurtle.dot(self.snakeHeadSize, self.snakeHeadColor)
                self.snakeTurtle.pu()
            else:
                self.snakeTurtle.pd()
                self.snakeTurtle.dot(self.snakeHeadSize, self.snakeColor)
            # self.i += 1
        self.snakeTurtle.clear()






        # if direction is 'x':
        if((self.x<=self.screenMax and self.x>=-self.screenMax) and (self.y <= self.screenMax and self.y >= -self.screenMax)):

            # self.snakeTurtle.ht()
            self.snakeTurtle.fd(self.movementVal)
            # self.snakeTurtle.st()
            self.x, self.y = self.snakeTurtle.pos()
            # self.x + self.movementVal

        elif self.x>self.screenMax or self.x<-self.screenMax:
            self.snakeTurtle.penup()
            self.x, self.y = self.snakeTurtle.pos()
            if self.x>self.screenMax:
                # self.snakeTurtle.ht()
                self.snakeTurtle.setx(-self.screenMax+self.movementVal)
                # self.snakeTurtle.st()
                print('X reset to {}'.format(-self.screenMax))

            elif self.x<-self.screenMax:
                # self.snakeTurtle.ht()
                self.snakeTurtle.setx(self.screenMax-self.movementVal)
                # self.snakeTurtle.st()
                print('X reset to {}'.format(self.screenMax))
            self.snakeTurtle.pendown()
        elif self.y > self.screenMax or self.y < -self.screenMax:
            self.snakeTurtle.penup()
            self.x, self.y = self.snakeTurtle.pos()
            if self.y > self.screenMax:
                # self.snakeTurtle.ht()
                self.snakeTurtle.sety(-self.screenMax+self.movementVal)
                # self.snakeTurtle.st()
                print('Y reset to {}'.format(-self.screenMax))

            elif self.y < -self.screenMax:
                # self.snakeTurtle.ht()
                self.snakeTurtle.sety(self.screenMax-self.movementVal)
                # self.snakeTurtle.st()
                print('Y reset to {}'.format(self.screenMax))
            self.snakeTurtle.pendown()

        else:
            pass

        # elif direction is 'y':
        # if (self.y <= self.screenMax and self.y >= -self.screenMax):
        #     self.snakeTurtle.fd(self.movementVal)
        #     self.x,self.y=self.snakeTurtle.pos()

        self.snakeTurtle.dot(self.snakeHeadSize, self.snakeColor)

        pass

    def changeDirectionLeft():
        Snake.snakeTurtle.lt(90)
        Snake.movementDirection='y'


    def changeDirectionRight():
        Snake.snakeTurtle.rt(90)
        Snake.movementDirection = 'x'

    # def changeDirectionUp():
    #     Snake.snakeTurtle.setheading(180)
    #
    # def changeDirectionDown():
    #     Snake.snakeTurtle.setheading(270)


    def eatFood(self):
        self.foodScreen.clear()
        self.generateFood()
        self.isFoodOnScreen=True
        self.score+=1
        self.tailLength+=1
        self.movementVal+=1


    def endGame(self):
        pass
    def updateScore(self):
        pass

    def __init__(self):
        title("Welcome {0},  SnakeGame.py ".format(self.playerName))
        self.startGame()

        while True:
            # print(listen())
            Snake.keyAction=self.snakeScreen.listen()

            # self.snakeScreen.onkey(Snake.changeDirectionUp,self.keyUp)
            # self.snakeScreen.onkey(Snake.changeDirectionDown, self.keyDown)
            self.foodScreen.onkeyrelease(Snake.changeDirectionLeft, self.keyLeft)
            self.foodScreen.onkeyrelease(Snake.changeDirectionRight, self.keyRight)
            if self.isFoodOnScreen is False:
                self.generateFood()
            self.move()

            if (self.x<=self.foodX+self.foodSize and self.x >= self.foodX-self.foodSize) and (self.y<=self.foodY+self.foodSize and self.y>=self.foodY-self.foodSize):
                print ('Snake ate Food')
                self.eatFood()
                self.isFoodOnScreen=False

            print('Food location is {0},{1}'.format(self.foodX, self.foodY))
            print('Snake Location is {0},{1}'.format(self.x,self.y))

            if (len(self.tailX) < self.tailLength):
                if((self.x>0 and self.x>self.screenMax)):
                    self.tailX.append(self.screenMax)
                elif(self.x<0 and self.x<-self.screenMax):
                    self.tailX.append(-self.screenMax)
                else:
                    self.tailX.append(self.x)


                if ((self.y > 0 and self.y > self.screenMax)):
                    self.tailY.append(self.screenMax)
                elif (self.y < 0 and self.y < -self.screenMax):
                    self.tailY.append(-self.screenMax)
                else:
                    self.tailY.append(self.y)

            #     if abs(self.screenMax+self.movementVal)>abs(self.x) else self.screenMax
            else:
                self.tailX.pop(0)
                self.tailY.pop(0)
                if ((self.x > 0 and self.x > self.screenMax)):
                    self.tailX.append(self.screenMax)
                elif (self.x < 0 and self.x < -self.screenMax):
                    self.tailX.append(-self.screenMax)
                else:
                    self.tailX.append(self.x)

                if ((self.y > 0 and self.y > self.screenMax)):
                    self.tailY.append(self.screenMax)
                elif (self.y < 0 and self.y < -self.screenMax):
                    self.tailY.append(-self.screenMax)
                else:
                    self.tailY.append(self.y)

            print('Tail is{}{}'.format(self.tailX, self.tailY))
            title('{0} Your Score is {1}'.format(self.playerName,self.score))
            # for i in range(0,self.tailLength):
            #     self.snakeTurtle.dot(self.snakeHeadSize, self.snakeColor)






            # print(Snake.keyAction)
            # mainloop()

speed(0)
b=Snake()
mainloop()



