"""
Sources: 

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
clear = Color(0xffffff, 0.0)
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
thinline = LineStyle(1, black)
oline = LineStyle(7, blue)

vline = RectangleAsset(10, 310, thinline, black)
hline = RectangleAsset(310, 10, thinline, black)
o = CircleAsset(30, oline, clear)

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))



#choice = input("Would you like to be X's or O's? )


class Ttt(App):
    
    def __init__(self):
        super().__init__() 
        self.listenMouseEvent( 'click', self.click)

    def click(self, event):
        x = event.x
        y = event.y
        Sprite(o, (x, y))



myapp = Ttt()
myapp.run()