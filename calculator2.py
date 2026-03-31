"""
A simple calculator that can perform basic arithmetic operations.
Author: OpenAI's ChatGPT
"""


def get_numbers():
    """Get numbers from user input."""
    numbers = []
    print("Enter numbers one by one. Type 'done' when finished.")
    while True:
        user_input = input("Enter a number").strip()
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers
    

def main():
    """Main function to run the calculator."""
    print("=" *50 ) 
    print("Welcome to the Simple Calculator!")
    print("=" * 50 ) 
    numbers = get_numbers()

    if len(numbers)==0:
        print("No numbers entered. Exiting.")
        return
    print(f"\n You entered the numbers: {numbers}")
    print("\n What operation would you like to perform?")
    print("1. Add")
    print("2. Multiply")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == '1':
        result = sum(numbers)
        print(f"The sum of the numbers is: {result}")
    elif choice == '2':
        print("Multiplication feature coming soon!")
#OPERATION WILL BE PERFORMED BY OTHERS
#TODO: Tricket to implement this.


if __name__ == "__main__":
    main()
    #     for n in numbers:
    #         result *= n
    #     print(f"The product of the numbers is: {result}")
    # else:
    #     print("Invalid choice. Please enter 1 or 2.")