# First tkinter script
# Create by 

# Import tkinter
import tkinter

# Create the GUI main window
root = tkinter.Tk()

# Add widgets
my_label = tkinter.Label(
    root,
    text = "Hello World", 
    font = ("Arial Bold", 50)
    )
my_label.pack()

# Enter the main event loop
root.mainloop()
