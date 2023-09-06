import ply.lex as lex
import re
import codecs
import sys
import os


tokens = ['JUMP', 'WALK','DEFVAR','DEFPROC','LEAP','TURN','DROP','TURNTO','GET','GRAB','LETGO','NOP','IF','FACING','CAN','NOT','OBRACKET', "ELSE", "SEMICOLON", "ELIF", "WHILE", "REPEAT", "TIMES", "COMA", "EBRECKET"]

def t_JUMP(t):
	r'jump\s*\(\s*(.*?)\s*\)'
	return t

def t_LEAP(t):
	r'leap\s*\(\s*(.*?)\s*\)'
	return t

def t_TURN(t):
	r'turn\s*\(\s*(.*?)\s*\)'
	return t

def t_WALK(t):
	r'walk\s*\(\s*(.*?)\s*\)'
	return t

def t_DROP(t):
	r'drop\s*\(\s*(.*?)\s*\)'
	return t

def t_DEFVAR(t):
    r'defvar\s+([a-zA-Z0-9_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_][a-zA-Z0-9_]*)'
    return t

def t_DEFPROC(t):
    r'defproc\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*(.*?)\s*\)'    
    return t

def t_TURNTO(t):
	r'turnto\s*\(\s*(.*?)\s*\)'
	return t
def t_GET(t):
	r'get\s*\(\s*(.*?)\s*\)'
	return t
def t_GRAB(t):
	r'grab\s*\(\s*(.*?)\s*\)'
	return t
def t_LETGO(t):
	r'letgo\s*\(\s*(.*?)\s*\)'
	return t

def t_NOP(t):
	r'nop\s*\(\)'
	return t

def t_FACING(t):
	r'facing\s*\(\s*(.*?)\s*\)'
	return t

def t_CAN(t):
	r'can\s*\(\s*(.*?)\s*\)'
	return t

def t_NOT(t):
	r'not'
	return t

def t_IF(t):
	r'if+t_NOT|t_CAN|t_FACING+\('
	return t

def t_OBRACKET(t):
	r'\{'
	return t

def t_ELSE(t):
    r"'\belse\b'"
    return t

def t_SEMICOLON(t):
    r"'\;'"
    return t

def t_ELIF(t):
    r"'\belif\b'"
    return t    

def t_WHILE(t):
    r"'\bwhile\b'"
    return t

def t_REPEAT(t):
    r"'\brepeat\b'"
    return t

def t_TIMES(t):
    r"'\btimes\b'"
    return t

def t_COMA(t):
    r"'\,'"
    return t

def t_EBRACKET(t):
    r'\}'
    return t 

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)


analizador_lexico = lex.lex()

working = True

while working:
    print("\nBienvenido al analizador léxico de nuestro lenguaje de programación ")
    print("\n1. Usar analizador léxico")
    print("2. Salir")
    opcion = input("\nIngrese una opción: ")
    
    if int(opcion) == 1:
        archivo = input("Ingrese el nombre del archivo txt: ")
        entrada = open(archivo, "r")
        cadena = entrada.read().lower()
        analizador_lexico.input(cadena)
        while True:
            token = analizador_lexico.token()
            if not token:
                break  
            print(token)
        
    elif int(opcion) == 2:
        working = False
        print("\nGracias por utilizar el programa")

 

