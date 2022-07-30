import re

nomina=[]

def CheckLetters(Input):
    pattern = re.compile('[a-zA-Z]+')
    pattern.fullmatch(Input)
    if pattern.fullmatch(Input) is not None: 
        return False
    else:
        print("Ingrese solo letras ")
        return True 

def CheckNumbers(input):
    pattern = re.compile('[0-9]+')
    pattern.fullmatch(input)
    if pattern.fullmatch(input) is not None: 
        return False
    else:
        print("Ingrese solo numeros ")
        return True 

print("BIENVENIDO ")
inicio = input("Desea agregar empleados a la nomina? s/n ")
while (inicio == 's'):
    x = True
    while x: 
        cedula = input("ingrese el numero de su cedula: ")
        if CheckNumbers(cedula):
            x = True
        else:
            x = False
            nomina.append(cedula)

    a = True
    while a:
        nombre = input("ingrese su nombre: ")
        if CheckLetters(nombre):
            a = True
        else:
            a = False
            nomina.append(nombre)

    b = True
    while b:
        apellido = input("ingrese sus apellidos: ")
        if CheckLetters(apellido):
            b = True
        else:
            b = False
            nomina.append(apellido)

    c = True
    while c: 
        dias = input("ingrese el numero de dias laborados: ")
        if CheckNumbers(dias):
            c = True
        else:
            c = False
            nomina.append(dias)

    e = True
    while e: 
        horas = input("ingrese el numero de horas extra laboradas: ")
        if CheckNumbers(horas):
            e = True
        else:
            e = False
            nomina.append(horas)
    
    d = True
    while d: 
        salario = input("ingrese su salario: ")
        if CheckNumbers(salario):
            d = True
        else:
            d = False
            nomina.append(salario)
    
    print("-------------------------------------------------------------------------------------------------------------------")

    if (float(salario)) <= 2000000:
        subsidioTransporte=(117172/30)*(float(dias))
    else:
        subsidioTransporte=0
    ValorDia=(float(salario)/30)
    TotalSalario=subsidioTransporte+(ValorDia*float(dias))+(((ValorDia/8)*(float(horas))))
    salud=TotalSalario*0.04
    pension=TotalSalario*0.04
    sindicato=TotalSalario*0.02
    deduccion=salud+pension+sindicato
    devengado=TotalSalario-deduccion

    print("El devengado fue de: ", devengado)
    print("El subsidio de Transporte fue de: ", subsidioTransporte)
    print("El total de su salario sin deducciones fue de: ", TotalSalario)
    print("las deducciones por Salud, Pension y Sindicato fueron respectivamente: ", salud, pension, sindicato)
    nomina.append(TotalSalario)
    nomina.append(deduccion)
    nomina.append(devengado)

    inicio = input("Desea realizar otra liquidacion? s/n ")

print("Gracias")

file = open("EjercicioNomina.txt", "w")
file.write('\n')
file.write('nomina=%s'%nomina)

file.close()