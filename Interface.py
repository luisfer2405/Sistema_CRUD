import csv
import tkinter as tk
import re
from tkinter import messagebox

ventana= tk.Tk()

canvas = tk.Canvas(ventana, width=400,height=300)
canvas.pack()

def mostrar_campos():
    ventana_secundaria = tk.Toplevel(ventana)  # Crea la ventana secundaria

    # Función para alternar el estado del botón de servicio de internet
    def alternar_estado():
        estado_actual = servicio_internet_var.get()

        if estado_actual:
            # Cambiar el estado a No y ocultar los campos del router
            servicio_internet_var.set(False)
            boton_internet.config(text="Servicio de Internet: No")
            ocultar_campos_router()
        else:
            # Cambiar el estado a Sí y mostrar los campos del router
            servicio_internet_var.set(True)
            boton_internet.config(text="Servicio de Internet: Sí")
            mostrar_campos_router()

    # Botón para indicar si es un servicio de internet
    servicio_internet_var = tk.BooleanVar()
    boton_internet = tk.Button(ventana_secundaria, text="Servicio de Internet: No", command=alternar_estado)
    boton_internet.pack()
    
    def guardar_en_csv():
        valores = [
            entrada_COD.get(),
            entrada_FECHA.get(),
            entrada_NOMBRES.get(),
            entrada_CC.get(),
            entrada_TELEFONO1.get(),
            entrada_TELEFONO2.get(),
            entrada_BARRIO.get(),
            entrada_CORREO.get(),
            entrada_SERVICIO.get(),
            entrada_MES.get(),
            entrada_MENSUALIDAD.get(),
            entrada_AFILIACION.get(),
            entrada_REF_PERSONAL.get(),
            entrada_TELEFONO11.get(),
            entrada_REF_FAMILIAR.get(),
            entrada_TELEFONO21.get()
        ]

        with open('str/bd.csv', 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(valores)

    etiqueta_COD = tk.Label(ventana_secundaria, text="COD")
    etiqueta_COD.pack()
    entrada_COD = tk.Entry(ventana_secundaria, validate="key")
    entrada_COD.config(validatecommand=(entrada_COD.register(lambda text: len(text) <= 5), "%P"))
    entrada_COD.pack()
    
    #validacion de codigo
    def validar_COD():
        codigo = entrada_COD.get()
        if len(codigo) != 5:
            messagebox.showerror('Error', 'El código debe tener 5 dígitos.')

    etiqueta_FECHA = tk.Label(ventana_secundaria, text="FECHA DE INGRESO")
    etiqueta_FECHA.pack()
    entrada_FECHA = tk.Entry(ventana_secundaria, validate="key")
    entrada_FECHA.config(validatecommand=(entrada_FECHA.register(lambda text: text.isdigit() and len(text) == 8), "%P"))
    entrada_FECHA.pack()

    etiqueta_NOMBRES = tk.Label(ventana_secundaria, text="NOMBRES Y APELLIDOS")
    etiqueta_NOMBRES.pack()
    entrada_NOMBRES = tk.Entry(ventana_secundaria, validate="key")
    entrada_NOMBRES.config(validatecommand=(entrada_NOMBRES.register(lambda text: len(text) <= 100), "%P"))
    entrada_NOMBRES.pack()

    etiqueta_CC = tk.Label(ventana_secundaria, text="C.C")
    etiqueta_CC.pack()
    entrada_CC = tk.Entry(ventana_secundaria, validate="key")
    entrada_CC.config(validatecommand=(entrada_CC.register(lambda text: text.isdigit()), "%P"))
    entrada_CC.pack()

    etiqueta_TELEFONO1 = tk.Label(ventana_secundaria, text="TELEFONO 1")
    etiqueta_TELEFONO1.pack()
    entrada_TELEFONO1 = tk.Entry(ventana_secundaria, validate="key")
    entrada_TELEFONO1.config(validatecommand=(entrada_TELEFONO1.register(lambda text: text.isdigit()), "%P"))
    entrada_TELEFONO1.pack()

    etiqueta_TELEFONO2 = tk.Label(ventana_secundaria, text="TELEFONO 2")
    etiqueta_TELEFONO2.pack()
    entrada_TELEFONO2 = tk.Entry(ventana_secundaria, validate="key")
    entrada_TELEFONO2.config(validatecommand=(entrada_TELEFONO2.register(lambda text: text.isdigit()), "%P"))
    entrada_TELEFONO2.pack()

    etiqueta_BARRIO = tk.Label(ventana_secundaria, text="BARRIO / DIRECCION")
    etiqueta_BARRIO.pack()
    entrada_BARRIO = tk.Entry(ventana_secundaria)
    entrada_BARRIO.pack()

    etiqueta_CORREO = tk.Label(ventana_secundaria, text="CORREO ELECTRONICO / EMAIL")
    etiqueta_CORREO.pack()
    entrada_CORREO = tk.Entry(ventana_secundaria)
    entrada_CORREO.pack()

    etiqueta_SERVICIO = tk.Label(ventana_secundaria, text="SERVICIO ASIGNADO")
    etiqueta_SERVICIO.pack()
    entrada_SERVICIO = tk.Entry(ventana_secundaria)
    entrada_SERVICIO.pack()

    etiqueta_MES = tk.Label(ventana_secundaria, text="MES A FACTURAR")
    etiqueta_MES.pack()
    entrada_MES = tk.Entry(ventana_secundaria, validate="key")
    entrada_MES.config(validatecommand=(entrada_MES.register(lambda text: text.isdigit() and 1 <= int(text) <= 12), "%P"))
    entrada_MES.pack()

    etiqueta_MENSUALIDAD = tk.Label(ventana_secundaria, text="VALOR DE LA MENSUALIDAD")
    etiqueta_MENSUALIDAD.pack()
    entrada_MENSUALIDAD = tk.Entry(ventana_secundaria, validate="key")
    entrada_MENSUALIDAD.config(validatecommand=(entrada_MENSUALIDAD.register(lambda text: text.isdigit()), "%P"))
    entrada_MENSUALIDAD.pack()

    etiqueta_AFILIACION = tk.Label(ventana_secundaria, text="VALOR DE LA AFILIACION")
    etiqueta_AFILIACION.pack()
    entrada_AFILIACION = tk.Entry(ventana_secundaria, validate="key")
    entrada_AFILIACION.config(validatecommand=(entrada_AFILIACION.register(lambda text: text.isdigit()), "%P"))
    entrada_AFILIACION.pack()

    etiqueta_REF_PERSONAL = tk.Label(ventana_secundaria, text="REF. PERSONAL")
    etiqueta_REF_PERSONAL.pack()
    entrada_REF_PERSONAL = tk.Entry(ventana_secundaria)
    entrada_REF_PERSONAL.pack()

    etiqueta_TELEFONO11 = tk.Label(ventana_secundaria, text="TELEFONO 1.1")
    etiqueta_TELEFONO11.pack()
    entrada_TELEFONO11 = tk.Entry(ventana_secundaria)
    entrada_TELEFONO11.pack()

    etiqueta_REF_FAMILIAR = tk.Label(ventana_secundaria, text="REF. FAMILIAR")
    etiqueta_REF_FAMILIAR.pack()
    entrada_REF_FAMILIAR = tk.Entry(ventana_secundaria)
    entrada_REF_FAMILIAR.pack()

    etiqueta_TELEFONO21 = tk.Label(ventana_secundaria, text="TELEFONO 2.1")
    etiqueta_TELEFONO21.pack()
    entrada_TELEFONO21 = tk.Entry(ventana_secundaria)
    entrada_TELEFONO21.pack()


    def boton_guardar_click():
        validar_COD()
        guardar_en_csv()

    boton_guardar = tk.Button(ventana_secundaria, text="Guardar")
    boton_guardar.pack()
    boton_guardar.config(command=boton_guardar_click)
    ventana.mainloop()

    campos_router = ['SN/MAC', 'IP', 'NOMBRE DE RED', 'CONTRASEÑA', 'MARCA', 'INGRESO ONU', 'CODIGO DE BARRA']

    campos_router_widgets = []

    # Función para mostrar los campos del router
    def mostrar_campos_router():
        for campo in campos_router:
            etiqueta = tk.Label(ventana_secundaria, text=campo)
            etiqueta.pack()

            entrada = tk.Entry(ventana_secundaria)
            entrada.pack()

            campos_router_widgets.append((etiqueta, entrada))

    # Función para ocultar los campos del router
    def ocultar_campos_router():
        for etiqueta, entrada in campos_router_widgets:
            etiqueta.pack_forget()
            entrada.pack_forget()

    ventana_secundaria.mainloop()

        


   

usuarios = tk.Button(ventana,text='Nuevo usuario',command=mostrar_campos)
usuarios.pack()
usuarios.config(bg="blue", fg="white", width=20, height=2)


editarusuarios = tk.Button(ventana,text='Editar usuarios')
editarusuarios.pack()
editarusuarios.config(bg="blue", fg="white", width=20, height=2)

ventana.mainloop()
