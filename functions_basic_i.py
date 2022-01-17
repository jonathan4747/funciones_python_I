#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#retorna y se imprime el valor de 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# error debido a que la funcion number_of_days_in_a_week_silicon_or_triangle_sides no esta definido

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#retona y se imprime el valor de 5 por ser el primero

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# retorna y se imprime el valor de 5, debido que el print esta despues del return

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# se imprime 5 porque la funcion manda ello, pero print(x) no existe por que no la funcion no tiene valor de retorno

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# error debido a que la funcion no tiene variable de retorno entonces el ultimo print no tiene valores de suma

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# nos da la cadena 25 debido a que se cincatena el 2 y el 5, y ello sale en la variable de retorno

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""imprme el valor de b (100) y nos da la variable de retorno que es 10 y lo imprime, debido a que b siempre es mayor que 10 
 y es el valor que cumple la condicion y retorna"""

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))#retorna y se imprime 7 debido, debido a que es la cumple la condicion
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#retorna y se imprime 14, debido a que b > c
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imrprime 21 debido a que se suma las variables de retorno 7 y 14 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# retorna 8; debido a que es el primer return , la cual es la sumatoria de b y c

#11
b = 500
print(b)#imprime 500
def foobar():
    b = 300
    print(b)
print(b)#imprime 500
foobar()#imprime 300
print(b)#imprime 500
# imprime 3 veces 500 por que no se manda la ejecucion de la funcion y despues se imprime 1 vez 300. ya que se llamo a la funcion 

#12
b = 500
print(b) # imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b)#imprime 500
foobar()#imprime 300
print(b)#imprime 500
#imprime 3 veces 500 por que no se manda la ejecucion de la funcion y despues se imprime 1 vez 300. ya que se llamo a la funcion 

#13
b = 500
print(b)#imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b)#imprime 500
b=foobar()
print(b)#imprime 300
#imrprime 500 por que todavia no se llama la funcion, despues se imprime 2 veces 300 por que se llama a la funcion y su retorno 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo() #1 3 2
# se llama a la funcion foo y se imprime 1 , depues la funcion bar se activa y se imprime 3 y por ultimo en la funcion foo se imprime 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)# 1 3 5 10
""" se llama a la funcion foo, este imprime 1, y pasa a x, la cual llama a la funcion bar,por eso se imprime 3 y retorna
5 y se imprime, y por ultimo retorna 10 que es igual a y, por lo cual se imprime"""