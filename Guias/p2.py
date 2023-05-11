# Metodo Constructor
class Persona:
    def __init__(self,name,year):
        pass
        self.name = name
        self.year = year
    def descrp(self):
        return "{} tiene {}".format(self.name,self.year)

    def coment(self,frase):
        return '{} dice: {}'.format(self.name,frase)

panadero = Persona("Ricardo",21)

print(panadero.descrp())
print(panadero.coment("Subeme la radio"))


class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

correo = Email()

print(correo.enviado)
correo.enviar_correo()
print(correo.enviado)
