"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# import random


def main():
    score = float(input("Enter score: "))
    print(score_type(score))
#    random.randint(0, 101)


def score_type(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()


