import tkinter as tk
from threading import Timer
from datetime import datetime

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")

        self.text_area = tk.Text(self.root, wrap=tk.WORD, width=50, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.timer_interval = 5  # Set the timer interval in seconds
        self.last_typing_time = datetime.now()

        self.start_timer()

        self.text_area.bind("<Key>", self.on_key_pressed)

    def start_timer(self):
        self.timer = Timer(self.timer_interval, self.check_typing)
        self.timer.start()

    def reset_timer(self):
        self.timer.cancel()
        self.start_timer()

    def check_typing(self):
        current_time = datetime.now()
        time_difference = (current_time - self.last_typing_time).total_seconds()

        if time_difference >= self.timer_interval:
            self.clear_text()

        self.start_timer()

    def on_key_pressed(self, event):
        self.last_typing_time = datetime.now()
        self.reset_timer()

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
