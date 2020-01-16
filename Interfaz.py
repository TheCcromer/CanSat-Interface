#!/usr/bin/python3

import csv  # este es un modulo reader que permite leer los archivos csv 
import numpy as np #aun no la utilizo
import tkinter as tk #libreria para la interfez grafica, en windows viene incluida en linux se ocupa descargar pero es facil


ventana = tk.Tk()

ventana.title("Primer ventana")

ventana.geometry('380x300') #AnchoxAlto

ventana.configure(background = 'dark turquoise')

#etiquetas

temperatura_etiqueta = tk.Label(ventana,text="Temperatura",bg="red",fg="white") #En que ventana, nombre, color fondo, color de fuente

#metodos para manipular las etiquetas
temperatura_etiqueta.pack(padx=20,pady=20)


ventana.mainloop() # mantiene la ventana viva por medio de un ciclo infinito 
