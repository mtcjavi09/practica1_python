#Import para crear la app
from tkinter import Label, Frame, Tk, Canvas, Entry, Button, W, E
#Import driver de conexión para postgresql
import psycopg2

#Se crea la pantalla emergente
root = Tk()
root.title("Python y PostgreSQL")

def guardaEstudiante(name, address, age):
    connection= psycopg2.connect(dbname="daads17to2qqm5",
                     user="dstunsoypdpdpn",
                     password="cbb5e68b3caffdb4b5dcfb015ea18957192c8c55560188602e666ddf3e881705",
                     host="ec2-34-230-153-41.compute-1.amazonaws.com",
                     port="5432")                     
    cursor= connection.cursor()
    query = '''INSERT INTO students(name, age, address) VALUES(%s, %s, %s)'''
    nombre = name
    edad = age
    direccion = address
    cursor.execute(query, (nombre, edad, direccion))
    print("Datos guardados")
    connection.commit()
    
#Se crea el canva
canvas=Canvas(root, height=380, width=400)
canvas.pack()

#Se agrega el frame para el Canvas (añade espaciados)
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
label = Label(frame, text="Agrega a un estudiante")
label.grid(row=0, column=1)


label = Label(frame, text="Nombre")
label.grid(row=1, column=0)
entryName = Entry(frame)
entryName.grid(row=1, column=1)

label = Label(frame, text="Edad")
label.grid(row=2, column=0)
entryAge = Entry(frame)
entryAge.grid(row=2, column=1)

label = Label(frame, text="Dirección")
label.grid(row=3, column=0)
entryAddress = Entry(frame)
entryAddress.grid(row=3, column=1)


button = Button(frame, text="Add", command=lambda:guardaEstudiante(entryName.get(), 
                                                                   entryAge.get(),
                                                                   entryAddress.get()))

button.grid(row=4, column=1, sticky=W+E)
root.mainloop()