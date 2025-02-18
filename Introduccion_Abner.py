# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

print("Ejercicio 1" "\n"
"Convertir Farenheit a Celsius")

Fahrenheit=float(input("Ingresa la temperatura en Fahrenheit: "))
Celsius=(Fahrenheit-32)*5/9
print("La temperatura en Celsius es: ",Celsius, "\n")###


print("Ejercicio 2" "\n"
"Evaluar senh (x) en x=2π"
"\n" "\n" "1.-Evaluar directamente")


import math as mt

x=float(input("Ingresa un valor para x: "))
resultado=mt.sinh(x)
print("Resultado: ",resultado)

print("\n" "2.-Evaluando con la definicion del lado derecho, usando la funcion exponencial:")
Definicion=(mt.e**x-mt.e**-x)/2
print("Resultado 2: ", Definicion, "\n" "\n")

print("3.-Con la definicion, usando la potencia.")
Potencia=(mt.exp(x)-mt.exp(-x))/2
print("Resultado 3: ", Potencia, "\n" "\n")


import cmath as cmt


print("Ejercicio 3" "\n" "1.Sen(ix)=iSenh(x)")

y=float(input("Ingrese valor de x: "))
q=mt.sinh(y)
print("senh (x)=",q)
r=1j*q
print("i*senh(x)=",r,)
s=cmt.sin(1j*y)
print("Sen(ix)=", s, "\n")

print("2.Relacion Euler para x real")
d=mt.cos(y)
e=1j*mt.sin(y)
print("Cos x + iSen x=",d+e)
f=mt.e**(1j*y)
print("e^ix=",f, "\n")


import numpy.lib.scimath as nls


print("Ejercicio 4" "\n" "Valor de las raices con valores de a,b,c dados.")
a=float(input("Ingresa un valor de a: "))
b=float(input("Ingresa un valor de b: "))
c=float(input("Ingresa un valor de c: "))
print("f(x)=",a,"x^2 +",b,"x+",c)
za=(-b+nls.sqrt(b**2-4*a*c))/(2*a)
zb=(-b-nls.sqrt(b**2-4*a*b))/(2*a)
print("x1=",za,"y x2=",zb)



