"""
Sources: Tess Snyder, https://docs.python.org/2/tutorial/datastructures.html

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
import random

black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
clear = Color(0xffffff, 0.0)
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
whiteline = LineStyle(1,white)
thinline = LineStyle(1, black)
thickline = LineStyle(5, black)
oline = LineStyle(8, blue)
xline = LineStyle(8, red)


vline = RectangleAsset(10, 310, thinline, black)
hline = RectangleAsset(310, 10, thinline, black)
oshape = CircleAsset(30, oline, clear)
xshape = PolygonAsset([(5,5),(35,35),(65,5),(5,65),(35,35),(65,65)], xline, red)

w = PolygonAsset([(5,5),(15,30),(25,15),(35,30),(45,5),(35,30),(25,15),(15,30)], thickline, clear)
i = PolygonAsset([(5,0),(5,30)], thickline, clear)
n = PolygonAsset([(5,30),(5,5),(25,25),(25,0),(25,25),(5,5),(5,30)], thickline, clear)
s = CircleAsset(7.5, thickline, clear)
scover = RectangleAsset(8, 10, whiteline, white)


Sprite(w, (400, 160))
Sprite(i, (455, 165))
Sprite(n, (470, 165))
Sprite(s, (510, 172))
Sprite(s, (510, 188))
Sprite(scover, (505,165))
Sprite(scover, (501,181))

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))
osprites = [ ]
xsprites = [ ]


for x in [95, 195, 295]:
    for y in [95, 195, 295]:
        so = Sprite(oshape, (x,y))
        so.visible = False
        osprites.append(so)

for x in [60, 160, 260]:
    for y in [60, 160, 260]:
        sx = Sprite(xshape, (x,y))
        sx.visible = False
        xsprites.append(sx)

choice = input("Would you like to be X's or O's? ")
player = 0

while player==0:
    if choice=="x":
        player = xsprites
        comp = osprites
            
    elif choice=="o":
        player = osprites
        comp = xsprites
            
    else:
        choice = input("Invalid input. Try again. Would you like to be X's or O's? ")



class Ttt(App):
    
    def __init__(self):
        super().__init__() 
        self.listenMouseEvent( 'click', self.click)
    
    

    
    def click(self, event):
        x = event.x
        y = event.y
        for s in player:
            if abs(x - s.x) <= 40 and abs(y - s.y) <= 40:
                s.visible = True
                player.remove(s)
                
                for sprite in comp:
                    if abs(sprite.x - s.x) <= 40 and abs(sprite.y - s.y) <= 40:
                        comp.remove(sprite)
                
                xorandom = random.choice(comp)
                xorandom.visible = True
                
                comp.remove(xorandom)
                for spr in player:
                    if abs(spr.x - xorandom.x) <= 40 and abs(xorandom.y - spr.y) <= 40:
                        player.remove(spr)



myapp = Ttt()
myapp.run()
