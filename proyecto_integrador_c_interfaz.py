import tkinter as tk
from tkinter.constants import X


def verentero(num):
    if num.isdecimal():
        num = int(num)
    else:
        num = 'error'
    return num

def vertexto(texto):
    if texto == '':
        texto = 'error'
    return texto

def mostrar_todos():
    print('Lista de alumnos: \n')
    for n in personas:
        print(f'{n} ----- {personas[n]} cursos')

def agregar_alumno():
    new_alu = caja_alu.get()
    new_alu = vertexto(new_alu)
    c = caja_cur.get()
    c = verentero(c)
    if new_alu == 'error':
        print('El nombre no es válido')
    elif c == 'error':
        print('El número de cursos no es válido')
    else:
        personas[new_alu] = c
        print('¡El alumno fue añadido a la lista! \n')

def ver_alumno():
    alu = caja_alu.get()
    alu = vertexto(alu)
    if alu in personas:
        print(f'{alu} tiene {personas[alu]} cursos.')
    else:
        print('Alumno no encontrado')

#####################################

personas = {}

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title('Alumnos')

# Botón de ver alumnos:
boton = tk.Button(text='Ver lista de alumnos', command=mostrar_todos)
boton.place(x=20, y=20, width=130, height=30)

# Ingresar alumno:
caja_alu = tk.Entry()
caja_alu.place(x=120, y=60, width=200, height=25)

etiqueta_alu = tk.Label(text='Ingrese nombre:')
etiqueta_alu.place(x=20, y=60)

# Ingresar cantidad de cursos:
caja_cur = tk.Entry()
caja_cur.place(x=120, y=100, width=50, height=25)

etiqueta_cur = tk.Label(text='Cursos:')
etiqueta_cur.place(x=20, y=100)

# Botón agregar a lista:
boton = tk.Button(text='Agregar a la lista', command=agregar_alumno)
boton.place(x=20, y=150, width=130, height=30)

# Botón de ver cantidad de cursos:
boton = tk.Button(text='Ver cantidad de cursos', command=ver_alumno)
boton.place(x=160, y=150, width=130, height=30)

ventana.mainloop()