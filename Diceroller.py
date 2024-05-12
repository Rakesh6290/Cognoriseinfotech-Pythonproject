import random

class DiceRollingSimulator:
    def __init__(self):
        print(" Dice Rolling Simulator!")

    def roll_dice(self, num_sides, num_rolls):
        results = []
        for _ in range(num_rolls):
            roll_result = random.randint(1, num_sides)
            results.append(roll_result)
        return results

    def run(self):
        while True:
            try:
                num_sides = int(input("Enter the number of sides on the dice: "))
                if num_sides <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        while True:
            try:
                num_rolls = int(input("Enter the number of rolls: "))
                if num_rolls <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        results = self.roll_dice(num_sides, num_rolls)
        print(f"\nResults of rolling a {num_sides}-sided dice {num_rolls} times:")
        for i, result in enumerate(results, start=1):
            print(f"Roll {i}: {result}")

        play_again = input("\nDo you want to roll again? (yes/no): ").lower()
        if play_again == "yes":
            self.run()
        else:
            print("Thank you for using the Dice Rolling Simulator!")

def main():
    simulator = DiceRollingSimulator()
    simulator.run()

if __name__ == "__main__":
    main()
