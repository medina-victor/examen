import random
import math


trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel",
 "Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


def calcular_promedio():
    return sum(sueldos.values()) / len(sueldos)

#sueldo mas alto
def encontrar_sueldo_mas_alto():
    return max(sueldos.values())

#bajo
def encontrar_sueldo_mas_bajo():
    return min(sueldos.values())

#md geo
def calcular_media_geometrica():
    producto = 1
    for sueldo in sueldos.values():
        producto *= sueldo
    return producto ** (1 / len(sueldos))
sueldos = {}
#calsi sueldos x rango
def clasificar_sueldos():
    clasificacion = {
        ">= 2000.000": [],
        "< 2000.000 y >= 800.000": [],
        "< 800.000": []
}

    for trabajador, sueldo in sueldos.items():
        if sueldo >= 2000.000:
            clasificacion[">= $2.000.000"].append(trabajador)
        elif sueldo >= 800.000:
            clasificacion["<$2.000.000 y >= 800.000"].append(trabajador)
        else:
            clasificacion["< $800.000"].append(trabajador)
    return clasificacion       
    
def asignar_sueldos():
    global sueldos
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = round(random.uniform(300.000, 2500.000), 1)
        sueldos[trabajador] = sueldo

def calcular_7_por_ciento():
    porcentaje_7 = {}
    for trabajador, sueldo in sueldos.items():
        porcentaje_7[trabajador] = sueldo * 0.07
    return porcentaje_7

def calcular_12_por_ciento():
    porcentaje_12 = {}
    for trabajador, sueldo in sueldos.items():
        porcentaje_12[trabajador] = sueldo * 0.12
    return porcentaje_12



def mostrar_menu():
    while True:
        print("-------------------------------------------")
        print("menu:")                             
        print("1. Asignar sueldos aleatorios")     
        print("2. Clasificar sueldos")             
        print("3. ver estadistica")               
        print("4. reporte de sueldo")             
        print("5. salir del programa")             

        print("-------------------------------------------")
        
        opcion = input("seleccione un opcion: ")

        if opcion == "1":
            asignar_sueldos()
            print("sueldos asignados aleatoriamente")
        
        elif opcion == "2":
            
            if not sueldos:
                print("primero debe asignar sueldos")
        else:
            clasificacion = clasificar_sueldos()
            print("clasificacion de sueldos:")
            for categoria, estudiantes in  clasificacion.items():

                print(f"trabajadores con promedio {categoria}:: {', '.join(trabajadores)}")

        if opcion == "3":
         
         promedio = calcular_promedio()
         sueldo_alto = encontrar_sueldo_mas_alto()
         sueldo_bajo = encontrar_sueldo_mas_bajo()
         media_geom = calcular_media_geometrica()
         print("\nEstadísticas:")
         print(f"Promedio de notas: {promedio:.2f}")
         print(f"sueldo mas alto: {sueldo_alto}")
         print(f"sueldo mas bajo: {sueldo_bajo}")
         print(f"Media geometrica de los suedos: {media_geom:.2f}")
        if opcion == "4":
                
            porcentaje_7 = calcular_7_por_ciento()
            print("Reporte decuento de salud - 7% de sueldo de cada trajador:")
            for trabajador , porcentaje in porcentaje_7.items():
                print(f"{trabajador}: {porcentaje:.2f}")

            porcentaje_12 = calcular_12_por_ciento()
            print("Reporte descuento afp - 12% de sueldo de cada trajador:")
            for trabajador , porcentaje in porcentaje_12.items():
                print(f"{trabajador}: {porcentaje:.2f}")
        elif opcion == "5":
            print("saliendo del progama")
            print("victor medina")
            print("rut 21654221-5")
            break
        else:print("opcion invalida")
mostrar_menu()



    
