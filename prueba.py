import ply.lex as lex
import re
import codecs
import sys
import os

name = "ejemploFull.txt"

tokens = ['JUMP', 'WALK','DEFVAR','DEFPROC','LEAP','TURN','DROP','TURNTO','GET','GRAB','LETGO','NOP','IF','FACING','CAN','NOT','OBRACKET']

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

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

analizador_lexico = lex.lex()
entrada = open(name, "r")
cadena = entrada.read().lower()

analizador_lexico.input(cadena)

while True:
    token = analizador_lexico.token()
    if not token:
        break  
    print(token)

 

