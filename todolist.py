import tkinter as tk
from tkinter import messagebox, font

class todolist:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Vibrant To-Do List 🎉")
        self.root.geometry("450x400")
        self.root.config(bg="#282c34")

        self.tasks = []

        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.list_font = font.Font(family="Helvetica", size=12)

        self.title_label = tk.Label(
            root, text="Your To-Do List", 
            bg="#282c34", fg="#61dafb", font=self.title_font
        )
        self.title_label.pack(pady=(15, 5))

        entry_frame = tk.Frame(root, bg="#282c34")
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, width=30, font=self.list_font)
        self.task_entry.grid(row=0, column=0, padx=(0,10), ipady=6)

        self.add_btn = tk.Button(
            entry_frame, text="Add Task", width=12, 
            bg="#61dafb", fg="#282c34", font=self.button_font,
            activebackground="#21a1f1", activeforeground="white",
            command=self.add_task
        )
        self.add_btn.grid(row=0, column=1)

        list_frame = tk.Frame(root)
        list_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            list_frame, width=45, height=12, font=self.list_font,
            yscrollcommand=self.scrollbar.set,
            bg="#20232a", fg="#61dafb", selectbackground="#21a1f1",
            selectforeground="white", relief=tk.FLAT, bd=0
        )
        self.listbox.pack()

        self.scrollbar.config(command=self.listbox.yview)

        self.del_btn = tk.Button(
            root, text="Delete Selected Task", width=20,
            bg="#e06c75", fg="white", font=self.button_font,
            activebackground="#be5046", activeforeground="white",
            command=self.delete_task
        )
        self.del_btn.pack(pady=15)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "You must enter a task.")
        else:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = todolist(root)
    root.mainloop()
