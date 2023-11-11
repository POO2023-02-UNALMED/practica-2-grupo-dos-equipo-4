from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("Hamburgueseria")
ventana.geometry("800x600")

def evento():
    pass

def salir_sistema():
    ventana.destroy()

def descripcion():
    texto = "Sistema de Hamburgueseria"
    label = tk.Label(ventana, text=texto)
    label.pack()

menuInicial = tk.Menu(ventana)
ventana.config(menu=menuInicial)
menu1 = tk.Menu(menuInicial)
menuInicial.add_cascade(label="Inicio",menu=menu1,command=evento)
menu1.add_command(label="Salir de la Aplicación",command=salir_sistema)
menu1.add_command(label="Descripción del Sistema",command=descripcion)

## contenedor 1
frame_principal1 = tk.Frame(ventana, bg="orange")
frame_principal1.pack(side="left", fill="both", expand=True)

frame1 = tk.Frame(frame_principal1, bg="red")
frame2 = tk.Frame(frame_principal1, bg="blue")

## contenedor 2
frame_principal2 = tk.Frame(ventana, bg="violet")
frame_principal2.pack(side="right", fill="both", expand=True)

frame3 = tk.Frame(frame_principal2, bg="green")
frame4 = tk.Frame(frame_principal2, bg="yellow")

frame1.pack(side="top", fill="both", padx=10, pady=10, expand= True)
frame2.pack(side="bottom", fill="both", padx=10, pady=100, expand=True)
frame3.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame4.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)

ventana.mainloop()
