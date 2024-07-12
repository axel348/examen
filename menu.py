from  random import randrange
import csv 

def generar_sueldos(lista):
    for i in range(10):
        nom= 'empleado'+ str(i+1)
        sueldo = randrange(500000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

def menu():
    menu= """menu de sueldos

    ------------------------
    [1].mostrar sueldos asignados 
    [2].calificar sueldos 
    [3].ver estadisticas de sueldo 
    [4].exportar sueldos"
    [5].salir 

    """
    print(menu, end="")

def validar_op():
    while True:
        try:
            op= int(input())
            if op >=1 and op <=4:
                return op
            else:
                raise ValueError
        except:
            print("seleccione una opcion valida, -->", end="") 

def clasificar_empleados(lista):
    bajos=[]
    medios=[]
    altos=[]
    for trabajador in lista:
        if trabajador["sueldo"]<=800000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]<=2000000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)
    print("empleados con sueldo menos a $800.000: ")
    print()

    for i in bajos:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
        print("****************")
   

    print("empleados con sueldo entre $800.000 y 2.000.000")
    print()

    for i in medios:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
        print("***********************")
    for i in altos:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")

def sueldo_bajo(lista):
    bajo=lista[0]
    for empleado in lista:
        if bajo["sueldo"] >empleado["sueldo"]:
            bajo=empleado
    return bajo

def sueldo_alto(lista):
    alto=lista[0]
    for empleado in lista:
        if alto["sueldo"] >empleado["sueldo"]:
            alto=empleado
    return alto

def imprimir_estadisticas(lista):
    print(f"sueldo mas bajo: {sueldo_bajo(lista)}")
    print(f"sueldo mas alto: {sueldo_alto(lista)}")
    listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
    suma=sum(listar_sueldos)
    promedio = sum/10
    print(f"sueldo promedio: {promedio:,.0f}")

def reporte_sueldos(lista):
    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto *0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        a = {"nombre":trabajador["nombre"],"sueldo_bruto":sueldo_bruto,"afp":afp,"salud":salud,"sueldo_liquido":sueldo_liquido}
        reporte.append(a)

nombre_campo = ["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
with open ['reporte Sueldo.csv','w'," "] as archivo:
    escritor = csv.DictReader(archivo,fieldname=nombre_campo)
    escritor.writeheader()
    escritor.writerows(reporte_sueldos)