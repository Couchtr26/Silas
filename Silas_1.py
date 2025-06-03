from colorama import Fore, Style, init
import time

int()

def type_text(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        print(color + char + Style.RESET_ALL, end="", flush=True)
        time.sleep(delay)
    print()
    
def ask_question(prompt, color=Fore.WHITE):
    type_text(prompt, color=color)
    return input("> ")

#You can vary your questions here and color they show colors: Red, Green, Blue, Yellow, Cyan, White and Black
#If you want to change question change the start for instance instead of feeling what do you want to do
#Do = ask_question ("What do you want to do?", color=Fore.RED)
#In the type_text and file.write line you would want to take {feeling} out and add {do}
name = ask_question("What is your name?", color=Fore.CYAN)
age = int(ask_question("How old are you?", color=Fore.BLUE))
location = ask_question("Where are you from?", color=Fore.YELLOW)
feeling = ask_question("How are you feeling today?", color=Fore.GREEN)

print()
type_text(f"Nice to meet you, {name}. You're {age}, from {location} and feeling {feeling}.", color=Fore.MAGENTA)

with open("Feeling.txt", "w") as file:
    file.write(f"Nice to meet you, {name}. You're {age}, from {location} and feeling {feeling}.")