from tkinter import *

root = Tk()
root.geometry("400x350")
root.resizable(0,0)
root.title('tinh BMI')

font = ("Arial",13)



#chức năng
def calculate(a):
    result_lb['text'] = ''
    valid = True
    try:
        age = int(age_entry.get())
    except:
        valid = False
        result_lb['text'] = 'Error'
        result_lb['foreground'] = 'red'
        
    try:
        num1 = int(weight_entry.get())
        
    except:
        valid = False
        result_lb['text'] = 'Error'
        result_lb['foreground'] = 'red'
    try:
        num2 = int(height_entry.get())/100
    except:
        result_lb['text'] = 'Error'
        result_lb['foreground'] = 'red'
        valid = False
    
    if valid:
        result = num1//(num2*num2)
        if result < 18.5:
            status = 'thiếu cân'
            result_lb['text'] = f'Chi so BMI cua bạn la: {result}, {status}'
            result_lb['fg'] = 'green'
        elif 18.5 <= result <25:
            status = 'bình thường'
            result_lb['text'] = f'Chi so BMI cua bạn la: {result}, {status}'
            result_lb['fg'] = 'green'
        elif 25 < result < 30:
            status = 'thừa cân'
            result_lb['text'] = f'Chi so BMI cua bạn la: {result}, {status}'
            result_lb['fg'] = 'green'
        elif result >30:
            status = 'béo phì'
            result_lb['text'] = f'Chi so BMI cua bạn la: {result}, {status}'
            result_lb['fg'] = 'green'
            
        else:

            result_lb['text'] = 'Lỗi nhập thông tin'
            result_lb['foregound'] = 'red'
    
        
def reset(b):
    num1 = None
    num2 = None
    age_entry.delete(0,'end')
    weight_entry.delete(0,'end')
    height_entry.delete(0,'end')
    result_lb['text'] = ''
    
    

    
    
    

#giao diện
age_lb = Label(root, text =  'Số tuổi',font = font)
age_lb.place(x = 30,y = 20)
age_entry = Entry(root,font = font)
age_entry.place(x = 200,y = 20)

weight_lb = Label(root, text = 'Cân nặng(kg)', font = font)
weight_lb.place(x = 30, y = 60)
weight_entry = Entry(root, font = font)
weight_entry.place(x = 200, y = 60)



height_lb = Label(root, text = 'Chiều cao(cm)', font = font)
height_lb.place(x = 30, y = 140)
height_entry = Entry(root, font = font)
height_entry.place(x = 200, y = 140)

calculatebtn = Button(root, font = font, text = "Tính", width = 20, height  = 3)

calculatebtn.place(x = 10, y = 200)
calculatebtn.bind("<Button-1>", calculate)

resetbtn = Button(root, font = font, text = "Reset", width = 20, height =3)
resetbtn.place(x = 200, y = 200)
resetbtn.bind("<Button-1>", reset)

result_lb = Label(root, font = font, text = '')
result_lb.place(x = 10, y = 275 )


root.mainloop()
