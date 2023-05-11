#Polimorfismo con metodo

class Argentina:
    def capital(self):
        print("Buenos Aires")
    def idioma(self):
        print("español")
        
class Japon:         
    def capital(self):
            print("Tokio")
    def idioma(self):
            print("japones")
            
japones = Japon()
argentino = Argentina()           

for pais in (argentino,japones):
    pais.capital()
    pais.idioma()
    
#Polimorfismo con herencia

class Aves:
    def volar(self):
        print('la mayoria de las aves pueden volar')
        
class Aguila:
    def volar(self):
        print('las aguilas pueden volar')
        
class Gallina:
    def volar(self):
        print('las gallinas no pueden volar')     
        
obj_ave = Aves()        
obj_gallina = Gallina()        
obj_aguila = Aguila()        
   
obj_ave.volar()
obj_gallina.volar()
obj_aguila.volar()