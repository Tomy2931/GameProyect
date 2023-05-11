#Herencia

class Pokemon:
    pass
    def __init__(self,name,tipo):
        self.name = name 
        self.tipo = tipo
        
    def desc(self):
        return '{} es un pokemon de tipo {}'.format(self.name,self.tipo)    
    
class Pikachu(Pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.name,tipoataque)
 
class Agumon(Pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.name,tipoataque)    
    



pino = Pikachu("Jorge","Awa")
print (pino.ataque("pijazo"))
