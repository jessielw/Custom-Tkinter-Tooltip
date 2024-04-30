from idlelib.tooltip import OnHoverTooltipBase
from tkinter import Widget, LEFT, SOLID, Tk, Button, Label, CENTER, TclError


class CustomToolTipBase(OnHoverTooltipBase):
    def __init__(self, anchor_widget, hover_delay=1000):
        super().__init__(anchor_widget=anchor_widget, hover_delay=hover_delay)

    def disable(self):
        try:
            self.anchor_widget.unbind("<Enter>", self._id1)
            self.anchor_widget.unbind("<Leave>", self._id2)
            self.anchor_widget.unbind("<Button>", self._id3)
        except TclError:
            pass

    def enable(self):
        self._after_id = None
        self._id1 = self.anchor_widget.bind("<Enter>", self._show_event)
        self._id2 = self.anchor_widget.bind("<Leave>", self._hide_event)
        self._id3 = self.anchor_widget.bind("<Button>", self._hide_event)

    def showcontents(self):
        raise NotImplementedError("Subclasses must implement the showcontents method")


class CustomTooltipLabel(CustomToolTipBase):
    """Hover tip for the label widget"""

    def __init__(
        self,
        anchor_widget: Widget,
        text,
        hover_delay: int = 800,
        justify=LEFT,
        background="#ffffe0",
        foreground="black",
        relief=SOLID,
        font=None,
        wraplength: int = None,
        anchor=None,
        border=2,
        width: int = None,
        textvariable=None,
    ):
        super(CustomTooltipLabel, self).__init__(
            anchor_widget=anchor_widget, hover_delay=hover_delay
        )
        self.text = text
        self.justify = justify
        self.background = background
        self.foreground = foreground
        self.relief = relief
        self.font = font
        self.wraplength = wraplength
        self.anchor = anchor
        self.border = border
        self.width = width
        self.textvariable = textvariable

    def showcontents(self):
        label = Label(
            self.tipwindow,
            text=self.text,
            justify=self.justify,
            foreground=self.foreground,
            background=self.background,
            relief=self.relief,
            font=self.font,
            wraplength=self.wraplength,
            anchor=self.anchor,
            border=self.border,
            width=self.width,
            textvariable=self.textvariable,
        )
        label.pack()


def example_window():
    """Tkinter root window for testing tool tips"""

    def enable_tip():
        t1.enable()

    top = Tk()
    top.title("Test Custom Tooltip")
    label = Label(top, text="Place your mouse over buttons")
    label.pack()
    button1 = Button(top, text="Button 1", command=enable_tip)
    button1.pack()
    t1 = CustomTooltipLabel(
        anchor_widget=button1, text="This is tooltip text for button1."
    )
    t1.disable()
    button2 = Button(top, text="Button 2")
    button2.pack()
    CustomTooltipLabel(
        anchor_widget=button2,
        text="This is tooltip\ntext for button2.",
        background="grey",
        foreground="black",
        width=15,
        justify=CENTER,
    )
    top.mainloop()


if __name__ == "__main__":
    example_window()
