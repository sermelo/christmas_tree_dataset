from tkinter import *


class RequestWindow():
    def __init__(self):
        self.window = Tk()
        self.coordinates = None
        self.create_buttons()
        self.create_canvas()

    def create_buttons(self):
        self.no_light_btn = Button(self.window, text="No light", command=self.noLightCallBack)
        self.no_light_btn.place(x=10, y=10)
        self.skip_btn = Button(self.window, text="Skip", command=self.skipCallBack)
        self.skip_btn.place(x=100, y=10)

    def create_canvas(self):
        self.canvas = Canvas(self.window, width=640, height=480)
        self.canvas.place(x=10, y=50)
        self.canvas.bind("<Button 1>", self.canvasCallBack)

    def canvasCallBack(self, eventorigin):
        x = eventorigin.x
        y = eventorigin.y
        print(x, y)
        self.coordinates = (x, y)
        self.window.quit()

    def skipCallBack(self):
        self.skip = True
        self.coordinates = None
        print("Skip")
        self.window.quit()
    
    def noLightCallBack(self):
        self.no_light = True
        print("no_light")
        self.coordinates = (None, None)
        self.window.quit()

    def request_position(self, image):
        img = PhotoImage(file=image)
        self.canvas.create_image(0, 0, anchor=NW, image=img)

        self.window.title('Process image')
        self.window.geometry("700x600+10+20")

        self.window.mainloop()
        return self.coordinates
