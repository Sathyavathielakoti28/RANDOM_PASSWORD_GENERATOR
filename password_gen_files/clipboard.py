from tkinter import messagebox


def copy_password(root, password):
    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Success",
        "Password copied to clipboard!"
    )