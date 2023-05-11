#Super Class
class Character:
    def __init__(self,name,defense,speed,life):
       self.name = name
       self.defense = defense
       self.life = life
       self.speed = speed
       
    def atributes(self):
        print(self.name, ' stats: ', sep=' ')
        print('')
        print('Defense: ',self.defense)
        print('------------')
        print('Speed: ', self.speed)
        print('------------')
        print('Life: ', self.life)

#Types
       
class Physical(Character):       
    def __init__(self, name, defense, speed, life, strenght, weapon):
        super().__init__(name, defense, speed, life)
        self.strenght = strenght
        self.weapon = weapon
        
    def atributes(self):
        super().atributes()   #Sobreescribimos el metodo de la superclase para agregar los nuevos atributos
        print('------------')
        print('Strenght: ',self.strenght)
        
class Distance(Character):
    def __init__(self, name, defense, speed, life, perception, weapon):
        super().__init__(name, defense, speed, life)       
        self.perception = perception
        self.weapon = weapon
        
    def atributes(self):
        super().atributes()   
        print('------------')
        print('Perception: ',self.perception)    
        
class Magic(Character):
    def __init__(self, name, defense, speed, life, power, book):
        super().__init__(name, defense, speed, life)      
        self.power = power
        self.book = book 
        
    def atributes(self):
        super().atributes()   
        print('------------')
        print('Power: ',self.power)        
        
#Rol

class Assasin(Physical):
    def __init__(self, name, defense, speed, life, strenght, weapon):
        super().__init__(name, defense, speed, life, strenght, weapon) 
    
        

class Warrior(Physical):
    def __init__(self, name, defense, speed, life, strenght, weapon):
        super().__init__(name, defense, speed, life, strenght, weapon)     

class Shooter(Distance):
    def __init__(self, name, defense, speed, life, perception, weapon):
        super().__init__(name, defense, speed, life, perception, weapon)
        
class Healer(Magic):
    def __init__(self, name, defense, speed, life, power, book):
        super().__init__(name, defense, speed, life, power, book)   

class Mague(Magic):
    def __init__(self, name, defense, speed, life, power, book):
        super().__init__(name, defense, speed, life, power, book)     
        
        
Pj1 = Mague('Carlos',20,80,100,50,'dildo')     
print(Pj1.atributes())   
