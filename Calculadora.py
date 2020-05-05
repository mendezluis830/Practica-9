#dejar espacios

def sumar (a, b):
    c = a + b
    return c

def restar (a , b):
    return a-b

def multiplicacion (a , b):
    return a*b

def divicion_entera(a,b):
    if b==0:
        print ("no se puede , division sobre cero ")
        return
    return a//b

def division (a,b):
    if b == 0:
        print(" no se puede divsion sobre cero ")
        return
    return a/b   

def modulo (a, b):
    if b== 0:
        print("no se puede division sobre cero ")
        return
    return a%b

def potencia (a, b):
    return a**b

def main():
    print ("ingresa dos valores ")
    x = int (input())
    y= int (input())

    print (" 1.Sumar \n 2.Restar \n 3.Division entera ")
    print ("4.Division \n 5.Modulo \n 6.Potencia \n 7.Multiplicar")
    op = int(input())
    

    if op == 1:
        print (sumar (x,y))
    elif op ==2:
        print (restar (x,y))
    elif op== 3:
        print ( divicion_entera (x ,y))
    elif op== 4:
        print (division (x , y)) 
    elif op == 5:
        print (modulo (x, y))
    elif op == 6:
        print (potencia (x , y))
    elif op == 7:
        print (multiplicacion (x, y))
    else :
        print  ("opcion no valida ")

if __name__ == "__main__":
    main ()
