import sys
import random

sys.stdout.reconfigure(encoding='utf-8')
def roll_dice(sides):
    return random.randint(1, sides)

def get_int(prompt, default=None):
    while True:
        try:
            user_input = input(prompt)
            if user_input == "" and default is not None:
                return default
            return int(user_input)
        except ValueError:
            print("⚠ Invalid input. Please enter a number value .")

def main():
    # Fun Fact (Historical)
    print("🎲 Did you know? The oldest known dice were found in Mesopotamia and date back over 5,000 years! "
          "Ancient civilizations used dice for games and fortune-telling, proving that chance has always been a part of human life.\n")

    print("🎲 Welcome to the Dice Roller! 🎲")

    while True:
        num_dice = get_int("How many dice do you want to roll? ")
        dice_sides = get_int("Enter the number of sides on your dice (default is 6): ", default=6)

        print("\n🎲 Rolling the dice... 🎲\n")
        rolls = [roll_dice(dice_sides) for _ in range(num_dice)]

        print("🎲 Results:", ", ".join(map(str, rolls)))

        again = input("\nRoll again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n💡 Every day is a roll of the dice. Some outcomes are uncertain, but the key is to keep rolling and making the best of what you get! 💪")
            print("\nThanks for playing! 🎲")
            break

if __name__ == "__main__":
    main()
