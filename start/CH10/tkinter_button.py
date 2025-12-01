# Seconder tkinter script
# Add a button and command
# First tkinter script
# Create by 
# Import tkinter
import tkinter

def button_clicked():
    tkinter.Label(
        root,
        text = "Button was clicked"
    ).pack()
    
# Create the GUI main window
root = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(
    root,
    text = "Hello World", 
    font = ("Arial Bold", 50)
    )
my_label.pack()
my_button = tkinter.Button(
    root, 
    text = "Click Me", 
    command = button_clicked
    )
my_button.pack()

# Enter the main event loop
root.mainloop()
