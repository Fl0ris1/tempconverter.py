from tkinter import *
import tkinter.font as font

def tempconverter():
    temp_cel=input_celcius.get()
    if temp_cel.replace(".","",1).isdigit():
        lbl_error.place_forget()
        farenheit=(float(temp_cel)*9/5)+32
        lbl_output.config(text="The temperature in farenheit is {}".format(farenheit))
    else:
        lbl_error.place(x=325,y=80)


root=Tk()
font1=font.Font(family="consolas",weight="bold")

root.geometry("500x250")
root.title("Temp Converter")
root.config(background="#99C2A2")

lbl_heading=Label(root,text="Celcius --> Farenheit", font=(font1,15),bg="#99C2A2",fg="#32908F")

lbl_heading.place(x=150,y=15)
#frame=Frame(root)
#frame.pack(pady=20)

lbl_input=Label(root,text="Insert your desired temperature in celcius:", font=(font1,12),bg="#99C2A2",fg="#12664F")
lbl_input.place(x=20,y=60)

input_celcius=Entry(root)
input_celcius.place(x=325,y=63)

lbl_error=Label(root,text="Please enter a valid input",font=(font1,8),bg="#99C2A2",fg="red")

lbl_output=Label(root,font=(font,12),bg="#99C2A2",fg="#000000")
lbl_output.place(x=150,y=100)

convert=Button(root,text="Convert temperature",font=(font1,12),bg="#537A5A",fg="#B1DDF1",padx=20,pady=10,command=tempconverter)
convert.place(x=160,y=130)
root.mainloop()