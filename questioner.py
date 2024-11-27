import os
import random
import keyboard
import time
from questions import gray_whale_quiz

def ask_question(question, answer):
    print(question)
    print("\nPress SPACE to reveal the answer...")
    keyboard.wait('space')
    print(f"\nAnswer: {answer}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
    correct = 0
    total = 0

    try:
        while True:
            question, answer = random.choice(list(gray_whale_quiz.items()))
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

if __name__ == "__main__":
    print("Welcome to the Gray Whale Quiz!")
    print("Press SPACE after each question to see the answer.\n")
    time.sleep(2)
    run_quiz() 