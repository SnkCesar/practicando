"""
---------
Desafío 1
---------
    150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

    Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

    Un trozo de chicle tarda 5 años en degradarse. 

    Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.
"""
def anios_degradacion(material):
    if material == 1:
        return 150
    elif material == 2:
        return 1000
    elif material == 3:
        return 30
    elif material == 4:
        return 5



titulo = "SALVEMOS EL PLANETA"

def opciones_materiales():
    print("=" * len(titulo))
    print(titulo)
    print("=" * len(titulo) + "\n")
    print("ingrese el material a continuación: " + "\n")
    print("0: SALIR")
    print("1: Bolsa de plástico")
    print("2: Botella PET")
    print("3: Envase tetrabrik")
    print("4: Chicle")
    print("====================" + "\n")
    return input()

salio = False
es_valido = False
while not es_valido and not salio:
    opcion = opciones_materiales()
    if not opcion.isdigit():
        opcion = opciones_materiales()
        continue
    opcion = int(opcion)
    if opcion == 0:
        salio = True
    elif opcion >= 5:
        continue
    else:
        es_valido = True

if es_valido and not salio:
    anios = anios_degradacion(opcion)

    print("El material selecionado demora %s años en degradarse." % (anios) + "\n")
