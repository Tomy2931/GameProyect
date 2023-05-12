# (defense, speed, life, strenght, weapon)
import random

def stats(num):
    #Assasin stats
    if num == 1:
        def_points = random.randint(10,50)
        speed_points = random.randint(20,90)
        life_points = random.randint(90,140)
        strenght_points = random.randint(50,110)
        return def_points,speed_points,life_points,strenght_points
    
    #Warrior stats
    if num == 2:
        def_points = random.randint(20,80)
        speed_points = random.randint(10,50)
        life_points = random.randint(100,190)
        strenght_points = random.randint(80,160)
        return def_points,speed_points,life_points,strenght_points
    
    #Shooter stats
    if num == 3:
        def_points = random.randint(20,40)
        speed_points = random.randint(20,65)
        life_points = random.randint(50,100)
        perception_points = random.randint(100,180)
        return def_points,speed_points,life_points,perception_points
    
    
    #Mague/Healer stats
    if num == 4 or num ==5:
        def_points = random.randint(40,90)
        speed_points = random.randint(20,65)
        life_points = random.randint(50,100)
        power_points = random.randint(80,200)
        return def_points,speed_points,life_points,power_points


    
def weapons():
    weapon_store = []
    armas = ["Copper Shortsword","Platinum Shortsword","Katana","Titanium Sword","Gold Shortsword","Mythril Sword"]
    cont = 3
    lista= []
    while cont >0:
        num = random.randint(0,(len(armas)-1))
            
        if num not in lista:
            lista.append(num) 
            weapon_name = armas[num]    
            weapon_store.append(weapon_name)
            cont = cont-1         
    return weapon_store

def select_weapon():
    weapon_store = weapons()
    damage_list = []
    print("")
    for i in range(0,3): 
        weapon_damage = random.randint(30,100) 
        damage_list.append(weapon_damage)
        print(weapon_store[i],':', weapon_damage,"damage")
        print('-------------------------------------')
    
    print("")
    print("Select one of the weapons: 1/2/3")
    print("")
    weapon = int(input("Selection: "))
    print("")
    print(weapon_store[weapon-1], 'selected')
    print("")
    print(damage_list[weapon-1])
    return damage_list[weapon-1]

select_weapon()
