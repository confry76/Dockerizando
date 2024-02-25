
import random
import os

max_fallos = 3
lista=['casa','escoba', 'pluma','perro']

def generar_Aleatoria():
    palabra_Aleatoria=random.choice(lista)
    secreto='_'*len( palabra_Aleatoria)
    return palabra_Aleatoria, secreto

def remplazar_simbolo(original,secreto,simbolo):
    cantidad= original.count(simbolo)
    inicio=0
    for i in range(cantidad):
        pos=original.find(simbolo,inicio)
        secreto=secreto[:pos]+simbolo+secreto[pos+1:]
        inicio=pos+1
    return secreto

def ahorcado():
    print(f"Hola, vamos a jugar al juego del ahorcado. La palabra secreta sera una plabra de una de la lista de {len(lista)} palabras y tienes una oportunidad de fallar {max_fallos} veces")
    input("Presiona para comenzar...")
    os.system("cls")
    original, secreto=generar_Aleatoria()
    fallos=0
    while secreto != original and fallos < max_fallos:
        os.system("cls")
        print(f"palabra: ",{secreto})
        s=input("cual es la letra  que quieres destapar?")
        if s in original:
            secreto=remplazar_simbolo(original, secreto,s)
            print("La letra es correcta")
        else:
            print("Lo siento, letra equivocada")
            fallos+=1  
            print(f"Llevas en total de:  {fallos} fallos ")
        input("presiona enter para continuar...")
        os.system("cls")  
    if secreto==original:
        print(f"felicidades, la plabra es:",  {secreto})
    else:
        print(f"lo siento, la palabra era:", {original})  
    print("Nos vemos...") 

def main():
    ahorcado()
if  __name__=="__main__":
    main()
