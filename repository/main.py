info=[
    'Lucas',
    'Martha',
    'Pedro',
    'Alicia',
    'Carmen',
    'Alberto'
]
#abrir y escribir fichero
def escribirFichero(fichero,datos_a_rellenar):
    f=open(fichero,'w')
    for i in datos_a_rellenar:
        f.write(i+"\n")
    f.close()
#leer fichero y mostrar los datos
def leerFichero(fichero):
    f=open(fichero,'r')
    datos='s'
    while len(datos) > 0:
        datos=f.readline()
        print(datos)
    f.close()

escribirFichero('datos.txt',info)
leerFichero('datos.txt')
