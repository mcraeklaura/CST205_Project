__author__ = 'lauramcrae'
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
window = 0                                             # glut window number
width, height = 1000, 1000                               # window size
right = 100
left = 100
recx = 10
recy = 10
velx = 24
vely = 22

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()



def draw():
    global recx
    global recy
    global velx
    global vely                                         # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()
    refresh2d(width, height)                                  # reset position
    
    
    glColor3f(0.0, 0.0, 1.0)
    
    #while  xaxis < 200 and yaxis < 200:
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    
    draw_rect(recx, recy, right, left)
    draw_rect(recx + 100, recy - 100, right - 50, left - 50)
    
    
    
    recx = recx + velx
    recy = recy + vely
    # ToDo draw rectangle
    if recx < 0:
        velx = 24
    if recy < 0:
        vely = 22
    if recx > 1000:
        velx = -24
    if recy > 1000:
        vely = -22
    
    
    glutSwapBuffers()                                  # important for double buffering


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Display Window")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything