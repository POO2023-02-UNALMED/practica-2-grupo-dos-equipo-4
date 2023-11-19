from tkinter import *
import tkinter as tk
from tkinter import messagebox


class FieldFrame(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado):

        super().__init__(master)

        self.data = {}
        self.dataform = {}
        self.tituloValores = tituloValores
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.valores = valores
        self.habilitado = habilitado

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = tk.Frame(self, bg="white", borderwidth=1, relief="solid", width=900, height=500)
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_propagate(False)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        tituloCriterios = Label(frameForm, text=f"{tituloCriterios}")
        tituloCriterios.grid(row=0, column=0, padx=5, pady=10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        tituloValores = Label(frameForm, text=f"{tituloValores}")
        tituloValores.grid(row=0, column=1, pady=10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el titulo de la consulta
        for index, criterio in enumerate(criterios):
            criterio_label = tk.Label(frameForm, text=f"{criterio}")
            criterio_label.grid(row=index + 1, column=0, padx=5)
            frameForm.grid_rowconfigure(index + 1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)

            input_widget = tk.Entry(frameForm, width=50)
            input_widget.place(width=100, height=100)
            input_widget.grid(row=index + 1, column=1, padx=1)

            frameForm.grid_rowconfigure(index + 1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)

            if valores and index < len(valores):
                input_widget.insert(0, valores[index])

            if not habilitado[index]:
                input_widget.config(state="disabled")

            self.data[criterio] = {
                "widget": input_widget,
                "value": None
            }

        # Botón para enviar el formulario
        button = Button(frameForm, text="enviar", height=1, width=7)
        #button.grid(row=index + 2, column=0, pady=20)
        frameForm.grid_rowconfigure(index + 2, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        clear = Button(frameForm, text="clear", bg="white", command=self.clear, height=1, width=6)
        #clear.grid(row=index + 2, column=1)
        frameForm.grid_rowconfigure(index + 2, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)
        self.radio_var = tk.StringVar()

        # Create the radio buttons
        self.radio_efectuar = tk.Radiobutton(frameForm, text="Efectuar reserva", variable=self.radio_var, value="Efectuar reserva",
                                             command=self.create_additional_frame)
        self.radio_hacer = tk.Radiobutton(frameForm, text="Hacer reserva", variable=self.radio_var, value="Hacer reserva",command=self.create_additional_frame)

        self.radio_cancelar = tk.Radiobutton(frameForm, text="Cancelar reserva", variable=self.radio_var, value="Cancelar reserva",
                                             command=self.create_additional_frame)
        self.radio_salir = tk.Radiobutton(frameForm, text="Salir de Gestion de Reservas", variable=self.radio_var, value="Yes",command=self.salir)

        # Pack the radio buttons
        self.radio_efectuar.grid(row=index - 1, column=0, padx=1, pady=10)
        self.radio_hacer.grid(row=index+0, column=0, padx=1, pady=10)
        self.radio_cancelar.grid(row=index +1, column=0, padx=1, pady=10)
        self.radio_salir.grid(row=index + 3, column=0, padx=10, pady=10)

    def salir(self):
        self.destroy()

    def create_additional_frame(self):
        if self.radio_var.get() == "Efectuar reserva":
            # Definimos los titulos de valores y criterio.
            tituloCriterios = "Componentes necesarios"
            criterios = ["Escriba la fecha, en el formato 00/00/00", "Escriba el numero de asientos"]
            tituloValores = "Complete"
            valores = ["", "", ""]
            habilitado = [True, True, True]

            # Crear un nuevo Frame.
            frame_efectuar_reserva = Toplevel(self)
            frame_efectuar_reserva.grid()

            # Creo otro fieldFrame para esta opcion
            frame_adicional_efectuar = FieldFrame(frame_efectuar_reserva, tituloCriterios, criterios, tituloValores, valores,
                                                  habilitado)
            frame_adicional_efectuar.grid()
        elif self.radio_var.get() == "Hacer reserva":
            # Definimos los titulos de valores y criterio.
            tituloCriterios = "Componentes necesarios"
            criterios = ["Escriba la fecha, en el formato 00/00/00", "Escriba el numero de asientos"]
            tituloValores = "Complete"
            valores = ["", "", ""]
            habilitado = [True, True, True]

            # Crear un nuevo Frame.
            frame_hacer_reserva = Toplevel(self)
            frame_hacer_reserva.grid()

            # Creo otro fieldFrame para esta opcion
            frame_adicional_hacer = FieldFrame(frame_hacer_reserva, tituloCriterios, criterios, tituloValores, valores,
                                               habilitado)
            frame_adicional_hacer.grid()
        elif self.radio_var.get() == "Cancelar reserva":
            # Definimos los titulos de valores y criterio.
            tituloCriterios = "Componentes necesarios"
            criterios = ["Escriba la fecha, en el formato 00/00/00", "Escriba el numero de asientos"]
            tituloValores = "Complete"
            valores = ["", "", ""]
            habilitado = [True, True, True]

            # Crear un nuevo Frame.
            frame_cancelar_reserva = Toplevel(self)
            frame_cancelar_reserva.grid()

            # Creo otro fieldFrame para esta opcion
            frame_adicional_cancelar = FieldFrame(frame_cancelar_reserva, tituloCriterios, criterios, tituloValores, valores,
                                                  habilitado)
            frame_adicional_cancelar.grid()

    def getValue(self, criterio):
        return self.data[criterio]["value"]

    def getValues(self):
        return self.dataform

    def clear(self):
        for criterio, info in self.data.items():
            info["widget"].delete(0, END)
            info["value"] = None

    def enviar(self):
        self.submitForm()
        valores = self.getValue()
        self.criterios(valores)

    def submitForm(self):
        resultados = []
        for criterio, info in self.data.items():
            valor = info["widget"].get()
            if valor is None or valor == "":
                messagebox.showinfo("Alerta", f"Campo '{criterio}' no puede estar vacío.")
                return
            resultados.append(f"{criterio}: {valor}")
        self.resultado_label.config(text="\n".join(resultados))


root = tk.Tk()  # Create a Tkinter window
root.geometry("1200x600")

# Define the titles, criteria, initial values, and enabled flags
tituloCriterios = "¿Que deseas hacer?"
criterios = ["Efectuar reserva", "Hacer reserva", "Cancelar reserva"]
tituloValores = "Descripciones"
valores = ["Aqui puedes verificar la confirmacion de tu reserva", "Aqui puedes Crear tu reserva a tu gusto",
           "Puedes deshacer tu reserva sin ningun tipo de costo"]
habilitado = [True, True, False]

# Create a FieldFrame
field_frame = FieldFrame(root, tituloCriterios, criterios, tituloValores, valores, habilitado)
field_frame.pack()

root.mainloop()  # Start the Tkinter event loop
