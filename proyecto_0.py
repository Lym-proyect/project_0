import re
import codecs
import sys
import os

check = False
name = "ejemploFull.txt"
archive = open(name, "r")

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

def values(token):
    variable = r"[a-zA-Z_][a-zA-Z0-9]*"
    return variable

def remove(archive: list):
    
    for caracter in archive:
        
        if caracter == "\n":
            archive.remove(caracter)
            
        if caracter == "\t":
            archive.remove(caracter)
        
        if caracter == " ":
            archive.remove(caracter)
    
    print(archive)

def token(archivo):
    archivo = remove(archivo)
    tokens = []
    for posicion in range(len(archivo)):
        for caracter in archivo:
            posicion += 1
            if caracter == "jump" and posicion:
                tokens.append("espacio")
            
        
def verificar(tokens: list):
    
    if tokens.size() > 0:
        check = True
    
    print(check)  
    