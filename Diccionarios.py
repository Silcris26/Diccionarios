# son cos este tipo de llaves {}



def ManeraAscendente(Diccionario:dict):
    Lista = []
    for val in Diccionario.values():
        Lista.append(val)
    Lista.sort()
    for i in Lista:
        print(i)

Diccionario1 = {"A":56,"B":3, "V":23, "G":20}
Diccionario2 = {"A":3,"B":23, "Z":10}
ManeraAscendente(Diccionario1)


def VerificarClaveValor(Diccionario:dict, Diccionario20:dict):
    s = 0
    for Val in Diccionario:
        if Val in Diccionario20:
            if Diccionario[Val] == Diccionario[Val]:
                s += 1
    else:
        if s == len(Diccionario):
            print(f"Todas las clave:valor esta en el diccionario 2")
        else:
            print(f"No todas las claves estan en el diccionario 2")

Diccionario1 = {"A":56,"B":3, "V":23, "G":20}
Diccionario2 = {"A":3,"B":23, "Z":10}

VerificarClaveValor(Diccionario1, Diccionario2)

def DiccionarioNuevo(Diccionario:dict, Diccionario20:dict):
    dicMezclado = {}
    for Key in Diccionario:
        if Key in Diccionario20:
            Diccionario20[Key] = Diccionario[Key]
    dicMezclado.update(Diccionario)
    dicMezclado.update(Diccionario20)
    print(dicMezclado)

Diccionario1 = {"A":56,"B":3, "V":23, "G":20}
Diccionario2 = {"A":3,"B":23, "Z":10}

DiccionarioNuevo(Diccionario1, Diccionario2)
    
def PrintNombresApellidos(diccionarioNombres:dict, diccioanrioApellidos:dict, diccinarioEdades:dict):
    ListaNombres = list(diccionarioNombres.values())
    ListaApellidos = list(diccioanrioApellidos.values())
    ListaEdades = list(diccinarioEdades.values())
    if len(diccinarioEdades) == len(diccionarioNombres) == len(diccioanrioApellidos):
        for i in range(len(ListaEdades)):
            if ListaEdades[i] >= 18:
                print(f"{ListaNombres[i]} {ListaApellidos[i]} cumple con los requerimientos de edad")

Nombres = {"Nombre1": "Cristian", "Nombre3":"Andres", "Nombre2":"Daniel"}
Apellidos = {"Apellido1":"Silva", "Apellido3":"Perez", "Apellido2":"Hernandez"}
edad = {"edad1":11,"edad3":20, "edad2":22}

PrintNombresApellidos(Nombres, Apellidos, edad)