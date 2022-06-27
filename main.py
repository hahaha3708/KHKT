import tkinter as tk

window = tk.Tk()
# greeting = tk.Label(text="Hello, me")
# greeting.pack()
# make a window
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=50,
    height=20
)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
label.place(x=0, y=0)
button.place(x=20, y=20)
window.mainloop()
