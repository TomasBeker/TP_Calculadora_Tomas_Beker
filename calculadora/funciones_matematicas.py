def menu_calculadora()->str:
    """Menu principal del programa.

    Returns:
        str: retorna la opcion elegida.
    """    
    print(f"{'Menu de opciones':^50s}")
    print("1- Ingresar primer operando")
    print("2- Ingresar segundo operando")
    print("3- Calcular todas las operaciones")
    print("4- Informar resultados")
    print("5- Salir")
    
    return input("Ingrese una opcion: ")


def sub_menu_informar(primer_operando:float, segundo_operando:float)->str:
    """Menu de opciones para informar el resultado de los calculos previamente hechos.

    Args:
        primer_operando (float): numero a calcular.
        segundo_operando (float): numero a calcular.

    Returns:
        str: Retorna la opcion elegida.
    """    

    print(f"{'Resultados de los Calculos ':50s}")    
    print(f"A- Resultado de la suma")
    print(f"B- Resultado de la resta")
    print(f"C- Resultado de la division")
    print(f"D- Resultado de la multiplicacion")
    print(f"E- Resultado del factorial de {primer_operando} y el de {segundo_operando}")

    entrada = input("Ingrese una opcion: ")

    return entrada.upper()

def sumar(primer_operando:float, segundo_operando:float)-> float:
    """Funcion hecha para sumar 2 numeros

    Args:
        primer_operando (float): numero a sumar.
        segundo_operando (float): numero a sumar.

    Returns:
        float: retorna la suma
    """    

    return primer_operando + segundo_operando

def restar(primer_operando:float, segundo_operando:float)-> float:
    """Funcion hecha para restar 2 numeros

    Args:
        primer_operando (float): numero a restar.
        segundo_operando (float): numero a restar.

    Returns:
        float: retorna la resta
    """
    return primer_operando - segundo_operando

def dividir(primer_operando:float, segundo_operando:float)-> float:
    """Funcion hecha para dividir 2 numeros

    Args:
        primer_operando (float): numero dividendo.
        segundo_operando (float): numero divisor.

    Returns:
        float: retorna la division 
    """
    return primer_operando / segundo_operando

def multiplicar(primer_operando:float, segundo_operando:float)-> float:
    """Funcion hecha para multiplicar 2 numeros

    Args:
        primer_operando (float): numero a multiplicar.
        segundo_operando (float): numero a multiplicar.

    Returns:
        float: retorna la multiplicacion
    """
    return primer_operando * segundo_operando

def factorial(numero:int)->int:
    """Funcion que busca el Factorial de un numero.

    Args:
        numero (int): Numero del cual se busca su factorial.

    Returns:
        int: Retorna el factorial.
    """    
    fact = None
    if numero == 0 or numero == 1:
        fact = 1
    else:
        fact = numero * factorial(numero - 1)

    return fact

    
