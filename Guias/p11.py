#Metodo super()

class Mamifero:
    def __init__(self,nombre,edad):
        print(nombre, 'es un animal de ',edad,' años')
        
class Leon(Mamifero):
    def __init__(self):
        print('el leon tiene 4 patas')
        super().__init__('Tulio',49) #Tomando variables de la superclase
    def rugir (self,num):
        for i in range(0,num): 
            print("a")
        
leon = Leon()        
print(leon.rugir(5))