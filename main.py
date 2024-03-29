#Interfaz grafica jeje XD
# Programa desarrollado por Dali Lopez, todos los derechos me pertenecen a  mi
# si no fierro, no robes descaradamente, ojo.
from tkinter import *
from functions import functions
import graphviz

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Automatas Finitos Determininstas")
        self.resizable(True,True)
        self.geometry("1280x720")
        self.init()
    def init(self):
        self.positions_xy = functions.count_entry_position(180, 190)
        self.transition = list()
        self.container = Frame(self)
        self.container.pack(side="left", expand=True, fill="x")
        self.container.config(height=1280, width=720,bg='#E3F8FF')
        ##### Agregando los entry
        
        self.transition.append(StringVar())
        self.alfabeto = StringVar()
        self.estados = StringVar()
        self.estado_inicial = StringVar()
        self.estados_finales = StringVar()
        
        self.number_of_entry = 0
        
        self.Entry_estados = Entry(self,textvariable=self.estados, font=("Candara", 12), bg="white", fg="black")
        self.Entry_estados.place(x=180 , y=130 , width=100, height=30)
        
        self.Entry_alfabeto = Entry(self,textvariable=self.alfabeto, font=("Candara", 12), bg="white", fg="black")
        self.Entry_alfabeto.place(x=180 , y=160 , width=100, height=30)
        
        self.Entry_transition = [Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black")]
        self.Entry_transition[self.number_of_entry].place(x=self.positions_xy.x, y=self.positions_xy.y, width=100, height=30)
        
        self.Entry_estado_inicial = Entry(self,textvariable=self.estado_inicial, font=("Candara", 12), bg="white", fg="black")
        self.Entry_estado_inicial.place(x=420 , y=130 , width=100, height=30)
        
        self.Entry_estados_finales = Entry(self,textvariable=self.estados_finales, font=("Candara", 12), bg="white", fg="black")
        self.Entry_estados_finales.place(x=420 , y=160 , width=100, height=30)
                
        # must be -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        #### Fin de los entry
        
        #### Labels
        label_name = Label(self, text="Autómatas finitos deterministas", font=("Impact", 20),bg='#E3F8FF', fg="black", anchor=NW).place(x=50, y=10)
        
        label_estado_inicial = Label(self, text="Estado inicial", font=("Lucida console", 10),bg='#E3F8FF', fg="black", anchor=NW).place(x=280, y=129)
        label_estados_finales = Label(self, text="Estados finales", font=("Lucida console", 10),bg='#E3F8FF', fg="black", anchor=NW).place(x=280, y=159)
        label_estados = Label(self, text="Estados", font=("Lucida console", 10),bg='#E3F8FF', fg="black", anchor=NW).place(x=20, y=129)
        label_alfabeto = Label(self, text="Alfabeto", font=("Lucida console", 10),bg='#E3F8FF', fg="black", anchor=NW).place(x=20, y=159)
        
        #self.img = PhotoImage(file="diagrama_automata.png")
        #self.label_image_automata = Label(self, image = self.img)
        
        #### Fin de Labels
        
        #### Buttons
        button_add_transition = Button(self, text="Agregar transición", font=("Lucida console", 10), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.addTransition())
        button_add_transition.place(x=20, y=190)

        button_get_values = Button(self, text="Dibujar autómata", font=("Lucida console", 12), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.dibujar_automata())
        button_get_values.place(x=420, y=100)
        
        button_clear = Button(self, text="Limpiar", font=("Lucida console", 10), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.clear_all())
        button_clear.place(x=20, y=50)
        #### Fin de Buttons
    
    def addTransition(self):
        self.positions_xy.newValues()
        self.number_of_entry = self.number_of_entry + 1
        self.transition.append(StringVar())
        self.Entry_transition.append(Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black"))
        self.Entry_transition[self.number_of_entry].place(x=self.positions_xy.x, y=self.positions_xy.y, width=100, height=30)
    
    def clear_all(self):
        self.positions_xy = functions.count_entry_position(180, 190)
        self.transition.clear()
        print("Limpiar: ",self.transition)
        for entry in self.Entry_transition:
            entry.place_forget()
        self.number_of_entry = 0
        self.transition.append(StringVar())
        self.Entry_transition = [Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black")]
        self.Entry_transition[self.number_of_entry].place(x=self.positions_xy.x, y=self.positions_xy.y, width=100, height=30)
        try: 
            print(self.label_image_automata.place_forget())
        except EOFError:
            print("No hay imagen que borrar")
    def dibujar_automata(self):
        ##### Pruebas del automata
        #self.estados.set("q0,q1,q2")
        #self.alfabeto.set("0,1")
        #self.transition[0].set("q0,1=q1")
        #self.estado_inicial.set("q0")
        #self.estados_finales.set("q2")
        
        automata_determinista = functions.automata(self.estados.get(), self.alfabeto.get(), self.transition, self.estado_inicial.get(), self.estados_finales.get())
        resultado = automata_determinista.evaluarAutomata()
        # Agregando la imagen al programa
        self.img = PhotoImage(file="diagrama_automata.png")
        self.label_image_automata = Label(self, image = self.img)
        self.label_image_automata.place(x=520,y=130)
        # Resultados
        label_name = Label(self, text=resultado, font=("Impact", 20),bg='#E3F8FF', fg="black", anchor=NW).place(x=680, y=90)

root = App()
root.mainloop()