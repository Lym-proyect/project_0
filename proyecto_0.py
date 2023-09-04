import ply.lex as lex
import re
import codecs
import sys
import os

tokens = ['JUMP', 'WALk', 'IDENTIFIER','DEFVAR']

def t_JUMP(t):
	r'JUMP'
	return t

def t_WALK(t):
	r'WALK'
	return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_defvar(t):
    r'defvar'
    return t

t_ignore = ' \t\n'

# Crear un analizador léxico
analizador_lexico = lex.lex()

# Ejemplo de uso del analizador léxico
entrada = "defvar my_variable"
analizador_lexico.input(entrada)

while True:
    token = analizador_lexico.token()
    if not token:
        break  # Se han analizado todos los tokens
    print(token)



















""" check = False
archivo = "ejemploFull.txt"
new_archive = "arreglo.txt"

full_tokens = []

reserved_non_terminal = {
    
    "variable": "defVar",
    "production" : "defProc",
    "JUMP": "JUMP",
    "WALK": "WALK",
    "leap": "leap",
    "turn": "turn",
    "turnto": "turnto",
    "drop": "drop",
    "get": "get",
    "grab": "grab",
    "letgo": "letGo",
    "nop": "nop",  
    "start": "{",
    "if" : "if",
    "else" : "else",
    "elif" : "elif",
    "can" : "can",
    "facing" : "facing",
    "not" : "not",
    "while" : "while",
    "repeat" : "repeat",
    "times" : "times",
    "start_parameter" : "(",
    "coma" : ",",  
}

reserved_terminal = {
    
    "end" : "}",
    "end_action" : ";",
    "end_parameter" : ")",
}

full_tokens = list(reserved_non_terminal.values()) + list(reserved_terminal.values())

def remove(name, archivo_salida):
        with open(name, "r") as entrada:
            lineas = entrada.readlines()
        with open(archivo_salida, "w") as salida:
            for linea in lineas:
                linea_sin_espacios = linea.replace(" ", "").replace("\n","").replace("\t","").lower()
                salida.write(linea_sin_espacios)
remove(archivo,new_archive)

with open(new_archive, 'r') as archivo:
    contenido = archivo.read()
 

#indicaciones

tokens = ['JUMP', 'WALk', 'IDENTIFIER','DEFVAR']

def t_JUMP(t):
	r'JUMP'
	return t

def t_WALK(t):
	r'WALK'
	return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_defvar(t):
    r'defvar'
    return t

t_ignore = ' \t\n'


def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)
 
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in full_tokens:
		t.value = t.value.upper()
		t.type = t.value
	return t 

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t 

analizador_lexico = lex.lex()
entrada = "defvar my_label"
analizador_lexico.input(entrada)

while True:
    token = analizador_lexico.token()
    if not token:
        break  # Se han analizado todos los tokens
    print(token)
 a = []
def analisis(contenido):
	analizador = lex.lex()
	analizador.input(contenido)
	a.clear()
	while True:
		tok = analizador.token()
		if not tok : break
		a.append(str(tok))
	return a

print(analisis(contenido))	
	 
	

def token(archivo):
    tokens = []
    for posicion in range(len(archivo)):
        for caracter in archivo:
            posicion += 1
            if caracter == "jump" and posicion:
                tokens.append("espacio")

def variable(cadena):
    pos = 0
    variable1 = ""
    for caracter in cadena:
        if pos >= 6 :
            variable1 += caracter
            if caracter == "d":
                break
        pos += 1
    variable1 = variable1.replace("d","")
    variable1 = variable1[:-1]
    return variable1

def variable2(cadena, variable1):
    pos = 0
    variable2 = ""
    tamaño = len(variable1) + 12
    for caracter in cadena:
        if pos > tamaño:
            variable2 += caracter
            if caracter == "d":
                break
        pos += 1
    variable2 = variable2.replace("d","")
    variable2 = variable2[:-1]
    return variable2

def variable3(cadena, variable1, variable2):
    pos = 0
    variable3 = ""
    tamaño = len(variable1) + len(variable2) + 19
    for caracter in cadena:
        if pos > tamaño:
            variable3 += caracter
            if caracter == "d":
                break
        pos += 1
    variable3 = variable3.replace("d","")
    variable3 = variable3[:-1]
    return variable3
            
def verificar(tokens: list): 
    
    if tokens.size() > 0:
        check = True
    
remove(archivo,new_archive)

