class Persona():
    edad = 22
    nombre = "Javier"
    sexo = "hombre"

panadero = Persona()

print (getattr(panadero,'edad')) #Valor de atributo

print (hasattr(panadero,'edad')) #Tiene ese atributo? t/f

setattr(panadero,'nombre','Pedro') #Cambiar valor

print (getattr(panadero,'nombre'))

delattr(Persona,'sexo')

print (hasattr(panadero,'sexo'))