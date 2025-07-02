import tkinter as tk
from tkinter import messagebox
import json
import random
import os
from datetime import datetime

#File Memory
MEMORY_FILE = "silas_memory.json"

#Colors
COLORS = {
    "bg": "#E6F2F8",
    "button_bg": "#B3D9FF",
    "button_active": "#99CCFF",
    "text": "#003366",
    "output_bg": "#DFF0FF",
}

#Moods
MOODS = {
    "Happy": "😄",
    "Sad": "😢",
    "Angry": "😠",
    "Tired": "😴",
    "Okay": "🙂",
}

#Friendly Messages
JOKES = [
    "Why don’t scientists trust atoms? Because they make up everything! 🤓",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why did the banana go to the doctor? Because it wasn’t peeling well! 🍌",
    "Why can't your nose be 12 inches long? Because then it would be a foot! 👃",
]

HUG_MESSAGES = [
    "Here’s a big warm hug for you! 🤗",
    "Silas sends you a gentle hug. You're awesome! 💙",
    "Whenever you feel down, remember I’m here for you. 🤗",
]

#Number Guessing Game
GAME_ANSWER = random.randint(1, 5)

class SilasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Silas - Your Friendly Companion")
        self.root.geometry("500x520")
        self.root.configure(bg=COLORS["bg"])
        self.memory = self.load_memory()
       
        self.create_widgets()
        
    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return{}
      
    def save_memory(self):
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, indent=2)
        except Exception
            pass
    
    def create_widgets(self):
    
        tk.Label(
            self.root,
            text="Hi! I'm Silas 🤖\nYour Friendly Companion",
            font=("Helvetica", 18, "bold"),
            fg=COLORS["text"],
            bg=COLORS["bg"], 
        ).pack(pady=(10, 20))

        self.last_mood_var = tk.StringVar()
        last_mood_text = "Last time you felt: "
        last_mood = self.memory.get("last_mood")
        if last_mood:
            last_mood_text += f"{last_mood} {MOODS.get(last_mood, '')}"
        else:
            last_mood_text += "No record yet"
        self.last_mood_var.set(last_mood_text)
        tk.Label(
            self.root,
            textvariable=self.last_mood_var,
            font=("Helvetica", 12),
            fg=COLORS["text"],
            bg=COLORS["bg"],
        ).pack(pady=(0, 15))

        mood_frame = tk.Frame(self.root, bg=COLORS["bg"])
        mood_frame.pack(pady=10)

        tk.Label(
            mood_frame,
            text="How are you feeling today?",
            font=("Helvetica", 14),
            fg=COLORS["text"],
            bg=COLORS["bg"],
        ).grid(row=0, column=0, columnspan=5, pady=(0, 10))

        self.mood_buttons = {}
        col = 0
        for mood, emoji in MOODS.items():
            btn = tk.Button(
                mood_frame,
                text=f"{mood} {emoji}",
                font=("Helvetica", 12),
                bg=COLORS["button_bg"],
                activebackground=COLORS["button_active"],
                fg=COLORS["text"],
                width=8,
                command=lambda m=mood: self.handle_mood(m),
            )
            btn.grid(row=1, column=col, padx=5, pady=5)
            self.mood_buttons[mood] = btn
            col += 1
        self.output = tk.Test(
            self.root,
            height=8,
            width=55,
            wrap="word",
            font=("Helvetica", 12),
            bg=COLORS["output_bg"],
            fg=COLORS["text"],
        )
        self.output.pack(pady=15)
        self.output.configure(state="disabled")

        action_frame = tk.Frame(self.root, bg=COLORS["bg"])
        action_frame.pack(pady=10)

        tk.Button(
            action_frame,
            text="Tell me a joke 🤡",
            font=("Helvetica", 12),
            bg=COLORS["button_bg"],
            activebackground=COLORS["button_active"],
            fg=COLORS["text"],
            width=15,
            command=self.tell_joke,
        ).grid(row=0, column=0, padx=5, pady=5)
   
        tk.Button(
            action_frame,
            text="Give me a hug 🤗",
            font=("Helvetica", 12),
            bg=COLORS["button_bg"],
            activebackground=COLORS["button_active"],
            fg=COLORS["text"],  
            width=15,
            command=self.give_hug,
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            action_frame,
            text="Play a game 🎲",
            font=("Helvetica", 12),
            bg=COLORS["button_bg"]
            activebackground=COLORS["button_active"],
            fg=COLORS["text"],
            width=15,
            command=self.start_game,
        ).grid(row=0, column=2, padx=5, pady=5)

        self.game_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.game_frame.pack(pady=10)
        self.game_active = False
        
    def handle_mood(self, mood):
        self.memory["last_mood"] = mood
        self.save_memory()
         
        self.last_mood_var.set(f"Last time you felt: {mood} {MOODS[mood]}")
        response = self.mood_response(mood)
          
        self.display_message(response)
          
        if self.game_active:
            self.end_game()
          
    def mood_response(self, mood):
        responses = {
            "Happy": "Yay! I'm so happy you feel good! 😄",
            "Sad": "I'm here if you're feeling low.  Want to tell me more? 😢",
            "Angry": "It's okay to feel upset sometimes. Let's breathe together. 😠",
            "Tired": "Make sure to rest! Even heroes need naps. 😴",
            "Okay": "Thanks for sharing! I'm here whenever you need me. 🙂",
        )
        return responses.get(mood, "Thanks for telling me how you feel!")
        
    def display_message(self, msg):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", msg)
        self.output.configure(state="disabled")
      
        with open("silas_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n\n")
      
    def tell_joke(self):
        if self.game_active:
            self.end_game()
         
        joke = random.choice(JOKES)
        self.display_message(joke)
         
    def give_hug(self):
        if self.game_active:
            self.end_game()

        hug_msg = random.choice(HUG_MESSAGES)
        self.display_message(hug_msg)

    def start_game(self):
        if self.game_active:
            self.display_message("Game already in progress! Guess a number between 1 and 5.")
            return
        
        self.game_active = True
        self.display_message("I'm thinking of a number between 1 and 5.  Can you guess it? Type your guess below and press Enter!")
        
        self.guess_entry = tk.Entry(self.game_frame, font=("Helvetica", 12), width=10)
        self.guess_entry.pack(side="left", padx=(0, 5))
        self.guess_entry.focus()
        
        self.guess_entry.bind("<Return>", self.check_guess)
       
        self.guess_submit_btn = tk.Button(
            self.game_frame,
            text="Guess",
            font=("Helvetica", 12),
            bg=COLORS["button_bg"],
            activebackground=COLORS["button_active"],
            fg=COLORS["text"],
            command=self.check_guess,
        )
        self.guess_submit_btn.pack(side="left")
    
    def check_guess(self, event=None):
        guess = self.guess_entry.get().strip()
        if not guess.isdigit():
            messagebox.showinfo("Oops!", "Please enter a number between 1 and 5.")
            return
          
        guess_num = int(guess)
        if guess_num < 1 or guess_num >5:
            messagebox.showinfo("Oops!", "Your guess must be between 1 and 5.")
            return
           
        if guess_num == GAME_ANSWER:
            self.display_message("🎉 You got it! Great job! Want to play again? Press 'Play a game'!")
            self.end_game()
        else:
            self.display_message("Nope, try again! Guess a number between 1 and 5.")
          
    def end_game(self):
        self.game_active = False
        self.guess_entry.destroy()
        self.guess_submit_btn.destroy()

if __name__ == "__main__":           
    root = tk.Tk()
    app = SilasApp(root)
    root.mainloop()

 
         
                    