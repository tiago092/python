# La lista de alumnos que habíamos creado en el módulo
# anterior ahora debe ser un diccionario, en donde las claves
# serán nombres de alumnos y los valores sus respectivas
# cantidades de cursos.
# Para esto deberemos modificar el código de las opciones 1
# y 2 (agregar un nuevo alumno y ver la lista de alumnos).
# La tercera opción será “Ver la cantidad de cursos de un
# alumno”. Deberá solicitar el nombre de un alumno e
# imprimir en pantalla el número de cursos que tiene
# asociados como clave.
# La cuarta opción es la de salir, como en la versión anterior.

def verentero(num):
    while num.isdecimal() == False:
        print('Error')
        num = input('Ingrese un número válido: ')
    return int(num)

def vertexto(texto):
    while texto == '':
        print('Error')
        texto = input('Debe ingresar texto: ')
    return texto

def mostrar_todos():
    print('Lista de alumnos: \n')
    for n in personas:
        print(f'{n} ----- {personas[n]} cursos')

def agregar_alumno():
    new_alu = input('Ingrese el nombre del alumno: ')
    new_alu = vertexto(new_alu)
    c = input('Ingrese la cantidad de cursos: ')
    c = verentero(c)
    personas[new_alu] = c
    print('¡El alumno fue añadido a la lista! \n')

def ver_alumno():
    alu = input('Ingrese el nombre del alumno: ')
    alu = vertexto(alu)
    if alu in personas:
        print(f'{alu} tiene {personas[alu]} cursos.')
    else:
        print('Alumno no encontrado')

#####################################

personas = {}

while True:
    num = input('Ingrese el número de la operación que desea ejecutar: \n \
        1 - Ver la lista de alumnos. \n \
        2 - Añadir un alumno a la lista. \n \
        3 - Ver cursos de un alumno\n \
        4 - Salir. \n')
     
    # Opción 1 Ver lista de alumnos
    if num == '1':
        mostrar_todos()

    # Opción 2 Agregar un nuevo alumno
    elif num == '2':
        agregar_alumno()

    # Opción 3 Ver la cantidad de cursos de un alumno    
    elif num == '3':
        ver_alumno()

    # Opción 4 Salir
    elif num == '4':
        break

    else:
        print('Error de opción')

