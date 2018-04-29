#! /usr/bin/python
# -*- coding: utf-8 -*-

import math as m, termcolor as tm

global a
global b
global c
global A
global B
global C

def bienvenida():
	print ""
	print tm.colored ('   ####################################################################','yellow')
	print tm.colored ('   ### ESCUELA PREPARATORIA FEDERAL POR COOPERACION LAZARO CARDENAS ###','yellow')
	print tm.colored ('   ###                MATEMATICAS II; TRIGONOMETRIA                 ###','yellow')
	print tm.colored ('   ###                      PROFESOR: SANTOS                        ###','yellow')
	print tm.colored ('   ###           ALUMNOS: LUIS CARLOS LOPEZ V, ADAN CAÑAMAR         ###','yellow')
	print tm.colored ('   ####################################################################','yellow')
def loop():
	while True:
		bienvenida()
		dibujar_triangulo()
		introducir_datos()
		i = int(salir())
		if i == 9:
			quit()
def introducir_datos():

	print tm.colored('\n\tIntroduce los datos de las partes conocidas del triangulo: \n', 'green')

	try:
		 a = float(input("Introduce el valor de la distancia a: "))
	except SyntaxError:
		print tm.colored('   No se conoce el valor de "a"!!!', 'red')
		a = 0

	try:
		b = float(input("Introduce el valor de la distancia b: "))
	except SyntaxError:
		print tm.colored('   No se conoce el valor de "b"!!!', 'red')
		b = 0 

	try:
		c = float(input("Introduce el valor de la distancia c: "))
	except SyntaxError:
		print tm.colored('   No se conoce el valor de "c"!!!', 'red')
		c = 0

	print tm.colored('\n\tPara introducir los valores de los angulos en G:M:S debes\n\tde hacerlo separado por espacios...\n\t         G  M  S\n\tEjemplo: 90 00 00.00\n','green')

	try:
		in_A = str(raw_input("Introduce el valor de el angulo A: "))
		if not in_A:
			raise SyntaxError
		A = in_A.split(' ')
		if len(A) == 1:
			A.extend(["0"])
		if len(A) == 2:
			A.extend(["0"])
		A = convertir_de_gms_a_g(A[0],A[1],A[2])
	except SyntaxError:
		print tm.colored('   No se conoce el valor de "A"!!!', 'red')
		A = 0

	try:
		in_B = str(raw_input("Introduce el valor de el angulo B: "))
		if not in_B:
			raise SyntaxError
		B = in_B.split(' ')
		if len(B) == 1:
			B.extend(["0"])
		if len(B) == 2:
			B.extend(["0"])
		B = convertir_de_gms_a_g(B[0],B[1],B[2])
	except SyntaxError:
		print tm.colored('   No se conoce el valor de "B"!!!', 'red')
		B = 0

	print "El valor del angulo C siempre es de 90°"

	datos = {'a':a,'b':b,'c':c,'A':A,'B':B}

	resolver_lo_faltante(datos)

def resolver_lo_faltante (datos):
	numeros_que_usaremos = []
	datos_que_usaremos = []

	for i, valor in datos.iteritems():
		if datos[i] != 0:
			numeros_que_usaremos.extend([valor])
			datos_que_usaremos.extend([i])
	if len(numeros_que_usaremos) > 2:
		print tm.colored('Introduciste mas de 2 datos...\nVuelve a introducirlos','red')
		introducir_datos()

	if datos_que_usaremos[0].isupper():
		aux = datos_que_usaremos[0]
		print "aux::", aux
		datos_que_usaremos[0] = datos_que_usaremos[1]
		print "datos 0 ::",datos_que_usaremos[0]
		datos_que_usaremos[1] = aux
		print "datos 1::", datos_que_usaremos[1]


		aux2 = numeros_que_usaremos[0]
		print "aux 2::", aux2
		numeros_que_usaremos[0] = numeros_que_usaremos[1]
		print " numeros 0::", numeros_que_usaremos[0]
		numeros_que_usaremos[1] = aux2
		print " numeros 1::", numeros_que_usaremos[1]

	print datos_que_usaremos,datos_que_usaremos[1]
	print numeros_que_usaremos

	if datos_que_usaremos[0].islower() and datos_que_usaremos[1].islower():
		### a b ###
		if datos_que_usaremos[0] == 'a' and datos_que_usaremos[1] == 'b':
			datos['c'] = round(m.sqrt(pow(numeros_que_usaremos[0],2) + pow(numeros_que_usaremos[1],2)),1)
			datos['A'] = convertir_de_g_a_gms(m.degrees(m.asin(datos['a']/datos['c'])))
			datos['B'] = convertir_de_g_a_gms(m.degrees(m.asin(datos['b']/datos['c'])))
			print "hola"
		### a c ###
		if datos_que_usaremos[0] == 'a' and datos_que_usaremos[1] == 'c':
			if datos_que_usaremos[0] == 'c':
				grande = numeros_que_usaremos[0]
				chico = numeros_que_usaremos[1]
			else:
				grande = numeros_que_usaremos[1]
				chico = numeros_que_usaremos[0]

			print "hola2"
			datos['b'] = round(m.sqrt(m.pow(grande,2) - m.pow(chico,2)),1)
			print datos['a'], datos['c']
			datos['A'] = convertir_de_g_a_gms(m.degrees(m.asin(datos['a']/datos['c'])))
			print datos['a'], datos['c']
			datos['B'] = convertir_de_g_a_gms(m.degrees(m.asin(datos['b']/datos['c'])))
			print datos['a'], datos['c']	

		### b c ###
		if datos_que_usaremos[0] == 'c' and datos_que_usaremos[1] == 'b':
			if datos_que_usaremos[0] == 'c':
				grande = numeros_que_usaremos[0]
				chico = numeros_que_usaremos[1]
				print "dentro 1"
			else:
				grande = numeros_que_usaremos[1]
				chico = numeros_que_usaremos[0]
				print "dentro 2"			
			datos['a'] = round(m.sqrt(m.pow(grande,2) - m.pow(chico,2)),1)
			print datos['a'], datos['c']	
			datos['A'] = convertir_de_g_a_gms(m.degrees(m.cos(datos['a']/datos['c'])))
			print datos['a'], datos['c']	
			datos['B'] = convertir_de_g_a_gms(m.degrees(m.sin(datos['b']/datos['c'])))
			print datos['a'], datos['c']

	if datos_que_usaremos[0].islower() and datos_que_usaremos[1].isupper():
		### a A ###
		if datos_que_usaremos[0] == 'a' and datos_que_usaremos[1] == 'A':
			datos['b'] = round(datos['a']/round(m.tan(m.radians(datos['A'])),4),1)
			datos['c'] = round(datos['a']/round(m.sin(m.radians(datos['A'])),4),1)
			datos['B'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])
		### a B ###
		if datos_que_usaremos[0] == 'a' and datos_que_usaremos[1] == 'B':
			datos['b'] = round(datos['a']/round(m.tan(m.radians(datos['B'])),1),1)
			datos['c'] = round(datos['a']/round(m.cos(m.radians(datos['B'])),1),1)
			datos['A'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])
		### b A
		if datos_que_usaremos[0] == 'b' and datos_que_usaremos[1] == 'A':
			datos['a'] = round(datos['b']/round(m.sin(m.radians(datos['A'])),1),1)
			datos['c'] = round(datos['b']/round(m.cos(m.radians(datos['A'])),1),1)
			datos['B'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])
		### b B
		if datos_que_usaremos[0] == 'b' and datos_que_usaremos[1] == 'B':
			datos['a'] = round(datos['b']/round(m.tan(m.radians(datos['B'])),1),1)
			datos['c'] = round(datos['b']/round(m.sin(m.radians(datos['B'])),1),1)
			datos['A'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])
		### c A
		if datos_que_usaremos[0] == 'c' and datos_que_usaremos[1] == 'A':
			datos['a'] = round(datos['c'] * round(m.sin(m.radians(datos['A'])),4),1)
			datos['b'] = round(datos['c'] * round(m.cos(m.radians(datos['A'])),4),1)
			datos['B'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])
		### c B		
		if datos_que_usaremos[0] == 'c' and datos_que_usaremos[1] == 'B':
			print convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1]
			datos['a'] = round(datos['c'] * round(m.cos(m.radians(datos['B'])),1),1)
			datos['b'] = round(datos['c']/round(m.sin(m.radians(datos['B'])),1),1)
			datos['A'] = convertir_de_g_a_gms(convertir_de_gms_a_g(90,0,0) - numeros_que_usaremos[1])

	print "Los valores finales son...",datos

def salir():

	return raw_input(tm.colored('\n\tSi quieres salir presiona(9)\n\tSi no, presiona cualqier otro numero: ', 'yellow'))
def convertir_de_gms_a_g(grados,minutos,segundos):
	datos_pasados_a_g = float(grados) + float(minutos)/60 + float(segundos)/(60 * 60)
	return datos_pasados_a_g
def convertir_de_g_a_gms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]
def dibujar_triangulo():
	print """
			               B
			              /|
			             / |
			            /  |
			           /   |
			       c  /    |  a
			         /     |  
			        /      |
			       /       | 
			      /________|
			     A           C
			           b     
					"""

loop()










"""
def c_angle(tri):
	h = tri["h"] 
	x = tri["x"] 
	y = tri["y"]

	print tm.colored('\nOf what angle would you like to know the value?', 'green')
	print """
###	X'OA (1)
###	X'OB (2)
###	X'OC (3)
###	X'OD (4)	
"""
	c = input(tm.colored('You have to enter the number of the function you would like to get: ', 'green'))
	if c == 1:
		ang = "X'OA"
	if c == 2:
		ang = "X'OB"
	if c == 3:		
		ang = "X'OC"
	if c == 4:
		ang = "X'OD"
	print tm.colored('\nThe trigonometric functions of angle', 'blue'), tm.colored(ang ,'cyan'), tm.colored('are:\n', 'blue')
	a = x	
	o = y	
	
	triva = {"h":h,"o":o,"a":a,"ang":ang}
	return triva
"""
"""
	if py_h == True:
		h = round(m.hypot(x,y),1)
	if py_x == True:
		x = pyt_c(h,y)
	if py_y == True:	
		y = pyt_c(h,x)
"""

"""
	global datos = {a:0,b:0,c:0,A:0,B:0,C:0}

	for i in range(6):
		if i == 0:
			print tm.colored('\n\tIntroduce los datos de las partes conocidas del triangulo: \n', 'green')
		if i <= 2:
			try:
				a = float(input("Introduce el valor de la distancia a: "))	
			except SyntaxError:	
				print tm.colored('   No se conoce el valor de "a"!!!', 'red')
				py_a = True
"""

"""
def dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   seconds = round(seconds,2)
   return (degrees,minutes,seconds)


"""
"""	
def pyt_c(h,c):

	return round(m.sqrt(h*h-c*c),1)
"""




"""
		try:
			A = in_A.split(' ')
		except IndexError:
			try:
				print "hello"
				A.extend(["0"])
				A = in_A.split(' ')
				print "fi except"
			except IndexError:
				try:
					A.extend(["0"])
					A = in_A.split(' ')
					print "se except"
				except:
					print "Something went horribly wrong"
"""
"""
	h = triva["h"]
	a = triva["a"]
	o = triva["o"]
	sin = o/h
	print tm.colored('\tSin: ', 'blue'), tm.colored(round(sin,4), 'cyan')
	cos = a/h
	print tm.colored('\tCos: ', 'blue'), tm.colored(round(cos,4), 'cyan')
	tan = o/a
	print tm.colored('\tTan: ', 'blue'), tm.colored(round(tan,4), 'cyan')
	csc = h/o
	print tm.colored('\tCsc: ', 'blue'), tm.colored(round(csc,4), 'cyan')
	sec = h/a
	print tm.colored('\tSec: ', 'blue'), tm.colored(round(sec,4), 'cyan')
	cot = a/o
	print tm.colored('\tCot: ', 'blue'), tm.colored(round(cot,4), 'cyan')

	print tm.colored ('\nThe value of the angle in sine passed to degrees, minutes and seconds is: ','blue'),tm.colored(dms(round(m.degrees(m.asin(sin)),4)),'magenta')
"""