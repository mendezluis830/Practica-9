#Comentario de una linea
"""
Comentario de varias 
lineas 
"""
print("Hola Mundo")

#sin punto y coma 
#Es print no printf 
#no se declaran varibales 
x = 10
print(type(x))

x = y = z = 2.3

print( x, y, z)
print(type(x))

#no se compila , leguaje intrepretado 

z = x + y
print ( z )

x = "cadena"
print(type(x))

c1="Hola"
c2 ="Adrian Farid "
saludo = c1 + " " +c2
#cocadenar cadena 
print(saludo)

#cocadenar 2
saludo2 =" {} {} {} ".format(c1 , c2 , 3)
#cada llave puede ir un valor 
print(saludo2)

saludo3 = "cambio de orde {1} {2} {0}".format(c1, c2 ,3)
print(saludo3)


