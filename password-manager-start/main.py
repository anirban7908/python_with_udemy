from tkinter import * # type: ignore
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip # type: ignore
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

     

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error", message="Please provide all the details to continue!")
        return
    
    is_okay = messagebox.askokcancel(
        title=website,
        message=f"Here are details entered: \n Email: {username}, \n Password: {password} \n Do you want tpo save them?",
    )

    if is_okay:
        with open("password_manager.txt", mode="a") as file:
            file.write(f"{website} | {username} | {password}\n")

            messagebox.showinfo(
                title="Success",
                message="Your credentials have been saved successfully!",
            )

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Create canvas
canvas = Canvas(width=200, height=200)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=0, column=1)

# Input label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)


# Input
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="ew")
username_input.insert(0, "example@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")


# Password generator button
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2, sticky="ew")

website_input_val = website_input.get()
username_input_val = username_input.get()
password_input_val = password_input.get()

add_new_entry = Button(text="Add", width=36, command=save_password)
add_new_entry.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
