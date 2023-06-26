import tkinter as tk
import csv

ventana = tk.Tk

def guardar_en_csv():
    texto = entrada.get()

    with open('archivo.csv', 'a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([texto])

# Crear la ventana
ventana = tk.Tk()

# Crear una casilla de entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para guardar el texto en el CSV
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_en_csv)
boton_guardar.pack()

# Ejecutar la ventana
ventana.mainloop()