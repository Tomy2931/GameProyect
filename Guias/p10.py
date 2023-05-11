#Encapsulacion

class Cliente: 
    def __init__(self):
        self.__codigo = 123
        
    def __cuenta(Self):
        print('cuenta de procesamiento')    
        
    def getcodigo(Self):
        return Self.__codigo  
     
persona = Cliente()

try:
    print(persona.__codigo)   
except   AttributeError as error:
    print("No se puede acceder a esta informacion")  
  
#objeto._nombreclase__nombreatributo  
     
print(persona._Cliente__codigo)

persona._Cliente__cuenta()