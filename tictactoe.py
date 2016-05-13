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
medline = LineStyle(4, black)
oline = LineStyle(8, blue)
xline = LineStyle(8, red)

vline = RectangleAsset(10, 310, thinline, black)
hline = RectangleAsset(310, 10, thinline, black)
oshape = CircleAsset(30, oline, clear)
xshape = PolygonAsset([(5,5),(35,35),(65,5),(5,65),(35,35),(65,65)], xline, red)

w = PolygonAsset([(5,5),(15,30),(25,15),(35,30),(45,5),(35,30),(25,15),(15,30)], thickline, clear)
i = PolygonAsset([(5,0),(5,30)], thickline, clear)
n = PolygonAsset([(5,30),(5,5),(25,25),(25,0),(25,25),(5,5),(5,30)], thickline, clear)
s = CircleAsset(7.5, medline, clear)
scover = CircleAsset(5, whiteline, white)

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))
osprites = [ ]
xsprites = [ ]
playeralive = [ ]


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
        running = False
    
    def click(self, event):
        x = event.x
        y = event.y
        vstop = False
        hstop = False
        diagonal = False
        for s in player:
            if abs(x - s.x) <= 50 and abs(y - s.y) <= 50:
                s.visible = True
                player.remove(s)
                for sprite in comp:
                    if abs(sprite.x - s.x) <= 40 and abs(sprite.y - s.y) <= 40:
                        comp.remove(sprite)
                        print(comp)
                    
                
                if len(playeralive)==0:
                    if (s.x==160 and s.y==160) or (s.x==195 and s.y==195):
                        for c in comp:
                            if c.x==c.y or abs(c.x-c.y)==200:
                                print("corner")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(spr.y - c.y) <= 40:
                                        player.remove(spr)
                                break
                    else:
                        for c in comp:
                            if (c.x==160==c.y==160) or (c.x==195==c.y==195):
                                print("center")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(spr.y - c.y) <= 40:
                                        player.remove(spr)
                                break
                
                #if len(comp) >= 3:
                    #compx = []
                    #for c in comp:
                        #compx.append(c.x)
                    #for n in range(len(comp)
                
                
                if len(playeralive) >= 1:    
                    for n in playeralive:
                        if n.x == s.x:
                            vstop = True
                            break
                    
                    for nn in playeralive:
                        if nn.y == s.y:
                            hstop = True
                            break
                        
                    for m in playeralive:
                        if abs(m.x-s.x)==100 and abs(m.y-s.y)==100:
                            diagonal = True
                            break
                    
                    if vstop == True:
                        for c in comp:
                            if abs(c.x - s.x)==35:
                                print("vstop")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(spr.y - c.y) <= 40:
                                        player.remove(spr)
                                break
                        
                        else: 
                            if hstop == True:
                                for co in comp:
                                    if abs(co.y - s.y)==35:
                                        print("vstop, hstop")
                                        co.visible = True
                                        comp.remove(co)
                                        for spr in player:
                                            if abs(spr.x - co.x) <= 40 and abs(co.y - spr.y) <= 40:
                                                player.remove(spr)
                                        break
                            
                                else: 
                                    if diagonal == True:
                                        for c in comp:
                                            if (abs(s.x-c.x)==abs(s.y-c.y)) or ( abs((abs(s.x-c.x))-(abs(s.y-c.y)))==70 ):
                                                print("vstop, hstop, diag")
                                                c.visible = True
                                                comp.remove(c)
                                                for spr in player:
                                                    if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                                        player.remove(spr)
                                                break
                                    else:
                                        print("vstop, hstop, random")
                                        crandom = random.choice(comp)
                                        crandom.visible = True
                                        comp.remove(crandom)
                                        for spr in player:
                                            if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                                player.remove(spr)
                                        break
                        
                            else:
                                if diagonal == True:
                                    for c in comp:
                                        if (abs(s.x-c.x)==abs(s.y-c.y)) or ( abs((abs(s.x-c.x))-(abs(s.y-c.y)))==70 ):
                                            print("vstop, diag")
                                            c.visible = True
                                            comp.remove(c)
                                            for spr in player:
                                                if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                                    player.remove(spr)
                                            break
                                    else:
                                        print("vstop, diag, random")
                                        crandom = random.choice(comp)
                                        crandom.visible = True
                                        comp.remove(crandom)
                                        for spr in player:
                                            if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                                player.remove(spr)
                                        break
                                    
                   
                    
                    elif hstop == True:
                        for co in comp:
                            if abs(co.y - s.y)==35:
                                print("hstop")
                                co.visible = True
                                comp.remove(co)
                                for spr in player:
                                    if abs(spr.x - co.x) <= 40 and abs(co.y - spr.y) <= 40:
                                        player.remove(spr)
                                break
                        else:
                            if diagonal == True:
                                for c in comp:
                                    if (abs(s.x-c.x)==abs(s.y-c.y)) or ( abs((abs(s.x-c.x))-(abs(s.y-c.y)))==70 ):
                                        print("hstop, diag")
                                        c.visible = True
                                        comp.remove(c)
                                        for spr in player:
                                            if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                                player.remove(spr)
                                        break
                                
                            else:
                                print("hstop, diag, random")
                                crandom = random.choice(comp)
                                crandom.visible = True
                                comp.remove(crandom)
                                for spr in player:
                                    if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                            player.remove(spr)
                                break
                    
                    
                    elif diagonal == True:
                        for c in comp:
                            if (abs(s.x-c.x)==abs(s.y-c.y)) or ( abs((abs(s.x-c.x))-(abs(s.y-c.y)))==70 ):
                                print("diag")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                        player.remove(spr)
                                break
                        else:
                                print("diag, random")
                                crandom = random.choice(comp)
                                crandom.visible = True
                                comp.remove(crandom)
                                for spr in player:
                                    if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                        player.remove(spr)
                                break 
                    
                    else: 
                        for c in comp:
                            if abs(s.x-c.x) == 35:
                                print("else, x=")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                        player.remove(spr)
                                break
                                
                            elif abs(s.y-c.y) == 35:
                                print("else, y=")
                                c.visible = True
                                comp.remove(c)
                                for spr in player:
                                    if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                        player.remove(spr)
                                break
                                
                        else:
                            print("else, random")
                            crandom = random.choice(comp)
                            crandom.visible = True
                            comp.remove(crandom)
                            for spr in player:
                                if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                    player.remove(spr)
                            break 
                
                playeralive.append(s)

myapp = Ttt()
myapp.run()


#Sprite(w, (400, 160))
#Sprite(i, (455, 165))
#Sprite(n, (470, 165))
#Sprite(s, (514, 174))
#Sprite(s, (514, 187))
#Sprite(scover, (522,174))
#Sprite(scover, (505,185))
