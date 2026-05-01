git init
git add .
git commit -m "Initial commit - testing code"
git remote add origin https://github.com/Girigmua/mi-workspace.git
git branch -M main
git push -u origin main

print("In the world of Eventaria you can choose from 4 different paths, each leading to a unique adventure. Each path will have its own story and challenges to overcome. You can choose to explore the mystical Forest of Elevaria, delve into the Cavernous depths, enter the grand Castle Demetreski, or soar into the Sky realm. Each path will offer a different experience and set of challenges, so choose wisely and enjoy your adventure in Eventaria!")
print()
name = input("What is your name? ")
def welcome():
    print(f"Welcome, {name} to Eventaria !")
print()
print("Choose a random path to begin your adventure.")


def choose_path():
    paths = {
        1: "Forest of Elevaria",
        2: "Cavernous depths",
        3: "Castle Demetreski",
        4: "Sky realm",
    }

    while True:
        choice = input("Choose a path (1-4): ")

        if not choice.isdigit():
            print("Please type a whole number, like 3.")
            continue

        choice = int(choice)

        if choice < 1 or choice > 4:
            print("The number must be between 1 and 4.")
            continue

        print()
        print("Path chosen:")
        print(paths[choice])
        print()

        if choice == 1:
            print("You step into a quiet forest where glowing flowers light your way.")
        elif choice == 2:
            print("You descend into dark caverns filled with ancient secrets.")
        elif choice == 3:
            print("You enter a grand castle where the king awaits your arrival.")
        else:
            print("You soar above the clouds into the sky realm of the goddess race.")

        print("You've made your choice, and your adventure begins!")
        input("Press Return to continue...")

        if choice == 1:
            print("In the forest, you find a faerie who offers you a quest to find an artifact that may save the faerie race and in return, she will grant you a powerful spell or weapon of your choice.")
            print("You accept the quest and venture into the glades of Elevaria,")
        
        
        break
    print("To be continued...")
 

def main():
    welcome()
    choose_path()
    print("Thanks for playing! Theres more to come.")


if __name__ == "__main__":
    main()
