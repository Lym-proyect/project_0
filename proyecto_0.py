import re
import codecs
import sys
import os

check = False
archivo = "ejemploFull.txt"
new_archive = "arreglo.txt"

full_tokens = []

reserved_non_terminal = {
    
    "variable": "defVar",
    "jump": "jump",
    "walk": "walk",
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
    "production" : "defProc",
    
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
                linea_sin_espacios = linea.replace(" ", "").replace("\n","").replace("\t","")
                salida.write(linea_sin_espacios)

def values(token):
    variable = r"[a-zA-Z_][a-zA-Z0-9]*"
    return variable

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
arreglo = open(new_archive, "r")
cadena = arreglo.read()
arreglo.close()
variable_1 = variable(cadena)
variable_2= variable2(cadena,variable_1)
variable_3 = variable3(cadena, variable_1, variable_2)

