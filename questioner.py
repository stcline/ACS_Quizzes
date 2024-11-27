# This script is a quiz game that asks the user questions about cetacians.

# Import the necessary modules
import os
import random
import keyboard
import time
from questions import gray_whale_quiz

# Define the functions

def select_question_bank():
    print("Select a question bank:")
    print("1. Gray Whale Quiz")
    # print("2. Humpback Whale Quiz")
    # print("3. Blue Whale Quiz")
    # print("4. Sperm Whale Quiz")
    # print("5. Beluga Whale Quiz")
    # print("6. Killer Whale Quiz")
    # print("7. All Whale Quiz")
    print("9. Exit")
    while True:
        key = keyboard.read_key()
        time.sleep(.2)
        if key == '1':
            return gray_whale_quiz
        # elif key == '2':
        #     return humpback_whale_quiz
        # elif key == '3':
        #     return blue_whale_quiz
        # elif key == '4':
        #     return sperm_whale_quiz
        # elif key == '5':
        #     return beluga_whale_quiz
        # elif key == '6':
        #     return killer_whale_quiz
        # elif key == '7':
        #     return all_whale_quiz
        # elif key == '8':
        #     return custom_quiz
        elif key == '9':
            return None
        else:
            print("Invalid selection. Please try again.")

def ask_question(question, answer):
    print(question)
    print("\nPress SPACE to reveal the answer...")
    keyboard.wait('space')
    print(f"\nAnswer: {answer}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz(quiz):
    correct = 0
    total = 0
    quiz = quiz

    try:
        while True:
            question, answer = random.choice(list(quiz.items()))
            ask_question(question, answer)
            
            print("Did you get it right? (Press 'y' for yes or 'n' for no)")
            while True:
                key = keyboard.read_key()
                if key.lower() == 'y':
                    time.sleep(.2)
                    clear_screen()
                    correct += 1
                    total += 1
                    break
                elif key.lower() == 'n':
                    time.sleep(.2)
                    clear_screen()
                    total += 1
                    break
            
            print(f"\nCurrent score: {correct}/{total} correct")
            
            print("\nDo you want another question? (Press 'y' for yes or 'n' for no)")
            while True:
                key = keyboard.read_key()
                if key.lower() == 'y':
                    clear_screen()
                    break
                elif key.lower() == 'n':
                    percentage = (correct / total) * 100 if total > 0 else 0
                    print(f"\nQuiz ended. Final score: {correct}/{total} correct ({percentage:.2f}%)")
                    time.sleep(3)
                    print("Thank you for participating!")
                    time.sleep(3)
                    return

    except Exception as e:
        print(f"An error occurred: {e}")
        print("The quiz will now exit.")

    print("Quiz ended. Thank you for participating!")
    time.sleep(3)

# Run the quiz
if __name__ == "__main__":
    quiz = select_question_bank()
    if quiz is None:
        print("Quiz exited.")
        time.sleep(3)
        exit()
    print("Welcome to the Gray Whale Quiz!")
    print("Press SPACE after each question to see the answer.\n")
    time.sleep(2)
    run_quiz(quiz) 