from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def search():
    """Search for username and password assosiacted with website."""
    
    # Get the website name from the user input
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No details for the website exists.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the website {website} exists.")

# Password generator
def password_generator():
    """Generate a random password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List comprehension to generate different types of characters
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the different types of characters to form the password list, then shuffle it
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list) # Join the list into a string
    password_entry.insert(0, password) # Populate the password field
    pyperclip.copy(password) # Copy the password to the clipboard


# Save data to file
def find_password():
    """Write the password to a .txt file."""
    
    # Get entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Check if entries are valid
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ops!", message="Do not leave any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
            # Reading from the file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # If file not found, create it and save the new data
                json.dump(new_data, data_file, indent=4)
        else:
             # If file exists, update the data with new information
            data.update(new_data)
            # Open file again and save the updated data to the JSON file
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Always clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=21)
website_entry.focus() # Cursor will start at this entry field
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, "john@example.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass_btn = Button(text="Generate Password", command=password_generator)
gen_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=find_password)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(row=1, column=2)



# Start event listener
window.mainloop()