#propiedades()

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario  
    def __getnombre(self):
        return self.__nombre
    
    def __getsalario(self):
        return self.__salario
    
    def __setnombre(self,nombre):
        self.__nombre = nombre
        
    def __setsalario(self,salario):
        self.__salario = salario
        
    def __delnombre(self):
        del self.__nombre
    
    def __delsalario(self):
        del self.__salario
              

    nombre = property(fget= __getnombre,
                      fset=__setnombre,
                      fdel=__delnombre,
                      doc="Soy la propiedad del 'nombre' ")

    salario = property(fget= __getsalario)

empleado2 = Empleado('Jorge',2000)

empleado2.nombre = 'Samuel'
print(empleado2.nombre,empleado2.salario)


# empleado1 = Empleado('Jujuy',100)
# print(empleado1.getnombre(),',', empleado1.getsalario())        

# print(empleado1.setnombre("Eeeo"))

# print(empleado1.getnombre())