from tkinter import Tk, ttk
from tkinter import * 

from PIL import Image, ImageTk

import requests
import json
 
#colors
cor0 = "#FFFFFF"   #White
cor1 = "#333333"     #black
cor2 = "#0000FF"   #blue
cor3 = "#006400"   #green

window = Tk()
window.geometry('300x380')
window.title('Converter')
window.configure(bg=cor1)
window.resizable(height= FALSE,width=FALSE)

#frame

top = Frame(window,width=300,height=90,bg=cor2)
top.grid(row=0,column=0)

main= Frame(window,width=300,height=380,bg=cor0)
main.grid(row=1,column=0)

def convert():
    url = "https://currency-converter241.p.rapidapi.com/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()


    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	    "x-rapidapi-key": "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61",
        "x-rapidapi-host": "currency-converter241.p.rapidapi.com"
    }

    response = requests.request("GET",url, headers=headers, params=querystring)


    data = json.loads(response.text)
    
    total_amount = data["total"]
    formatted = "{:,.2f}".format(total_amount)

    result['text'] = formatted
 
    print(formatted)

    

#top frame

app_name = Label(top,text="Currecny Converter",height=2,padx=20, pady=15,anchor="center",font=('Time 20 bold'),bg=cor2,fg=cor0)
app_name.place(x= 0 , y = 0)

#main frame
result = Label(main,text=" ",width=16,height=2,relief="solid",pady=7,anchor="center",font=('Ivy 15 bold'),bg=cor0,fg=cor1)
result.place(x=50,y=10)
currency = ['CAD', 'BRL','INR','USD','EUR','KWD','BHD','OMD','JOD','CHF','IDR',]

from_label= Label(main,text="From",width=8,height=1,relief="flat",pady=0,padx=0, anchor="nw",font=('Ivy 10 bold'),bg=cor0,fg=cor1)
from_label.place(x=48, y = 90)
combo1 = ttk.Combobox(main,width=8, justify=CENTER,font=('Ivy 12  bold'))
combo1['value'] =  (currency)
combo1.place(x=50,y=115)


to_label= Label(main,text="To",width=8,height=1,relief="flat",pady=0,padx=0, anchor="nw",font=('Ivy 10 bold'),bg=cor0,fg=cor1)
to_label.place(x=158, y = 90)
combo2 = ttk.Combobox(main,width=8, justify=CENTER,font=('Ivy 12  bold'))
combo2['value'] =  (currency)
combo2.place(x=160,y=115)

value= Entry(main, width=22,justify=CENTER,font=("ivy 12 bold"),relief=SOLID)
value.place(x=50,y=155)

button = Button(main, text="Click to Convert", width=19,padx=5,height=1,bg=cor3,fg=cor0,font=("ivy 12 bold"),command=convert) 
button.place(x=50,y=210)


window.mainloop()