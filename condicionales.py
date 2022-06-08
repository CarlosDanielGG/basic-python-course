#Declaramos una variable
calificacion  = input("Introduce la calificacio de la AZ-900: ")
calificacion = int(calificacion)

#Condicional
if calificacion < 700 :
    print("Ves?, Por no estudiar baboso") #indentación es un espacio que indica que el codigo pertenece al if es como las llaves {}
elif calificacion == 700 :
    print("De Panzaso canijo")
elif calificacion > 1000:
    print("Mientes, me haces daño y luego te arrepientes")    
else:
    print("Felicidades eres un crack")


edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <=115:
    print("Bienvenido al mamitas")
elif edad > 100:
    print("Si vienes acompañado de tus abuelitos si te podemos fiaar")
elif edad < 0:
    print("Ni que fueras viajero del tiempo")
else:
    print("No puedes ingresar, eres menor")

#En python no tienes switch case, es a puro elif