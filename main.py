#Interfaz grafica jeje XD
# Programa desarrollado por Dali Lopez, todos los derechos me pertenecen a  mi
# si no fierro, no robes descaradamente, ojo.
from tkinter import *
import graphviz

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Automatas Finitos Determininstas")
        self.resizable(True,True)
        self.geometry("1280x720")
        self.init()
    def init(self):
        #frame_botones = Frame(self)
        #frame_botones.pack(side="left", expand=True, fill="y", anchor="nw")
        #frame_botones.config(width=300, bg='#1E262C')
        self.container = Frame(self)
        self.container.pack(side="left", expand=True, fill="x")
        self.container.config(height=1280, width=720,bg='#E3F8FF')
        
        transition = [StringVar()]
        
        #Entry_transition = [Entry(self, font=("Candara", 12), bg="white", fg="black").place(x=180, y=300, width=100, height=30)]
        Entrada1 = Entry(self,textvariable=transition[0], font=("Candara", 12), bg="white", fg="black").place(x=180, y=300, width=100, height=30)
        print("asdf: "+transition[0].get())
        label_name = Label(self, text="Autómatas finitos deterministas", font=("Impact", 20),bg='#E3F8FF', fg="black", anchor=NW).place(x=50, y=10)
        button_add_transition = Button(self, text="Agregar transición", font=("Candara", 12), bg="#E3F8FF", fg="black", anchor=NW, command=lambda: self.addTransition(transition)).place(x=30, y=300)
        # self.frame_m = Frame
        # self.frame_m = frame_chat.Frame_chat(self.container)
        
        
        #Entry_transition[0] = Button(self.container, text="Chat", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.prueba).place(x=0, y=0, width=300, height=35)
        #Entry_transition.add(Button())
        #Entry_transition[1] = Button(self.container, text="drogas", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.prueba).place(x=10, y=10, width=300, height=35)

        #frame_botones.button_2 = Button(frame_botones, text="Ayuda", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.prueba).place(x=0, y=36, width=300, height=35)
    def prueba(self):
        print("prue")
    def addTransition(self,transitions):
        
        print("Agregando una nueva transicion: Sumanod los valores: "+transitions[0].get())
        
        #transitions.append(Entry(self, font=("Candara", 12), bg="white", fg="black").place(x=180, y=300, width=100, height=30))
        
root = App()
root.mainloop()