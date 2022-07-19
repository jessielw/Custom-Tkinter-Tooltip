# Custom-Tkinter-Tooltip
Basic Hover Tooltip for Tkinter based off of Tkinter's built in tooltip with the added ability to customize most options

## Install:
`pip install --upgrade Custom-Tooltip`
*https://pypi.org/project/Custom-Tooltip/*

## Uninstall:
`pip uninstall Custom-Tooltip`

## Use:
Example:
```
from custom_hovertip import CustomTooltipLabel
CustomTooltipLabel(anchor_widget=button1, text="This is tooltip text for button1.")
```

Full Example:
```
from tkinter import *
from custom_hovertip import CustomTooltipLabel

top = Tk()
top.title("Test Custom Tooltip")
label = Label(top, text="Place your mouse over buttons")
label.pack()
button1 = Button(top, text="Button 1")
button1.pack()
CustomTooltipLabel(anchor_widget=button1, text="This is tooltip text for button1.")
button2 = Button(top, text="Button 2")
button2.pack()
CustomTooltipLabel(anchor_widget=button2, text="This is tooltip\ntext for button2.", background="grey",
                   foreground="black", width=15, justify=CENTER)
top.mainloop()
```
You only have to define the widget it's anchored to as well as the text. You can see this example under `button1`

## Customization: 
References to the Label Widget:
*https://www.tutorialspoint.com/python/tk_label.htm* and *https://www.pythontutorial.net/tkinter/tkinter-label/*

Options that can be changed are:
`justify, foreground, background, relief, font, wraplength, anchor, border, width, textvariable`

## Pictures:
![image](https://user-images.githubusercontent.com/48299282/179792850-0d8a16fc-f81a-42e2-a791-5b8dca7257d3.png)

![image](https://user-images.githubusercontent.com/48299282/179793011-ef6a7285-2ec0-4f4f-971c-3f81383bd3f4.png)

![image](https://user-images.githubusercontent.com/48299282/179793097-690f7edd-d320-4372-a937-5eeec108d9ba.png)
