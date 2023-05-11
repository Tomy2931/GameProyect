import math
def ejemplo1():    #Metodos clases
    class Torta:
        def __init__(self,ingred):
            self.ingred = ingred
            
        def __repr__(self):
            return f'torta({self.ingred !r})'        
        
        
        @classmethod

        def torta_chocolate(cls):
            return cls(['harina','leche','chocolate'])
        
        @classmethod
        
        def torta_vainilla(cls):
            return cls(['harina','leche','vainilla'])
        
    print(Torta.torta_chocolate())    


class Torta:
        def __init__(self,ingred,tamaño):
            self.ingred = ingred   
            self.tamaño = tamaño 
        def __repr__(self):
            return (f'Torta({self.ingred,self.tamaño},'f'{self.tamaño})')
        def area(self):
            return self.tamaño_area(self.tamaño)
        @staticmethod
        def tamaño_area(A):
            return A **2 * math.pi
        
        
caca = Torta(['harina','azucar','leche'],4)      
print(caca.tamaño_area())  