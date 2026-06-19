import random


player_health = 100
enemy_health = 100
potions = 3

print("Fighting Game")
print("Defeat the enemy before your health reaches 0.")

while player_health > 0 and enemy_health > 0:
    print("\n--------------------")
    print(f"Your health: {player_health}")
    print(f"Enemy health: {enemy_health}")
    print(f"Potions left: {potions}")
    print("\nChoose your move:")
    print("1. Punch")
    print("2. Kick")
    print("3. Block")1
    print("4. Heal")

    choice = input("Enter 1, 2, 3, or 4: ")

    blocking = False

    if choice == "1":
        damage = random.randint(10, 18)
        enemy_health -= damage
        print(f"You punched the enemy for {damage} damage.")
    elif choice == "2":
        if random.randint(1, 100) <= 70:
            damage = random.randint(18, 30)
            enemy_health -= damage
            print(f"You kicked the enemy for {damage} damage.")
        else:
            print("Your kick missed.")
    elif choice == "3":
        blocking = True
        print("You raised your guard.")
    elif choice == "4":
        if potions > 0:
            heal = random.randint(18, 28)
            player_health += heal
            if player_health > 100:
                player_health = 100
            potions -= 1
            print(f"You healed {heal} health.")
        else:
            print("You have no potions left.")
    else:
        print("Invalid move. You lost your turn.")

    if enemy_health <= 0:
        break

    enemy_move = random.choice(["punch", "kick", "heavy attack"])

    if enemy_move == "punch":
        enemy_damage = random.randint(8, 15)
        print(f"The enemy punched you for {enemy_damage} damage.")
    elif enemy_move == "kick":
        enemy_damage = random.randint(12, 20)
        print(f"The enemy kicked you for {enemy_damage} damage.")
    else:
        enemy_damage = random.randint(18, 26)
        print(f"The enemy used a heavy attack for {enemy_damage} damage.")

    if blocking:
        enemy_damage = enemy_damage // 2
        print(f"You blocked and reduced the damage to {enemy_damage}.")

    player_health -= enemy_damage

print("\n====================")

if player_health <= 0 and enemy_health <= 0:
    print("It is a draw!")
elif player_health <= 0:
    print("You lost the fight.")
else:
    print("You won the fight!")
