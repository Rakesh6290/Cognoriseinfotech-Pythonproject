import tkinter as tk
from tkinter import messagebox

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.master.configure(bg="pink")
        
        self.duration_label = tk.Label(master, text="Enter duration (seconds):", bg="pink")
        self.duration_label.pack()
        
        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer, bg="black", fg="white")
        self.start_button.pack()
        
        self.timer_label = tk.Label(master, text="", bg="pink")
        self.timer_label.pack()
        
        self.is_running = False
        self.remaining_time = 0
        
    def start_timer(self):
        if not self.is_running:
            try:
                duration = int(self.duration_entry.get())
                if duration <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Invalid duration. Please enter a positive integer.")
                return
            
            self.remaining_time = duration
            self.is_running = True
            self.update_timer()
    
    def update_timer(self):
        if self.is_running:
            self.timer_label.config(text=f"Time remaining: {self.remaining_time} seconds")
            if self.remaining_time <= 0:
                self.is_running = False
                self.timer_label.config(text="Time's up!")
            else:
                self.remaining_time -= 1
                self.master.after(1000, self.update_timer)

def main():
    root = tk.Tk()
    CountdownTimerApp(root)
    root.configure(bg="pink")
    root.mainloop()

if __name__ == "__main__":
    main()

