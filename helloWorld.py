import random


# Initialize variables
def guessgame():
    guess = 0
    guess_max = 100
    guess_min = 0
    # Generate a random number between 0 and 99
    answer = random.randrange(0, 100) 
    count = 0    # Counter for the number of guesses

    # Main game loop 
    while guess != answer:
        # Get user input for the guess
        guess = int(input("Please input a number  : "))
        
        # increment the guess count
        count += 1
        
        # Check if the guess is higher than the answer
        if guess > answer:
            guess_max = guess    # Update the upper bound of the range
            print("The answer is between", guess_min, "and", guess_max)
            
        # Check if the guess is lower than the answer
        elif guess < answer:
            guess_min = guess    # Update the lower bound of the range
            print("The answer is between", guess_min, "and", guess_max)
            
        # The guess is correct    
        else:
            print("You win!")
            print("Total guess: ", count)
            # Check if the player guessed within 3 attempts, show result report
            if count <= 5:
                print("You are very lucky today, the god of luck is by your side")
            else:
                print("You have a good day")
            break  # Exit the loop 

def main():
    # Print introductory messages
    print()
    print("Hello World! Git awesome!")
    print("Python changes your lives.")
    print("Input 0~100 Number can Test your luck index today!")
    print()
    
    # Start the game
    guessgame()
   

if __name__ == "__main__":
    main()






