import tkinter as tk
    
root = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()
button = tk.Button(text="touch Me")
button.pack()

text = tk.Text()
text.pack()


root.mainloop()  
