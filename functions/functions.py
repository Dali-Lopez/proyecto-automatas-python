class count_entry_position:
    x = 0
    y = 0
    def __init__(self, px, py):
        self.x = px
        self.y = py
        print("x: ",self.x," y: ",self.y)    
    def newValues(self):
        if self.y == 680:
            self.y = 290
            self.x = self.x + 100
        else:
            self.x = self.x + 0
            self.y = self.y + 30
def getValues_function(self,list_values):
    for value in list_values:
            print("valores para las entradas: ", value.get())