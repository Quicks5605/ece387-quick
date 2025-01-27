"""
Risk Game Module

This module simulates a simplified version of the Risk board game. Players recruit units and battle each other until one side is defeated.

Classes:
    Unit: Represents a generic unit in the game.
    Footman: Represents a Footman unit with specific attributes.
    Archer: Represents an Archer unit with specific attributes.
    Knight: Represents a Knight unit with specific attributes.
    SiegeMachine: Represents a Siege Machine unit with specific attributes.
    Player: Represents a player in the game.
    Risk: Represents the Risk game.

Functions: main: Entry point for the game. Initialize and start the Risk game.

Author: Dr. Stan Baek, United Stated Air Force Academy
Date: 18 Jan 2025

**IMPORTANT DISCLAIMER** This code is intended solely for use within the ECE387 class at the United States Air Force Academy. Unauthorized sharing, distribution, or reproduction of this code is strictly prohibited.
"""

import random
from itertools import cycle

# Base class for all units
class Unit:
    """
    Represents a generic unit in the game.
    Attributes:
        name: The name of the unit (e.g., "Footman").
        cost: The cost of the unit in coins.
        attack_dice: The number of dice the unit rolls when attacking.
        health: The health points of the unit.
        hit_threshold: The minimum dice roll required to score a hit.
    """

    def __init__(self, name: str, cost: int, health: int, hit_threshold: int):
        self.name = name
        self.cost = cost
        self.health = health
        self.hit_threshold = hit_threshold

    def roll_attack(self) -> int:
        """
        Roll a die for the unit's attack.
        Returns:
            The total number of hits scored by the unit.
        """
        roll = random.randint(1, 6)  # Roll a six-sided die
        print(f"{self.name} rolls {roll}.")
        return 1 if roll >= self.hit_threshold else 0

    def take_damage(self, damage: int) -> None:
        """
        Reduce the unit's health by the specified amount of damage.
        Ensures health doesn't drop below zero.

        TODO:
        - Subtract the damage value from the unit's health.
        - Ensure the health value never goes below 0. Use `max()` to handle this.
        """
        # Remove the pass statement and implement the health reduction logic.
        
        self.health -= damage
        if self.health < 0:
            self.health = 0


    def isalive(self) -> bool:
        """
        Check if the unit is still alive (health > 0).

        Returns:
            bool: True if the unit's health is greater than 0, otherwise False.

        TODO:
        - Check the value of `self.health`.
        - Return `True` if health is greater than 0, otherwise return `False`.
        """
        # Remove the `return False` statement and implement the logic to check health.
        if self.health >0 :
            return True
        else:
            return False

    def __str__(self) -> str:
        """Return a string representation of the unit."""
        return f"{self.name} (Health: {self.health})"


# Subclasses for specific unit types
class Footman(Unit):
    """Represents a Footman unit with specific attributes."""
    def __init__(self, name: str):
        super().__init__(name="Footman", cost=1, health=1, hit_threshold=5)


class Archer(Unit):
    """Represents an Archer unit with specific attributes."""
    def __init__(self, name: str):
        super().__init__(name="Archer", cost=2, health=1, hit_threshold=4)


class Knight(Unit):
    """Represents a Knight unit with specific attributes."""
    def __init__(self, name: str):
        super().__init__(name="Knight", cost=3, health=2, hit_threshold=3)


class SiegeMachine(Unit):
    """Represents a Siege Machine unit with specific attributes."""
    def __init__(self, name: str):
        super().__init__(name="Siege Machine", cost=10, health=3, hit_threshold=3)

    def roll_attack(self) -> int:
        """
        Rolling two dice for the unit's attack.

        Returns:
            int: The total number of hits scored by the unit.

        TODO:
        - Roll two dice instead of one. Use a loop or roll twice manually.
        - Count how many rolls are greater than or equal to `hit_threshold` and return that count.
        - Use `random.randint(1, 6)` to simulate rolling a six-sided die.
        """
        # Remove the `return 0` statement and implement the two-dice attack logic.
        count = 0
        for i in range(2):
            roll = random.randint(1, 6)
            if roll >= self.hit_threshold:
                count+=1

        return count


class Player:
    """
    Represents a player in the game.
    Attributes:
        name: The name of the player.
        budget: The amount of coins available for recruiting units.
        army: A list of units the player has recruited.
    """

    MaxSiegeUnits = 2  # Maximum number of Siege Machines allowed per player

    def __init__(self, name, budget=100):
        self.name = name
        self.budget = budget
        self.army = []  # List of recruited units
        self.army_type = cycle((SiegeMachine, Archer, Knight, Footman))  # Cycle through unit types

    def recruit_units(self) -> None:
        """
        Randomly recruit units for the player within their budget.
        - Ensure the player doesn't exceed the max allowed Siege Machines.

        TODO:
        - Check the player's remaining budget before adding a unit.
        - If the selected unit is a Siege Machine, ensure the player has not exceeded `MaxSiegeUnits`.
        - Append the unit to `self.army` and deduct the unit's cost from `self.budget`.

        """
        unit_types = [Footman, Archer, Knight, SiegeMachine]
        siege_count = 0

        while self.budget > 0:
            unit_class = random.choice(unit_types)  # Randomly pick a unit type
            unit = unit_class()  # Create an instance of the unit
            if unit.cost <= self.budget:
                # TODO: Remove the `pass` statement and implement:
                # 1. Use isinstance() to check if the unit is an instance of the SiegeMachine class.
                # 1. Logic to skip adding another Siege Machine if `siege_count >= MaxSiegeUnits`.
                # 2. Add the unit to the player's army.
                # 3. Deduct the unit's cost from `self.budget`.
                pass

                self.army.append(unit)
                self.budget -= unit.cost
                if isinstance(unit, SiegeMachine):
                    siege_count += 1

        # Display the player's army composition after recruitment
        unit_counts = self.get_army_composition()
        print(f"\n{self.name}'s Army Composition:")
        for unit_type, count in unit_counts.items():
            print(f"{unit_type}: {count}")

    def get_army_composition(self) -> dict:
        """
        Count and return the number of each type of unit in the army.
        Returns:
            A dictionary with unit types as keys and their counts as values.
        """
        unit_counts = {
            "Footman": sum(1 for unit in self.army if isinstance(unit, Footman)),
            "Archer": sum(1 for unit in self.army if isinstance(unit, Archer)),
            "Knight": sum(1 for unit in self.army if isinstance(unit, Knight)),
            "Siege Machine": sum(1 for unit in self.army if isinstance(unit, SiegeMachine)),
        }
        return unit_counts

    def is_defeated(self) -> bool:
        """
        Check if the player has any units left alive.
        Returns:
            True if all units are dead; False otherwise.
        """
        return all(not unit.isalive() for unit in self.army)

    def attack(self, defender) -> None:
        """
        Simulate the player's attack on the defender.
        - Rolls dice for each unit of the current type in the cycle.
        - Calculates and applies damage to the defender.

        TODO:
        - Loop through `self.army` and roll attack dice for units of the current type.
        - Keep track of the total number of hits and print the results.
        - Call `defender.resolve_damage()` with the total hits.
        """
        print(f"\n{self.name}'s turn to attack!")

        total_hits = 0
        army_type = next(self.army_type)  # Get the current unit type in the cycle

        for unit in self.army:
            if isinstance(unit, army_type) and unit.isalive():
                # TODO: Remove the `pass` statement and implement:
                # 1. Roll attack dice for the unit.
                # 2. Add the resulting hits to `total_hits`.
                # 3. Print the result, e.g., "Knight (Health: 2) scores 1 hit(s)"
                pass  # Students must implement this

        print(f"{self.name} dealt {total_hits} total hits!")
        defender.resolve_damage(total_hits)

    def resolve_damage(self, total_damage: int) -> None:
        """
        Resolve damage by applying it to random units in the army.
        - Units with zero health are removed from the army.
       TODO:
        - While `total_damage > 0`, randomly pick a unit from `self.army` using `random.choice()`.
        - Call `unit.take_damage(1)` for the chosen unit.
        - If the unit's health drops to 0, remove it from the army.
        - Print the name of the unit eliminated (if any).
        """

        print(f"{self.name} receives {total_damage} total damage!")

        while total_damage > 0 and self.army:
            # TODO: Remove the `pass` statement and implement
            # 1. Pick a random unit to apply damage
            # 2. Apply damage to a randomly chosen unit
            pass  # Students must implement this

        # TODO: Remove dead units from the army and print the dead units
        # If the unit's health drops to 0, remove it from the army.
        # Print the name of the unit eliminated (if any), e.g., "Knight has been eliminated"
        # Update the army with the alive units.        
        pass  # Students must implement this

    def __str__(self):
        """
        Return a string representation of the player's army composition.
        """
        unit_counts = self.get_army_composition()
        return (f"{self.name}'s Army\n"
                f"Footmen: {unit_counts['Footman']}, Archers: {unit_counts['Archer']}, "
                f"Knights: {unit_counts['Knight']}, Siege Machines: {unit_counts['Siege Machine']}")


class Risk:
    """Represents the Risk game."""

    def __init__(self, name: str, budget: int = 30):
        self.user = Player(name=name, budget=budget)
        self.computer = Player(name="Computer", budget=budget)

        # Recruit units for both players
        self.user.recruit_units()
        self.computer.recruit_units()

        # Display initial armies
        print("\nInitial Armies:")
        print(self.user)
        print(self.computer)

    def play(self) -> None:
        """
        Simulate the battle between the user and the computer until one is defeated.
        """
        while not self.user.is_defeated() and not self.computer.is_defeated():
            # User attacks first
            self.user.attack(self.computer)
            if self.computer.is_defeated():
                print("\nComputer is defeated! You win!")
                break

            # Computer's turn to attack
            self.computer.attack(self.user)
            if self.user.is_defeated():
                print("\nYou are defeated! Computer wins!")
                break

        # Display final armies
        print("\nFinal Armies:")
        print(self.user)
        print(self.computer)


def test():
    hulk = Footman("Bruce Banner")
    blackwidow = Archer("Natasha Romanova")
    batman = Knight("Bruce Wayne")

    units = (hulk, blackwidow, batman)

    for _ in range(5):
        for unit in units:
            hit = unit.roll_attack()
            print(f"{unit} scores {hit} hit(s)")

    for _ in range(2):
        for unit in units:
            unit.take_damage(1)
            print(f"{unit} is still alive." if unit.isalive() else f"{unit} is dead.")


def main():
    """
    Entry point for the game. Initialize and start the Risk game.
    """
    print("\n=======================")
    print("     Welcome to Risk!    ")
    print("=======================\n")

    game = Risk("Dr. Baek, the legendary pirate captain")
    game.play()


# Run the game
if __name__ == "__main__":
    #main()
    test()
