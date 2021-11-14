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
        self.positions_xy = functions.count_entry_position(180, 290)
        self.transition = list()
        self.container = Frame(self)
        self.container.pack(side="left", expand=True, fill="x")
        self.container.config(height=1280, width=720,bg='#E3F8FF')
        ##### Agregando los entry
        self.transition.append(StringVar())
        self.number_of_entry = 0
        
        self.Entry_transition = [Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black")]
        self.Entry_transition[self.number_of_entry].place(x=self.positions_xy.x, y=self.positions_xy.y, width=100, height=30)
        
        self.prueba = Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black")
        self.prueba.place(x=500, y=self.positions_xy.y, width=100, height=30)
        #self.Entry_transition = [Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black").pack(padx=self.positions_xy.x, pady=self.positions_xy.y)]
        
        # must be -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        #### Fin de los entry
        
        #### Labels
        label_name = Label(self, text="Autómatas finitos deterministas", font=("Impact", 20),bg='#E3F8FF', fg="black", anchor=NW).place(x=50, y=10)
        #### Fin de Labels
        
        #### Buttons
        button_add_transition = Button(self, text="Agregar transición", font=("Candara", 12), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.addTransition(self.positions_xy))
        button_add_transition.place(x=30, y=290)
        
        button_get_values = Button(self, text="Obtener valores", font=("Candara", 12), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: functions.getValues_function(self, self.transition))
        button_get_values.place(x=30, y=320)
        
        button_clear = Button(self, text="Limpiar", font=("Candara", 12), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.clear_all())
        button_clear.place(x=30, y=50)
        #### Fin de Buttons
    
    def addTransition(self,positions_xy):
        positions_xy.newValues()
        self.number_of_entry = self.number_of_entry + 1
        self.transition.append(StringVar())
        self.Entry_transition.append(Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black"))
        self.Entry_transition[self.number_of_entry].place(x=positions_xy.x, y=positions_xy.y, width=100, height=30)
    def clear_all(self):
        self.positions_xy = functions.count_entry_position(180, 290)
        print("Limpiar")
        
        for entry in self.Entry_transition:
            entry.place_forget()
        #self.Entry_transition[0].place_forget()
        self.prueba.place_forget()
        self.number_of_entry = 0
        self.transition.append(StringVar())
        self.Entry_transition = [Entry(self,textvariable=self.transition[self.number_of_entry], font=("Candara", 12), bg="white", fg="black")]
        self.Entry_transition[self.number_of_entry].place(x=self.positions_xy.x, y=self.positions_xy.y, width=100, height=30)
            
            
root = App()
root.mainloop()