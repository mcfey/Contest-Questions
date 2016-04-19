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
oline = LineStyle(8, blue)

vline = RectangleAsset(10, 310, thinline, black)
hline = RectangleAsset(310, 10, thinline, black)
o = CircleAsset(30, oline, clear)

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))
sprites = [ ]

#choice = input("Would you like to be X's or O's? )
#difficulty??

for x in [95, 195, 295]:
    for y in [95, 195, 295]:
        so = Sprite(o, (x,y))
        so.visible = False
        sprites.append(so)


class Ttt(App):
    
    def __init__(self):
        super().__init__() 
        self.listenMouseEvent( 'click', self.click)

    def click(self, event):
        x = event.x
        y = event.y
        for s in sprites:
            if abs(x - s.x) <= 50 and abs(y - s.y) <= 50:
                s.visible = True



myapp = Ttt()
myapp.run()