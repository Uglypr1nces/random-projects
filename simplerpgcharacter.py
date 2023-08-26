class Character:
    def __init__(self, health, attack, defense):
        self.attack = attack
        self.health = health
        self.defense = defense

user = Character(health=100, attack=60, defense=100)
enemy = Character(health=700, attack=100, defense=300)

battle = input("Ready to battle the enemy? (y or n): ")
if battle.lower() == "y":
    print("Your health is {}, your attack is {}, your defense is {}".format(user.health, user.attack, user.defense))
    print("The enemy health is {}, enemy attack is {}, enemy defense is {}".format(enemy.health, enemy.attack, enemy.defense))

    while user.health > 0 and enemy.health > 0:
        print("You attack the enemy!")
        damage_to_enemy = user.attack - enemy.defense
        if damage_to_enemy > 0:
            enemy.health -= damage_to_enemy

        if enemy.health <= 0:
            print("You won!")
            break

        print("The enemy attacks you!")
        damage_to_user = enemy.attack - user.defense
        if damage_to_user > 0:
            user.health -= damage_to_user

        if user.health <= 0:
            print("You lost!")
            break


