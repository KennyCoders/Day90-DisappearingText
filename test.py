import tkinter as tk

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")

        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus_set()

        self.timer_id = None
        self.start_timer()

        self.text_area.bind("<KeyPress>", self.reset_timer)
        self.text_area.bind("<KeyRelease>", self.check_typing)

    def reset_timer(self, event=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.start_timer()

    def check_typing(self, event=None):
        if not self.text_area.get("1.0", "end-1c"):
            self.reset_timer()

    def start_timer(self):
        self.timer_id = self.root.after(5000, self.delete_text)

    def delete_text(self):
        self.text_area.delete(1.0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    app.run()