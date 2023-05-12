import ramdomizer


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
        

# Pj1 = Mague('Carlos',20,80,100,50,'Katana')     
#     print(Pj1.atributes())   


if __name__ == "__main__":        
    
    def crear_pj():
        print('')  
        print('Creating character')
        print('------------')
        name = input("Name: ")
        print('')    
        print('Classes: 1)Assasin 2)Warrior 3)Shooter 4)Healer 5)Mague') 
        print('')
        choice = 0
        while choice <=0 or choice >5:
            choice = int(input("Class: "))
            if choice <=0 or choice >5:
                print('Invalid number, choose between 1 and 5')
            
            if choice == 1:
                
                def_points,speed_points,life_points,strenght_points = ramdomizer.stats(1)
                objeto= Assasin(name,def_points,speed_points,life_points,strenght_points,"xd")
                
            elif choice == 2:
                def_points,speed_points,life_points,strenght_points = ramdomizer.stats(2)
                objeto = Warrior(name,def_points,speed_points,life_points,strenght_points,"xd")
                
            elif choice == 3:
                def_points,speed_points,life_points,strenght_points = ramdomizer.stats(3)
                objeto = Shooter(name,def_points,speed_points,life_points,strenght_points,"xd")
                
            elif choice == 4:
                def_points,speed_points,life_points,power_points = ramdomizer.stats(4)
                objeto = Healer(name,def_points,speed_points,life_points,power_points,"xd")
                
            elif choice == 5:
                def_points,speed_points,life_points,power_points = ramdomizer.stats(5)
                objeto = Mague(name,def_points,speed_points,life_points,power_points,"xd") 
                  
                                                 
        return objeto
          
    


print(crear_pj().atributes())