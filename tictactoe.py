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
xline = LineStyle(8, red)

vline = RectangleAsset(10, 310, thinline, black)
hline = RectangleAsset(310, 10, thinline, black)
o = CircleAsset(30, oline, clear)
x = PolygonAsset([(5,5),(35,35),(65,5),(5,65),(35,35),(65,65)], xline, red)

#PolygonAsset([(180,10),(140,90),(220,90)], thinline, darkgreen)

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))
osprites = [ ]

#choice = input("Would you like to be X's or O's? )
#difficulty??

for x in [95, 195, 295]:
    for y in [95, 195, 295]:
        so = Sprite(o, (x,y))
        so.visible = False
        osprites.append(so)

for x in [95, 195, 295]:
    for y in [95, 195, 295]:
        sx = Sprite(x, (x,y))

class Ttt(App):
    
    def __init__(self):
        super().__init__() 
        self.listenMouseEvent( 'click', self.click)

    def click(self, event):
        x = event.x
        y = event.y
        for s in osprites:
            if abs(x - s.x) <= 50 and abs(y - s.y) <= 50:
                s.visible = True



myapp = Ttt()
myapp.run()