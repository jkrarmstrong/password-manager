
# Password Manager App

This app is a simple password manager built with Python and Tkinter. It allows users to generate random passwords, save login credentials (website, email, and password), and search for existing credentials.

## Features:
1. **Generate a Password**: A random password can be generated and copied to the clipboard.
2. **Save Passwords**: Users can save website login credentials (email and password) to a local `data.json` file.
3. **Search for Passwords**: Users can search for saved login details by entering a website name.
4. **GUI**: The app uses Tkinter for a user-friendly graphical interface.

## Requirements:
- `pyperclip` for copying the generated password to the clipboard.
- `json` for saving and retrieving login details.

## How to Use:
1. Open the app.
2. Click **Generate Password** to create a strong password.
3. Enter the website, email, and password, then click **Add** to save the data.
4. Use the **Search** button to find saved credentials by entering the website name.
