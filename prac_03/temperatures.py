"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """ C - Convert Celsius to Fahrenheit\n F - Convert Fahrenheit to Celsius\n Q - Quit"""


def main():
    print(MENU)
    choices()


def choices():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_to_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        choice = wrong_choice()
    print("Thank you.")


def wrong_choice():
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
