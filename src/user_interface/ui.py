import tkinter as tk
from tkinter import scrolledtext

from ..answer_pipeline.run_answer_pipeline import run_answer_pipeline

class ChatUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat UI")
        self.root.geometry("400x500")
        
        self.create_widgets()
        self.user_message = ''
        
    def create_widgets(self):
        # Create chat box
        self.chat_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create message entry field
        self.entry_field = tk.Entry(self.root, width=80)
        self.entry_field.pack(padx=10, pady=10, fill=tk.X)
        self.entry_field.bind("<Return>", self.send_message)
        
        # Create send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self, event=None):
        self.user_message = self.entry_field.get()
        
        if self.user_message:
            self.display_message("You", self.user_message)
            self.entry_field.delete(0, tk.END)
            self.root.after(100, self.bot_response)  # Schedule bot_response after a short delay

    def display_message(self, sender, message):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.yview(tk.END)

    def bot_response(self):
        response = run_answer_pipeline(self.user_message)
        self.display_message("Bot", response)

    def run(self):
        self.root.mainloop()
