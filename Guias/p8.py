#Polimorfismo

class Tomate:
    def tipo(self):
        print('vegetal')
    def color(self):
        print('rojo')
        
class Manzana:
    def tipo(self):
        print('fruta')
    def color(self):
        print('verde')    
        
def funcion(objeto):
      objeto.tipo()        
      objeto.color()      
      
new_tomate= Tomate()

funcion(new_tomate)        