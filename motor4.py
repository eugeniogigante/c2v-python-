#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eugenio
#
# Created:     06/03/2021
# Copyright:   (c) Alberto 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import pygame module in this program
import pygame
import RPi.GPIO as GPIO
import time

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

in1 = 19
in2 = 20
in3	= 16
in4 = 21

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")

# marker current co-ordinates
x = 200
y = 200

# dimensions of the marker
width = 10
height = 10

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
	pygame.time.delay(10)

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:
			# it will make exit the while loop
			run = False
	# stores keys pressed
	keys = pygame.key.get_pressed()

	# if left arrow key is pressed
	if keys[pygame.K_LEFT] :
		# decrement in x co-ordinate
		x -= vel

		# if left arrow key is pressed
	if keys[pygame.K_RIGHT] :
		# increment in x co-ordinate
		x += vel
        # if left arrow key is pressed

    if keys[pygame.K_UP] :
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        y -= vel

		# if left arrow key is pressed
	if keys[pygame.K_DOWN] :
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
		y += vel


	# drawing spot on screen which is rectangle here
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

	# it refreshes the window
	pygame.display.update()

# closes the pygame window
pygame.quit()
