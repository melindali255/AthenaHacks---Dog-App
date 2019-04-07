'''
Authors:
    Anna Salieva
    Melinda Li
    Sabrina Thiem
    
API from Dog CEO
'''

import tkinter
from PIL import ImageTk,Image
import Dog_Image

_DEFAULT_FONT = ('Helvetica', 20)

class DogApp:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._create_button()

        self._root_window.minsize(600,600)
        self._root_window.configure(background="#FF9E91")

    def _create_button(self):
        self.button = tkinter.Button(
            master = self._root_window, text = "CLICK HERE IF YOU'RE SAD",
            font = _DEFAULT_FONT,
            command = self.handle_click)
        self.button.pack(padx = 0, pady = 250) 
        return self.button

    def handle_click(self):
        self.button.pack_forget()
        if hasattr(self,"canvas"):
            self.canvas.pack_forget()
            
        img = Image.open(Dog_Image.returnImage())
        tkimage = ImageTk.PhotoImage(img)
        if tkimage.height() > 500:
            self.handle_click()
            return
        self.canvas = tkinter.Canvas(self._root_window, height = 500, width = 500, 
                                     highlightthickness = 0, bg = "#FF9E91" )
        self.canvas.pack()
        self.canvas.create_image((250,250), image=tkimage)
        self.canvas.img = tkimage
        self.button = tkinter.Button(master = self._root_window,text = "STILL SAD?", 
                                     font = _DEFAULT_FONT, command = self.handle_click)
        self.button.pack()

    def run(self):
        self._root_window.mainloop()

if __name__=='__main__':
    DogApp().run()