#f-strings
#format %

def run():
    nombre = "Tomas"
    edad = 22
    print("hola, soy % s y tengo % s años"%(nombre,edad))

    print(("Hola soy {} y tengo {} años") .format(nombre,edad+1))

    print(f"Hola, me llamo {nombre} y mi edad es {edad+4}")


class Estudiante:
    def __init__(self,name,apellido,edad):
        pass
        self.name = name
        self.apellido = apellido
        self.edad = edad  
       
    def __str__(self) -> str:
        return f"Me llamo {self.name} {self.apellido}  y tengo {self.edad} años"
     
    
nuevo_estudiante = Estudiante('Jose',"Peron",29)    
print(f"{nuevo_estudiante}")