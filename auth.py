from tkinter import *
import os


def destroyPackWidget(parent):
    for e in parent.pack_slaves():
        e.destroy()


def register():
    global register_screen, username, phone, password
    global username_entry, phone_entry, password_entry

    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x300")

    username = StringVar()
    phone = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter the details below", bg="blue", fg="white").pack(pady=10)

    Label(register_screen, text="Username").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    Label(register_screen, text="Phone Number").pack()

    # Validate phone number to accept only 10 digits
    def validate_phone(P):
        return P.isdigit() and len(P) <= 10

    vcmd = register_screen.register(validate_phone)
    phone_entry = Entry(register_screen, textvariable=phone, validate="key", validatecommand=(vcmd, "%P"))
    phone_entry.pack()

    Label(register_screen, text="Password").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Button(register_screen, text="Register", width=10, height=1, bg="blue", fg="white", command=register_user).pack(pady=10)


def register_user():
    username_info = username.get()
    phone_info = phone.get()
    password_info = password.get()

    # Final phone number check (length must be 10)
    if len(phone_info) != 10:
        Label(register_screen, text="Phone number must be 10 digits", fg="red").pack()
        return

    with open(username_info, "w") as file:
        file.write(username_info + "\n")
        file.write(phone_info + "\n")
        file.write(password_info)

    username_entry.delete(0, END)
    phone_entry.delete(0, END)
    password_entry.delete(0, END)

    show_thank_you_screen()


def show_thank_you_screen():
    destroyPackWidget(register_screen)
    Label(register_screen, text="Thanks! Registration Successful", fg="green", font=("Calibri", 14)).pack()
    Button(register_screen, text="Go to Login", command=register_screen.destroy).pack(pady=10)


def login():
    global login_screen, username_verify, password_verify
    global username_login_entry, password_login_entry

    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Please enter login details").pack(pady=10)

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Button(login_screen, text="Login", width=10, height=1, bg="green", fg="white", command=login_verify).pack(pady=10)


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    try:
        with open(username1, "r") as file:
            lines = file.read().splitlines()
            if password1 == lines[2]:
                login_success()
            else:
                invalid_password()
    except FileNotFoundError:
        user_not_found()


def login_success():
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x100")
    Label(login_success_screen, text="Login Successful").pack()
    Button(login_success_screen, text="OK", command=login_success_screen.destroy).pack()


def invalid_password():
    pw_screen = Toplevel(login_screen)
    pw_screen.title("Error")
    pw_screen.geometry("200x100")
    Label(pw_screen, text="Invalid Password").pack()
    Button(pw_screen, text="OK", command=pw_screen.destroy).pack()


def user_not_found():
    nf_screen = Toplevel(login_screen)
    nf_screen.title("Error")
    nf_screen.geometry("200x100")
    Label(nf_screen, text="User Not Found").pack()
    Button(nf_screen, text="OK", command=nf_screen.destroy).pack()


def main_account_screen():
    global root
    root = Tk()
    root.title("Healthcare Chatbot - Login/Register")
    root.geometry("300x250")

    Label(root, text="Welcome to HealthBot", bg="skyblue", width="300", height="2", font=("Calibri", 14)).pack(pady=10)
    Button(root, text="Login", height="2", width="30", bg="lightgreen", command=login).pack(pady=5)
    Button(root, text="Register", height="2", width="30", bg="lightblue", command=register).pack(pady=5)

    root.mainloop()


# Start the app
main_account_screen()
