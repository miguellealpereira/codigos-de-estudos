import random 

numero = random.randrange(1, 100)
print("======adivinhe o numero que estou pensando entre 1 e 100======")
def adivinhanumero():
    while True:
        print("diga um numero de 1 a 100: ")
        chute = int(input())


        if abs(chute - numero) <= 5:
            print("quente")

        elif abs(chute - numero) <=15:
         print("morno")

        else:
            print("frio")      

        if chute == numero:
            print("parabens voce acertou o numero")
            break
    return True
        
adivinhanumero()
    
           

