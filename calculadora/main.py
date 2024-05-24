from funciones_matematicas import *
import os

seguir = "s"

flag_primer_operando = False
flag_segundo_operando = False

flag_calculos = False



while(seguir == "s"):
    os.system("cls")

    match menu_calculadora():
        case "1":
            a = int(input("Ingrese el primer operando: "))
            flag_primer_operando = True
        case "2":
            b = int(input("Ingrese el segundo operando: "))
            flag_segundo_operando = True
        case "3":
            if flag_primer_operando and flag_segundo_operando:
                os.system("cls")

                suma = sumar(a, b)

                resta = restar(a, b)

                division = dividir(a, b)

                multiplicación = multiplicar(a, b)

                factorial_a = factorial(a)
                
                factorial_b = factorial(b)

                if a == 0 or b == 0:
                    division = print("No es posible dividir por cero")
                else:
                    division = dividir(a, b)   

                flag_calculos = True
                print("Las operaciones han sido calculadas...") 
            elif flag_primer_operando == False:
                print("Para calcular primero debes ingresar el primer operando.")
            else:
                print("Para calcular primero debes ingresar el segundo operando.")
        case "4":
            if flag_primer_operando and flag_segundo_operando:
                if flag_calculos:
                    os.system("cls")
                    match sub_menu_informar(a,b):
                    
                        case "A":
                            
                            print(f"El resultado de la suma entre {a} y {b} es: {suma}")
                        case "B":
                            print(f"El resultado de la resta entre {a} y {b} es: {resta}")
                        case "C":
                            print(f"El resultado de la division entre {a} y {b} es: {division}")
                        case "D":
                            print(f"El resultado de la multiplicacion entre {a} y {b} es: {multiplicación}")
                        case "E":
                            print(f"El resultado del factorial de {a} es:{factorial_a} y el de {b} es:{factorial_b} ")
                else:
                    print("Para informar los datos primero deben ser calculados")
            elif flag_primer_operando == False:
                print("Para calcular primero debes ingresar el primer operando.")
            else:
                print("Para calcular primero debes ingresar el segundo operando.")
        case "5":
            seguir = input("desea continuar?(s/para continuar n/para salir del programa): ")
    
    os.system("pause")
