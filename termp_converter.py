from tkinter import *

root=Tk()

root.geometry("500x250")
root.title("Temp Converter")
root.config(background="#99C2A2")
lbl_heading=Label(root,text="Celcius --> Farenheit", font=("consolas",15,"bold"),bg="#99C2A2",fg="#32908F")

lbl_heading.pack()
frame=Frame(root)
frame.pack(pady=20)


lbl_input=Label(frame,text="Insert your desired temperature in celcius:", font=("consolas",10,"bold",),bg="#99C2A2",fg="#12664F")
lbl_input.grid(row=0,column=0)

input_celcius=Entry(frame)
input_celcius.grid(row=1,column=0)

lbl_error=Label(frame,text="Please enter a valid input",font=("consolas",8,"bold"),bg="#99C2A2",fg="red")


root.mainloop()