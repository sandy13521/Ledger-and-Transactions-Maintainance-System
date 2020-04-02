from tkinter import *
import tkinter.ttk as table
import webbrowser as web
import people
import dashboard

def change_frame(frame, name, prev = "None"):
    global window, people_button, transactions_button
    frame.destroy()
    if name == "Dashboard":
        if prev == "People":
            people_button.config(text = "People", command = lambda: change_frame(frame, "People"))
    elif name == "People":
        people_button.config(text = "Dashboard", command = lambda: change_frame(frame, "Dashboard", "People"))
        frame = people.get_frame(window)
        frame.pack(side = TOP)

# This method adds the menu to the program.
def add_menu(window):
    menu = Menu(window)
    window.config(menu = menu)

    files_menu = Menu(menu)
    help_menu = Menu(menu)

    files_menu.add_command(label = "Settings", command = print("#"))
    files_menu.add_separator()
    files_menu.add_command(label = "Exit", command = window.quit)

    about_menu = Menu(help_menu)
    about_menu.add_command(label = "Sandeep N S", command = lambda: web.open("https://www.linkedin.com/in/sandeep-n-s-6b3888165/"))
    about_menu.add_command(label = "Suprad S Parashar", command = lambda: web.open("https://www.linkedin.com/in/supradparashar/"))

    help_menu.add_cascade(label = "About", menu = about_menu)

    menu.add_cascade(label = "File", menu = files_menu)
    menu.add_cascade(label = "Help", menu = help_menu)

# Main Logic of the function

window = Tk()
window.title("Ledger and Transactions Maintainance System")
add_menu(window)
frame = dashboard.get_frame(window)
frame.pack(side = TOP)
navigation_frame = Frame(window)
people_button = Button(navigation_frame, text = "People", command = lambda: change_frame(frame, "People"))
transactions_button = Button(navigation_frame, text = "Transactions")
quit_button = Button(navigation_frame, text = "Quit", command = window.quit)
people_button.pack(side = LEFT)
transactions_button.pack(side = LEFT)
quit_button.pack(side = LEFT)
navigation_frame.pack(side = BOTTOM)
window.mainloop()