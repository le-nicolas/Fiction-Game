#A basic adventure game where players navigate through text-based scenarios and make decisions.
import random

def print_intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can explore different locations and encounter various creatures.")
    print("Type 'help' to see a list of commands.")

def print_help():
    print("Available commands:")
    print(" - explore: Explore the current area.")
    print(" - north, south, east, west: Move in the specified direction.")
    print(" - attack: Attack a creature if you encounter one.")
    print(" - run: Run away from a creature.")
    print(" - quit: Quit the game.")

def explore():
    encounter = random.choice(["nothing", "creature"])
    if encounter == "nothing":
        print("You explore the area and find nothing of interest.")
    else:
        creature = random.choice(["goblin", "wolf", "troll"])
        print(f"You encounter a {creature}!")
        return creature
    return None

def attack(creature):
    if creature:
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print(f"You bravely fight the {creature} and win!")
            return True
        else:
            print(f"You fight the {creature}, but it overpowers you. You lose.")
            return False
    else:
        print("There is nothing to attack here.")
    return False

def run():
    outcome = random.choice(["escape", "caught"])
    if outcome == "escape":
        print("You manage to run away safely.")
        return True
    else:
        print("You try to run, but the creature catches you. You lose.")
        return False

def main():
    print_intro()
    current_room = "forest"
    creature = None

    while True:
        command = input("> ").strip().lower()
        
        if command == "help":
            print_help()
        elif command == "explore":
            creature = explore()
        elif command in ["north", "south", "east", "west"]:
            print(f"You move {command}.")
            creature = None
        elif command == "attack":
            if creature:
                if attack(creature):
                    creature = None
                else:
                    break
            else:
                print("There is nothing to attack here.")
        elif command == "run":
            if creature:
                if run():
                    creature = None
                else:
                    break
            else:
                print("There is nothing to run from.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see a list of commands.")

if __name__ == "__main__":
    main()
