LEVEL=int(input("Level? "))
p_STR =int(input("Strength? "))
p_END =int(input("Endurance? "))
p_SPD =int(input("Speed? "))
e_STR =int(input("Enemy Strength? "))
e_END =int(input("Enemy Endurance? "))
e_SPD =int(input("Enemy Speed? "))
Death =int(input("How many times did you die? "))
Kill =int(input("How many did you kill? "))
enemy_atk= e_STR+ 5*e_SPD
enemy_def = e_END
p_atk = p_STR+ 5*p_SPD+Death*80+Kill*8
p_def= p_END-5*Death
p_DMG =p_atk-enemy_def
e_DMG =enemy_atk-p_def
p_HEALTH = LEVEL+ 10*p_END
e_HEALTH = LEVEL+ 10*e_END
p_HEALTH -=e_DMG
e_HEALTH -=p_DMG
print("The enemy attacks and Kazushi loses ",e_DMG," HP")
print("Kazushi has ",p_HEALTH," HP left")
print("Kazushi strikes back and enemy loses ",p_DMG," HP" )
if e_HEALTH < p_DMG:
    print("Kazushi has killed the fucker")
else:
    print("Kazushi couldn't kill the fucker and has fucking died")