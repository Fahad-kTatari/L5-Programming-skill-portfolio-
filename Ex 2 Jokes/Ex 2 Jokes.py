import random
import tkinter as tk
from tkinter import messagebox

# Function to load jokes from the file
def load_jokes(filename):
    try:
        with open(filename, 'r') as file:
            jokes = [line.strip().split('?') for line in file if '?' in line]
            # Ensure each joke has a setup and punchline
            jokes = [joke for joke in jokes if len(joke) == 2]
        return jokes
    except FileNotFoundError:
        messagebox.showerror("Error", "The joke file was not found.")
        return []
    except IOError:
        messagebox.showerror("Error", "Could not read the joke file.")
        return []

# Function to display a random joke
def tell_joke():
    if jokes:
        joke = random.choice(jokes)
        setup, punchline = joke[0], joke[1]
        # Display setup in message box and punchline after pressing OK
        messagebox.showinfo("Joke Setup", setup + "?")
        messagebox.showinfo("Punchline", punchline)
    else:
        messagebox.showwarning("Warning", "No jokes available.")

# Main program window
def main():
    global jokes
    jokes = load_jokes('randomJokes.txt')
    
    root = tk.Tk()
    root.title("Joke Teller")
    root.geometry("300x200")

    # Button to display joke
    joke_button = tk.Button(root, text="Tell me a joke", command=tell_joke, font=("Arial", 14))
    joke_button.pack(pady=50)

    # Button to quit
    quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 14))
    quit_button.pack(pady=10)

    root.mainloop()

# Start the program
if __name__ == "__main__":
    main()
