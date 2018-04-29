#! /usr/bin/python
# -*- coding: utf-8 -*-

import math as m, termcolor as tm

def welcome():
	print ""
	print tm.colored ('   ####################################################################','yellow')
	print tm.colored ('   ###                MATEMATICAS II; TRIGONOMETRIA                 ###','yellow')
	print tm.colored ('   ###                      PROFESOR: SANTOS                        ###','yellow')
	print tm.colored ('   ###           ALUMNOS: LUIS CARLOS LOPEZ V, ADAN CAÑAMAR         ###','yellow')
	print tm.colored ('   ####################################################################','yellow')# Welcome message
def loop():
	while True:
		welcome()
		raw_values = input_values()
		raw_values_with_angle = choose_angle(raw_values)
		make_operations(raw_values_with_angle)

		i = int(quit_the_program())

		if i == 9:
			quit()# The loop of the script. Checks if the user wants to quit or it gives a run to the rest of the code.
def input_values():	# This gets the input of the user and completes a value if the user didn't input it.
	# Variables used to check if a value is missing
	py_h = False
	py_x = False
	py_y = False

	print tm.colored('\nInput the values of the known parts of the triangle: \n', 'green')

	try:
		h = float(input("Hypothenusa: "))
	except SyntaxError:
		print tm.colored('Hypothenusa unknown!!!', 'red')
		py_h = True # Set variable to true if value is missing

	try:
		x = float(input("Input the value of X: "))
	except SyntaxError:
		print tm.colored('X unknown!!!', 'red')
		py_x = True

	try:
		y = float(input("Input the value of Y: "))
	except SyntaxError:
		print tm.colored('Y unknown!!!', 'red')
		py_y = True

	if py_h == True:
		h = round(m.hypot(x,y),1)
	if py_x == True:
		x = round(m.sqrt(h*h-y*y),1)
	if py_y == True:
		y = round(m.sqrt(h*h-x*x),1)

	raw_values = {"h":h,"x":x,"y":y}
	return raw_values
def make_operations (raw_values): # Makes the respective trigonometric operations to calculate the value of its function given the input.

	h = raw_values["h"]
	a = raw_values["a"]
	o = raw_values["o"]

	print tm.colored('\tSen: ', 'blue'), tm.colored(round(o/h,4), 'cyan')
	print tm.colored('\tCos: ', 'blue'), tm.colored(round(a/h,4), 'cyan')
	print tm.colored('\tTan: ', 'blue'), tm.colored(round(o/a,4), 'cyan')
	print tm.colored('\tCsc: ', 'blue'), tm.colored(round(h/o,4), 'cyan')
	print tm.colored('\tSec: ', 'blue'), tm.colored(round(h/a,4), 'cyan')
	print tm.colored('\tCot: ', 'blue'), tm.colored(round(a/o,4), 'cyan')

	print tm.colored ('\nThe value of the angle in degrees, minutes and seconds converted \n using the sine function is:: \n','blue'),tm.colored(dms(round(m.degrees(m.asin(o/h)),4)),'magenta')
def choose_angle(tri): # Prompts the user to choose which angle it would like to know the value of in according to the Cartesian plane
	h = tri["h"]
	x = tri["x"]
	y = tri["y"]

	print tm.colored('\nOf what angle would you like to know the angle?', 'green')
	print """
	X'OA (1)
	X'OB (2)
	X'OC (3)
	X'OD (4)
	"""
	c = input(tm.colored('You have to input of the function you would like to know: ', 'green'))
	if c == 1:
		ang = "X'OA"
	if c == 2:
		ang = "X'OB"
	if c == 3:
		ang = "X'OC"
	if c == 4:
		ang = "X'OD"
	print tm.colored('\nLas funciones Trigonometricas del ángulo', 'blue'), tm.colored(ang ,'cyan'), tm.colored('son:\n', 'blue')
	a = x
	o = y

	raw_values_with_angle = {"h":h,"o":o,"a":a,"ang":ang}
	return raw_values_with_angle
def quit_the_program():

	return raw_input(tm.colored('\n\tIf you want to quit prees (9)\n\tIf not, press any other number: ', 'yellow'))
def dms(dd): # convert decimal dot value to -> degrees, minutes and seconds
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   seconds = round(seconds,2)
   return degrees, minutes, seconds

loop()