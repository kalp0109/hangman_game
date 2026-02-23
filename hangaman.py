import random
from words import tech_words
from stages import hangman

#Selecting a random words 
def choose_words():
    selected_words = random.choice(tech_words)
    return selected_words
    

def welcome():

    print("Welcome to the Hangman Game!")
    print("We have list of Terms related to: Big Data, Programming, Databases, Cloud & DevOps, Data Engineering")
    print("Lets play!!!")




def play_game():
    welcome()
    selected_words = choose_words()
    total_attempt = len(hangman) - 1   # 🔥 attempts based on stages
    len_of_word = len(selected_words)
    
    display = ["_"] * len_of_word
    guessed_letter = []
    
    print("Word:", " ".join(display))


    
    while total_attempt>0:
        
        print(hangman[total_attempt]) 
        print(f"You have {total_attempt} attempt left!!")
        user_guess = input("Make a guess:").lower()

        if len(user_guess) !=1 or not user_guess.isalpha():
            print("Invalid input! Enter only one alphabet letter.")

            continue

        if user_guess in guessed_letter:
            print("You already guessed this letter!")
            continue
        guessed_letter.append(user_guess)

        found= False
        for index in range(len_of_word):
            if selected_words[index] == user_guess:
                display[index] = user_guess
                found = True
        
        print("Word:", " ".join(display))


        if "_" not in display:
            print(f"Congratulations!! You won with {total_attempt} attempts remaining!")
            return

        if not found:
            print("Wrong letter!, choose again")
            total_attempt-=1
    
    
    print(hangman[0])
    print(f"\n💀 Game Over! The word was '{selected_words}'")


def main():
    while True:
        play_game()
        replay = input("Do you want to play again? :(y/n): ").lower()
        if replay !='y':
            print("Thanks for playing! 👋")
            break   

main()