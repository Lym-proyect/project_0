import ply.lex as lex
import re
import codecs
import sys
import os

tokens = ['JUMP', 'WALk','DEFVAR','DEFPROC']

def t_JUMP(t):
	r'jump\s*\(\s*(.*?)\s*\)'
	return t

def t_WALK(t):
	r'WALK'
	return t

def t_DEFVAR(t):
    r'defvar\s+([a-zA-Z_][a-zA-Z]*)\s+([a-zA-Z0-9_]+)'
    return t

def t_DEFPROC(t):
    r'defproc\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\)\s*{([^}]*)}'    
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

analizador_lexico = lex.lex()


entrada = "jump (r,t)"
analizador_lexico.input(entrada)

while True:
    token = analizador_lexico.token()
    if not token:
        break  
    print(token)



