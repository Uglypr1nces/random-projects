import random
import pyttsx3

# Initialize the pyttsx3 engine before the loop
engine = pyttsx3.init()

list_of_ideas = ["to-do list", "simple quiz game", "hangman", "currency converter"]

while True:
    idea = random.choice(list_of_ideas)
    engine.say(idea)
    engine.runAndWait()  # Ensure that the TTS speech is completed before continuing

    choice = input("Are you satisfied? (yes/no): ").strip().lower()
    if choice == "yes":
        break
    elif choice == "no":
        print("Okay, let me suggest another idea.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Don't forget to close the pyttsx3 engine when done
engine.stop()
engine.quit()
