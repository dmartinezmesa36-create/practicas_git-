from funtions import suma
from calculos import calclar_area_c,calcular_area_t,area_circilo




#programa
print("hola mundo")
resultado= suma(5,10)
print(resultado)





def mostrar_menu():
     
     
     while True:
    
            print("\n--- MENÚ DE ÁREAS ---")
            print("(1) Área de un triángulo")
            print("(2) Área de un cuadrado")
            print("(3) suma")
            print("(4) area del un circilo")
            print("(5) Salir")
 
            opcion = input("Selecciona una opción (1 al 4): ")


            if opcion == "1":
                    base = float(input("Ingresa la base del triángulo: "))
                    altura = float(input("Ingresa la altura del triángulo: "))
                    print("Área del triángulo:", calcular_area_t(base, altura))

            elif opcion == "2":
                    lado = float(input("Ingresa el lado del cuadrado: "))
                    print("Área del cuadrado:", calclar_area_c(lado))
                
            elif opcion == "3":
                    a = float(input("el nuemro a sumar: "))
                    b = float(input("el otro numero a sumar"))
                    print("Área del cuadrado:", suma(a,b))
            elif opcion == "4":
                   r= float (input("ingrese el radido"))
                   print("el area del ciculo es: ",area_circilo(r))
                
            if opcion == "5":
                    print("¡Hasta luego!")
                    break

            else:
                print("Opción no válida. Intenta de nuevo.")
mostrar_menu()
