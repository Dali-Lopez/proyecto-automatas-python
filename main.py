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
        frame_botones = Frame(self)
        frame_botones.pack(side="left", expand=True, fill="y", anchor="nw")
        frame_botones.config(width=300, bg='#1E262C')
        self.container = Frame(self)
        self.container.pack(side="left", expand=True, fill="x")
        self.container.config(height=720, width=980)
        # self.frame_m = Frame
        # self.frame_m = frame_chat.Frame_chat(self.container)
        frame_botones.button_1 = Button(frame_botones, text="Chat", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.prueba).place(x=0, y=0, width=300, height=35)
        frame_botones.button_2 = Button(frame_botones, text="Ayuda", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.prueba).place(x=0, y=36, width=300, height=35)
    def prueba(self):
        print("ricas drogas")
root = App()
root.mainloop()