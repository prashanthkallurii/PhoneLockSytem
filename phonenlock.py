import tkinter as tk
from tkinter import messagebox, simpledialog

class PhoneLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Lock & Unlock Management System")

        self.password = "1234"
        self.is_locked = True

        self.lock_button = tk.Button(root, text="Lock Phone", command=self.lock_phone)
        self.unlock_button = tk.Button(root, text="Unlock Phone", command=self.unlock_phone)
        self.change_password_button = tk.Button(root, text="Change Password", command=self.change_password)
        self.status_label = tk.Label(root, text="Phone is locked")

        self.update_button_states()

        self.lock_button.pack(pady=10)
        self.unlock_button.pack(pady=10)
        self.change_password_button.pack(pady=10)
        self.status_label.pack(pady=20)

    def update_button_states(self):
        if self.is_locked:
            self.lock_button.config(state=tk.DISABLED)
            self.unlock_button.config(state=tk.NORMAL)
            self.change_password_button.config(state=tk.DISABLED)
            self.status_label.config(text="Phone is locked")
        else:
            self.lock_button.config(state=tk.NORMAL)
            self.unlock_button.config(state=tk.DISABLED)
            self.change_password_button.config(state=tk.NORMAL)
            self.status_label.config(text="Phone is unlocked")

    def lock_phone(self):
        if self.is_locked:
            messagebox.showinfo("Already Locked", "Phone is already locked.")
        else:
            password_input = simpledialog.askstring("Lock Phone", "Enter password:")
            if password_input == self.password:
                self.is_locked = True
                self.update_button_states()
                messagebox.showinfo("Phone Locked", "Phone has been locked.")
            else:
                messagebox.showerror("Incorrect Password", "Incorrect password entered.")

    def unlock_phone(self):
        if not self.is_locked:
            messagebox.showinfo("Already Unlocked", "Phone is already unlocked.")
        else:
            password_input = simpledialog.askstring("Unlock Phone", "Enter password:")
            if password_input == self.password:
                self.is_locked = False
                self.update_button_states()
                messagebox.showinfo("Phone Unlocked", "Phone has been unlocked.")
            else:
                messagebox.showerror("Incorrect Password", "Incorrect password entered.")

    def change_password(self):
        if not self.is_locked:
            new_password = simpledialog.askstring("Change Password", "Enter new password:")
            if new_password:
                self.password = new_password
                messagebox.showinfo("Password Changed", "Password has been changed successfully.")
        else:
            messagebox.showwarning("Phone Locked", "Please unlock the phone to change the password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneLockApp(root)
    root.mainloop()
