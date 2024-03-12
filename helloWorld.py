import random


def guessgame():
    guess = 0
    max = 100
    min = 0
    answer = random.randrange(0, 100)
    count = 0

    while guess != answer:
        guess = int(input("Please input a number  : "))

        count += 1
        if guess > answer:
            max = guess
            print("The answer is between", min, "and", max)
        elif guess < answer:
            min = guess
            print("The answer is between", min, "and", max)
        else:
            print("You win!")
            print("Total guess: ", count)
            return count


def main():
    print()
    print("Hello World! Git awesome!")
    print("Python changes your lives.")
    print("Input 0~100 Number can Test your luck index today!")
    print()
    guessgame()
   

if __name__ == "__main__":
    main()






