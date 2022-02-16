"""
This file contains code for the game "Attack The Enemy RPG".
Author: DigitalCreativeApkDev
"""


# Importing necessary libraries


import sys
import uuid
import copy
import random
from mpmath import mp, mpf
import os

mp.pretty = True

# Creating static function to be used in this game.


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes


class Player:
    """
    This class contains attributes of the player in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        self.id: str = str(uuid.uuid1())  # Generating random player ID
        self.name: str = name
        self.level: int = 1
        self.max_hp: mpf = mpf(random.randint(120, 150))
        self.curr_hp: mpf = self.max_hp
        self.attack_power: mpf = mpf(random.randint(20, 50))
        self.defense: mpf = mpf(random.randint(20, 50))

    def level_up(self):
        # type: () -> None
        self.max_hp *= 2
        self.restore()
        self.attack_power *= 2
        self.defense *= 2

    def restore(self):
        # type: () -> None
        self.curr_hp = self.max_hp

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "ID: " + str(self.id) + "\n"
        res += "Name: " + str(self.name) + "\n"
        res += "HP: " + str(self.curr_hp) + "/" + str(self.max_hp) + "\n"
        res += "Attack Power: " + str(self.attack_power) + "\n"
        res += "Defense: " + str(self.defense) + "\n"
        return res

    def is_alive(self):
        # type: () -> bool
        return self.curr_hp > 0

    def attack(self, other):
        # type: (Player) -> None
        raw_damage: mpf = self.attack_power - other.defense
        damage: mpf = raw_damage if raw_damage > mpf("0") else mpf("0")
        other.curr_hp -= damage
        print(str(self.name) + " dealt " + str(damage) + " damage at " + str(other.name) + "!")

    def clone(self):
        # type: () -> Player
        return copy.deepcopy(self)


class Enemy(Player):
    """
    This class contains attributes of the enemy in this game.
    """

    def __init__(self):
        # type: () -> None
        Player.__init__(self, "CPU")


# Creating main function used to run the game.


def main():
    """
    This main function is used to run the game.
    :return: None
    """

    print("Welcome to 'Attack The Enemy RPG' by 'DigitalCreativeApkDev'.")
    print("This game is a turn-based RPG where your mission is to reach a level as high as possible without dying.")

    name: str = input("Please enter your name: ")
    player: Player = Player(name)
    enemy: Enemy = Enemy()

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_playing: str = input("Do you want to continue playing 'Attack The Enemy RPG'? ")
    while continue_playing == "Y":
        curr_round: int = 1  # initial value
        turn: int = 0  # initial value
        while player.is_alive():
            print("-------------------------ROUND " + str(curr_round) + "-------------------------")
            print("Your stats: " + str(player) + "\n")
            print("Your enemy's stats: " + str(enemy) + "\n")
            if turn % 2 == 0:
                print("It is your turn to attack.")
                print("Enter 'ATTACK' to attack your enemy.")
                print("Enter anything else to quit the game.")
                action: str = input("What do you want to do? ")
                if action == "ATTACK":
                    player.attack(enemy)
                else:
                    sys.exit()

                turn += 1

            else:
                print("It is your enemy's turn to attack")
                enemy.attack(player)
                turn += 1

            if not enemy.is_alive():
                print("You have defeated your enemy! You advance to round " + str(curr_round + 1) + "!")
                player_level_ups: int = random.randint(1, 100)
                enemy_level_ups: int = random.randint(1, 100)
                for i in range(player_level_ups):
                    player.level_up()

                for i in range(enemy_level_ups):
                    enemy.level_up()

        print(str(player.name) + " has been defeated! You reached round " + str(curr_round) + "!")
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing 'Attack The Enemy RPG'? ")

    sys.exit()


if __name__ == '__main__':
    main()
