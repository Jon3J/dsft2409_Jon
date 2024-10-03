biblioteca = [{},{},{}] #--> Variable global

def funcion_prueba_1():
    global biblioteca
    a = 1
    b = 2 #variables locales
    c = 3
    print(a,b,c)
    print(biblioteca)
    
def funcion_prueba_2():
    funcion_prueba_3()
    
def funcion_prueba_3():
    print("hola")

biblioteca = [{},{},{}]
funcion_prueba_1()
funcion_prueba_2()
