#Import para crear la app
from tkinter import Label, Frame, Tk, Canvas, Entry, Button, W, E, Listbox, END
#Import driver de conexión para postgresql
import psycopg2

#Se crea la pantalla emergente
root = Tk()
root.title("Python y PostgreSQL")

#Se crea la función para guardar el estudiante en la base de datos
def guardaEstudiante(name, age, address):
    #Se ingresan credenciales
    connection= psycopg2.connect(dbname="daads17to2qqm5",
                     user="dstunsoypdpdpn",
                     password="cbb5e68b3caffdb4b5dcfb015ea18957192c8c55560188602e666ddf3e881705",
                     host="ec2-34-230-153-41.compute-1.amazonaws.com",
                     port="5432")
    #Se crea el cursor y la query para insertar el nuevo estudiante
    cursor= connection.cursor()
    query = '''INSERT INTO students(name, age, address) VALUES(%s, %s, %s)'''
    cursor.execute(query, (name, age, address))
    #Se muestra que los datos han sido guardados
    print("Datos guardados")
    #Se termina la conexión a la base de datos
    connection.commit()
    connection.close()
    
#Se crea la función para ver todos los estudiantes guardados
def visualizaEstudiante():
    #Se ingresan credenciales
    connection= psycopg2.connect(dbname="daads17to2qqm5",
                     user="dstunsoypdpdpn",
                     password="cbb5e68b3caffdb4b5dcfb015ea18957192c8c55560188602e666ddf3e881705",
                     host="ec2-34-230-153-41.compute-1.amazonaws.com",
                     port="5432")
    #Se crea el cursor y se define y ejecuta la query             
    cursor= connection.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    #Se buscan los datos y se agregan a una lista
    row = cursor.fetchall()
    listBox = Listbox(frame, width=64, height=16)
    listBox.grid(row=10, columnspan=4, sticky=W+E)
    for x in row:
        listBox.insert(END, x)
    #Se finaliza la conexión a la base de datos
    connection.commit()
    connection.close()

#Función para buscar al estudiante por el id
def buscar(id):
    #Se ingresan credenciales
    connection= psycopg2.connect(dbname="daads17to2qqm5",
                     user="dstunsoypdpdpn",
                     password="cbb5e68b3caffdb4b5dcfb015ea18957192c8c55560188602e666ddf3e881705",
                     host="ec2-34-230-153-41.compute-1.amazonaws.com",
                     port="5432")
    #Se crea el cursor y se define y ejecuta la query
    cursor= connection.cursor()
    query = '''SELECT * FROM students WHERE id=%s'''
    cursor.execute(query, (id))
    #Se busca el dato y se llama a la función de despligue de la información
    row = cursor.fetchone()
    muestraLinea(row)
    #Se cierra la conexión a la base de datos
    connection.commit()
    connection.close()

#Función para mostrar los datos de un estudiante buscado por id
def muestraLinea(row):
    listBox = Listbox(frame, width=64, height=16)
    listBox.grid(row=10, columnspan=4, sticky=W+E)
    listBox.insert(END, row)

#Se crea el canva
canvas=Canvas(root, height=3840, width=2160) 
canvas.pack()

#Se agrega el frame para el Canvas (añade espaciados)
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
label = Label(frame, text="Agrega a un estudiante")
label.grid(row=0, column=1)

#Se agrega el label para el nombre
label = Label(frame, text="Nombre")
label.grid(row=1, column=0)
entryName = Entry(frame)
entryName.grid(row=1, column=1)

#Se agrega el label para la edad
label = Label(frame, text="Edad")
label.grid(row=2, column=0)
entryAge = Entry(frame)
entryAge.grid(row=2, column=1)

#Se agrega el label para la dirección
label = Label(frame, text="Dirección")
label.grid(row=3, column=0)
entryAddress = Entry(frame)
entryAddress.grid(row=3, column=1)

#Se crea el botón para guardar la información del estudiante
button = Button(frame, text="Add", command=lambda:guardaEstudiante(entryName.get(), 
                                                                   entryAge.get(),
                                                                   entryAddress.get()))
button.grid(row=4, column=1, sticky=W+E)

#Se crea el label para buscar al estudiante por id
label = Label(frame, text="Busca tus datos")
label.grid(row=5, column=1)
label = Label(frame, text="Busca por el id")
label.grid(row=6, column=0)
idBuscado = Entry(frame)
idBuscado.grid(row=6, column=1)
#Se agrega el botón para confirmar la búsqueda
button = Button(frame, text="Buscar", command=lambda:buscar(idBuscado.get()))
button.grid(row=6, column=2, sticky=W+E)

#Se agrega un último botón para ver a todos los estudiantes guardados
button = Button(frame, text="Visualiza todos los estudiantes", command=lambda:visualizaEstudiante())
button.grid(row=7, column=1, sticky=W+E)

#Termina la aplicación
root.mainloop()