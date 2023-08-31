
check = False
archivo = open("archivo.txt", "r")

def remove(archivo: list):
    
    nuevo_archivo = []
    
    for caracter in archivo:
        
        if caracter == "\n":
            archivo.remove(caracter)
            
        elif caracter == "\t":
            archivo.remove(caracter)
        
        minuscula = caracter.lower()
        nuevo_archivo.append(minuscula)
    
    return archivo

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
    