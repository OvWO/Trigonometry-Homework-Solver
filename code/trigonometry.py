#! /usr/bin/python
# -*- coding: utf-8 -*-

import math as m, termcolor as tm

def bienvenida():
	print ""
	print tm.colored ('   ####################################################################','yellow')
	# print tm.colored ('   ### ESCUELA PREPARATORIA FEDERAL POR COOPERACION LAZARO CARDENAS ###','yellow')
	print tm.colored ('   ###                MATEMATICAS II; TRIGONOMETRIA                 ###','yellow')
	print tm.colored ('   ###                      PROFESOR: SANTOS                        ###','yellow')
	print tm.colored ('   ###           ALUMNOS: LUIS CARLOS LOPEZ V, ADAN CAÑAMAR         ###','yellow')
	print tm.colored ('   ####################################################################','yellow')
def vuelta():
	while True:
		bienvenida()
		tri = com_tri()
		va_tri = escoger_angulo(tri)
		hacer_operaciones(va_tri)

		i = int(salir())

		if i == 9:
			quit()
def com_tri():
	py_h = False
	py_x = False
	py_y = False

	print tm.colored('\nIntroduce los valores de las partes conocidas del triangulo: \n', 'green')

	try:
		h = float(input("Hypotenusa: "))
	except SyntaxError:
		print tm.colored('Hypotenusa desconocida!!!', 'red')
		py_h = True


	try:
		x = float(input("Introduce el Valor de X: "))
	except SyntaxError:
		print tm.colored('X desconocida!!!', 'red')
		py_x = True


	try:
		y = float(input("Introduce el Valor de Y: "))
	except SyntaxError:
		print tm.colored('Y desconocida', 'red')
		py_y = True

	###Estas operaciones de abajo completan los valores faltantes del triangulo
	if py_h == True:
		h = round(m.hypot(x,y),1)
	if py_x == True:
		x = round(m.sqrt(h*h-y*y),1)
	if py_y == True:
		y = round(m.sqrt(h*h-x*x),1)

	tri = {"h":h,"x":x,"y":y}
	return tri
def hacer_operaciones (va_tri):

	h = va_tri["h"]
	a = va_tri["a"]
	o = va_tri["o"]

	print tm.colored('\tSen: ', 'blue'), tm.colored(round(o/h,4), 'cyan')
	print tm.colored('\tCos: ', 'blue'), tm.colored(round(a/h,4), 'cyan')
	print tm.colored('\tTan: ', 'blue'), tm.colored(round(o/a,4), 'cyan')
	print tm.colored('\tCsc: ', 'blue'), tm.colored(round(h/o,4), 'cyan')
	print tm.colored('\tSec: ', 'blue'), tm.colored(round(h/a,4), 'cyan')
	print tm.colored('\tCot: ', 'blue'), tm.colored(round(a/o,4), 'cyan')

	print tm.colored ('\nEl valor del angulo en grados, minutos y segundos convertido\nusando la funcion seno es: \n','blue'),tm.colored(gms(round(m.degrees(m.asin(o/h)),4)),'magenta')
def escoger_angulo(tri):
	h = tri["h"]
	x = tri["x"]
	y = tri["y"]

	print tm.colored('\n¿De qué ángulo te gustaria conocer el valor?', 'green')
	print """
	X'OA (1)
	X'OB (2)
	X'OC (3)
	X'OD (4)
	"""
	c = input(tm.colored('Tienes que introducir el numero de la funcion que te gustaria obtener: ', 'green'))
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

	va_tri = {"h":h,"o":o,"a":a,"ang":ang}
	return va_tri
def salir():

	return raw_input(tm.colored('\n\tSi quieres salir presiona (9)\n\tSi no, presiona cualquier otro numero: ', 'yellow'))
def gms(dd): # convert decimal dot to degrees, minutes and seconds
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   seconds = round(seconds,2)
   return degrees, minutes, seconds

vuelta()