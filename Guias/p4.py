class Calculadora:
    def __init__(self,num):
        self.n = num
        self.datos = [0 for i in range(num)]
    
    def ingresar_datos(self):
        self.datos = [int(input('Ingresar dato n°' +  str(i+1) + ' = ')) for i in range(self.n)]

class operation(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b = self.datos
        s = a + b 
        print('El resultado es: ' ,s)   
    
    def resta(self):
        a,b = self.datos
        s = a - b 
        print('El resultado es: ' ,s)       

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
        
    def cuadrada(self):
        import math
        a = self.datos
        print('El resultado es: ' ,math.sqrt(a))    
        
ejemplo = operation()
# print(ejemplo.ingresar_datos())
# print(ejemplo.suma())        

isinstance(ejemplo,operation)    #Objeto contiene esta clase?

issubclass(operation,Calculadora) #Subclase pertenece a esta superclase?