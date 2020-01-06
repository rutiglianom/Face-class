# Matthew Rutigliano
# ECEGR 3910
# November 22nd, 2019
# AS.17: Graphics Class
# Description: Demonstration of face class, showing the move function, blink animation, and spinning animation

from graphics import *

class Face:
    def __init__(self, xloc, yloc, height, skinColor, eyeColor, window):
        self.__xloc = xloc   # private to class
        self.__yloc = yloc   # private to class
        self.skinColor = skinColor
        self.eyeColor = eyeColor
        self.window = window
        self.vert = height/2
        self.coVert = self.vert/2
        self.eyeRad = self.vert/5
        self.mouthHeight = self.vert/50
        
        self.head = Oval(Point(self.__xloc - self.coVert,self.__yloc + self.vert), Point(self.__xloc + self.coVert, self.__yloc - self.vert))        
        self.eye1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad)
        self.iris1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad/2)
        self.pupil1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad/4)
        
        self.closedEye1 = Rectangle(Point(self.__xloc - self.coVert/2 - self.eyeRad, self.__yloc + self.coVert + self.vert/100),
                                    Point(self.__xloc - self.coVert/2 + self.eyeRad, self.__yloc + self.coVert))
        
        self.eye2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad)
        self.iris2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad/2)
        self.pupil2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad/4)
        
        self.closedEye2 = Rectangle(Point(self.__xloc + self.coVert/2 - self.eyeRad, self.__yloc + self.coVert + self.vert/100),
                                    Point(self.__xloc + self.coVert/2 + self.eyeRad, self.__yloc + self.coVert))
        
        self.mouth = Rectangle(Point(self.__xloc - self.coVert/2, self.__yloc - self.coVert),
                               Point(self.__xloc + self.coVert/2, self.__yloc - self.coVert - self.mouthHeight))
        self.__fillInit()
        
    def __fillInit(self):
        self.head.setFill(self.skinColor)
        self.eye1.setFill('white')
        self.iris1.setFill(self.eyeColor)
        self.iris1.setOutline(self.eyeColor)
        self.pupil1.setFill('black')
        self.eye2.setFill('white')
        self.iris2.setFill(self.eyeColor)
        self.iris2.setOutline(self.eyeColor)
        self.pupil2.setFill('black')
        self.mouth.setFill('black')
        self.closedEye1.setFill('black')
        self.closedEye2.setFill('black')

        
    def faceDraw(self):
        self.head.draw(self.window)
        self.eye1.draw(self.window)
        self.iris1.draw(self.window)
        self.pupil1.draw(self.window)
        self.eye2.draw(self.window)
        self.iris2.draw(self.window)
        self.pupil2.draw(self.window)
        self.mouth.draw(self.window)
        
    def faceUndraw(self):
        self.head.undraw()
        self.eye1.undraw()
        self.iris1.undraw()
        self.pupil1.undraw()
        self.eye2.undraw()
        self.iris2.undraw()
        self.pupil2.undraw()
        self.mouth.undraw()
        
    def faceMove(self, xdir, ydir):
        self.head.move(xdir,ydir)
        self.eye1.move(xdir,ydir)
        self.iris1.move(xdir,ydir)
        self.pupil1.move(xdir,ydir)
        self.closedEye1.move(xdir,ydir)
        self.eye2.move(xdir,ydir)
        self.iris2.move(xdir,ydir)
        self.pupil2.move(xdir,ydir)
        self.closedEye2.move(xdir,ydir)
        self.mouth.move(xdir,ydir)
        self.__xloc += xdir
        self.__yloc += ydir
    
    def getX(self):
        return self.__xloc

    def getY(self):
        return self.__yloc
        
    def blink(self):
        self.eye1.undraw()
        self.iris1.undraw()
        self.pupil1.undraw()
        self.eye2.undraw()
        self.iris2.undraw()
        self.pupil2.undraw()
        
        self.closedEye1.draw(self.window)
        self.closedEye2.draw(self.window)
        
        time.sleep(.5)
        
        self.closedEye1.undraw()
        self.closedEye2.undraw()
        
        self.eye1.draw(self.window)
        self.iris1.draw(self.window)
        self.pupil1.draw(self.window)
        self.eye2.draw(self.window)
        self.iris2.draw(self.window)
        self.pupil2.draw(self.window)
        
        time.sleep(.5)
        
    def spin(self, spinTime):
        # Turn 1
        self.faceUndraw()
        self.head = Oval(Point(self.__xloc - self.vert,self.__yloc + self.coVert), Point(self.__xloc + self.vert, self.__yloc - self.coVert))
        self.eye1 = Circle(Point(self.__xloc + self.coVert, self.__yloc + self.coVert/2), self.eyeRad)
        self.iris1 = Circle(Point(self.__xloc + self.coVert, self.__yloc + self.coVert/2), self.eyeRad/2)
        self.pupil1 = Circle(Point(self.__xloc + self.coVert, self.__yloc + self.coVert/2), self.eyeRad/4)
        self.eye2 = Circle(Point(self.__xloc + self.coVert, self.__yloc - self.coVert/2), self.eyeRad)
        self.iris2 = Circle(Point(self.__xloc + self.coVert, self.__yloc - self.coVert/2), self.eyeRad/2)
        self.pupil2 = Circle(Point(self.__xloc + self.coVert, self.__yloc - self.coVert/2), self.eyeRad/4)
        self.mouth = Rectangle(Point(self.__xloc - self.coVert, self.__yloc + self.coVert/2),
                               Point(self.__xloc - self.coVert - self.mouthHeight, self.__yloc - self.coVert/2))
        
        self.__fillInit()

        self.faceDraw()
        time.sleep(spinTime)
        
        # Turn 2
        self.faceUndraw()
        self.head = Oval(Point(self.__xloc - self.coVert,self.__yloc + self.vert), Point(self.__xloc + self.coVert, self.__yloc - self.vert))
        self.eye1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc - self.coVert), self.eyeRad)
        self.iris1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc - self.coVert), self.eyeRad/2)
        self.pupil1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc - self.coVert), self.eyeRad/4)
        self.eye2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc - self.coVert), self.eyeRad)
        self.iris2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc - self.coVert), self.eyeRad/2)
        self.pupil2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc - self.coVert), self.eyeRad/4)
        self.mouth = Rectangle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert),
                               Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert + self.mouthHeight))
        
        self.__fillInit()

        self.faceDraw()
        time.sleep(spinTime)
        
        # Turn 3
        self.faceUndraw()
        self.head = Oval(Point(self.__xloc - self.vert,self.__yloc + self.coVert), Point(self.__xloc + self.vert, self.__yloc - self.coVert))
        self.eye1 = Circle(Point(self.__xloc - self.coVert, self.__yloc + self.coVert/2), self.eyeRad)
        self.iris1 = Circle(Point(self.__xloc - self.coVert, self.__yloc + self.coVert/2), self.eyeRad/2)
        self.pupil1 = Circle(Point(self.__xloc - self.coVert, self.__yloc + self.coVert/2), self.eyeRad/4)
        self.eye2 = Circle(Point(self.__xloc - self.coVert, self.__yloc - self.coVert/2), self.eyeRad)
        self.iris2 = Circle(Point(self.__xloc - self.coVert, self.__yloc - self.coVert/2), self.eyeRad/2)
        self.pupil2 = Circle(Point(self.__xloc - self.coVert, self.__yloc - self.coVert/2), self.eyeRad/4)
        self.mouth = Rectangle(Point(self.__xloc + self.coVert, self.__yloc + self.coVert/2),
                               Point(self.__xloc + self.coVert - self.mouthHeight, self.__yloc - self.coVert/2))
        
        self.__fillInit()

        self.faceDraw()
        time.sleep(spinTime)
        
        # Return to normal
        self.faceUndraw()
        self.head = Oval(Point(self.__xloc - self.coVert,self.__yloc + self.vert), Point(self.__xloc + self.coVert, self.__yloc - self.vert))
        self.eye1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad)
        self.iris1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad/2)
        self.pupil1 = Circle(Point(self.__xloc - self.coVert/2, self.__yloc + self.coVert), self.eyeRad/4)
        self.eye2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad)
        self.iris2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad/2)
        self.pupil2 = Circle(Point(self.__xloc + self.coVert/2, self.__yloc + self.coVert), self.eyeRad/4)
        self.mouth = Rectangle(Point(self.__xloc - self.coVert/2, self.__yloc - self.coVert),
                               Point(self.__xloc + self.coVert/2, self.__yloc - self.coVert - self.mouthHeight))
        
        self.__fillInit()

        self.faceDraw()
        time.sleep(spinTime)

# Main
WIN_WIDTH = 800
WIN_HEIGHT = 800

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT)
win.setCoords(0, 0, WIN_WIDTH, WIN_HEIGHT)
win.setBackground("white")

scott = Face(250, 400, 500, 'tan', 'brown', win)
scott.faceDraw()
time.sleep(1)
scott.faceMove(250, 0)
time.sleep(1)
scott.blink()
for i in range(10):
    scott.spin(.05)
scott.faceUndraw()
win.getMouse()