import pyttsx3
import datetime
import random
from playsound import playsound
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] ='1'
import pygame

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the engine
engine.setProperty('rate', 150)  # Set the speaking rate to 150 words per minute
engine.setProperty('volume', 1)  # Set the speaking volume to 100%

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Jokes list
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
]

# Function to tell a joke
def tell_joke():
    while True:
        joke = random.choice(jokes)
        speak(joke)
        response = input("Do you want to hear another joke? (yes/no): ").lower()
        if response != 'yes':
            break

# Function to play a song
def play_song():
    from playsound import playsound
    # Dictionary of song names and their file paths
    song_dict = {
        "Apna Bana Le": "C:\\Users\Admin\\Music\\Apna-Bana-Le(PagalWorld).mp3",
        "Kesariya": "C:\\Users\\Admin\\Music\\Kesariya(PagalWorld).mp3",
        "Kabira": "C:\\Users\\Admin\\Music\\Re-Kabira-Manja(PagalWorld).mp3",
        "Tere Hawale": "C:\\Users\\Admin\\Music\\Tere Hawaale(PagalWorld.cm).mp3",
        # Add more songs here
    }

    pygame.mixer.init()
    current_song = None

    while True:
        if current_song is None:
            # If no song is currently playing, offer song choices to the user
            print("Choose a song to play (or 'q' to quit):")
            for i, song_name in enumerate(song_dict.keys()):
                print(f"{i + 1}. {song_name}")

            choice = input("Enter the number of the song you want to play: ")

            if choice == 'q':
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(song_dict):
                    song_name = list(song_dict.keys())[choice - 1]
                    current_song = song_dict[song_name]
                    pygame.mixer.music.load(current_song)
                    pygame.mixer.music.play()
                    print(f"Now playing: {song_name}")
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
        else:
            # If a song is currently playing, give the option to stop it or change to another song
            print("Options:")
            print("1. Stop the current song")
            print("2. Change to another song")
            print("3. Quit")

            option = input("Enter your choice: ")

            if option == '1':
                pygame.mixer.music.stop()
                print("Song stopped.")
                current_song = None
            elif option == '2':
                pygame.mixer.music.stop()
                current_song = None
            elif option == '3':
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")

# Function for the Rock-Paper-Scissors game
def rock_paper_scissors():
    speak("Let's play Rock, Paper, Scissors! Choose one: rock, paper, or scissors.")
    choices = ['rock', 'paper', 'scissors']
    user_choice = input().lower()
    while user_choice not in choices:
        speak("Invalid choice. Please choose either rock, paper, or scissors.")
        user_choice = input().lower()

    computer_choice = random.choice(choices)
    speak(f"You chose {user_choice}. The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        speak("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            speak("Computer wins! Paper beats rock.")
        else:
            speak("You win! Rock beats scissors.")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            speak("Computer wins! Scissors beats paper.")
        else:
            speak("You win! Paper beats rock.")
    else:  # user_choice == 'scissors'
        if computer_choice == 'rock':
            speak("Computer wins! Rock beats scissors.")
        else:
            speak("You win! Scissors beats paper.")

# Welcome message
speak("Welcome to RoboSpeaker 1.0 Created by Chetan..")
speak("How May I help You? Type Here what you want me to speak")

# Define the command dictionary
commands = {
    'stop': "Thank You! Bye",
    '1': "I want water.",
    '2': "I want lunch.",
    '3': "I want Medicine.",
    '4': "I want Tea.",
    '5': "I want Breakfast.",
    '6': "I am busy now.",
    '7': "I want cold drinks.",
    'joke': tell_joke,
    'song': play_song,
    'game': rock_paper_scissors,
}

# Run the engine in a loop until the user enters 'stop'
while True:
    text = input("Enter the text you want the robo speaker to say (or enter 'stop' to exit): ")

    # Use the dictionary.get() method to get the corresponding command or response
    command_or_response = commands.get(text.lower())
    if command_or_response is not None:
        # If the input is a function, execute it; otherwise, it's a response, so speak it.
        if callable(command_or_response):
            command_or_response()
        else:
            speak(command_or_response)


    else:
        speak(text)
