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
        for s in player:
            if abs(x - s.x) <= 50 and abs(y - s.y) <= 50:
                s.visible = True
                playeralive.append(s)
                player.remove(s)
                for sprite in comp:
                    if abs(sprite.x - s.x) <= 40 and abs(sprite.y - s.y) <= 40:
                        comp.remove(sprite)
                        print(comp)
                    
                
                ######some issues with the vstop / hstop thing and too many elses???
                if len(playeralive) >= 2:    
                    pxvalues = [ ]
                    for p in playeralive:
                        pxvalues.append(p.x)
                    pxvalues.sort()
                    for n in range(len(playeralive)):
                        if pxvalues[n] == pxvalues[n+1]:
                                vstop = True
                
                if vstop == True:
                    for c in comp:
                        if abs(c.x - a.x)==35:
                            c.visible = True
                            comp.remove(c)
                            for spr in player:
                                if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                    player.remove(spr)
                            break
                
                elif hstop == True:
                    for c in comp:
                        if abs(c.y - a.y)==35:
                            c.visible = True
                            comp.remove(c)
                            for spr in player:
                                if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                    player.remove(spr)
                        break
                
                else:
                    for c in comp:
                        if abs(s.x-c.x) == 35:
                            c.visible = True
                            comp.remove(c)
                            for spr in player:
                                if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                    player.remove(spr)
                            break
                    
                        elif abs(s.y - c.y) == 35:
                            c.visible = True
                            comp.remove(c)
                            for spr in player:
                                if abs(spr.x - c.x) <= 40 and abs(c.y - spr.y) <= 40:
                                    player.remove(spr)
                            break
                    
                #else:
                    #crandom = random.choice(comp)
                    #crandom.visible = True
                    #comp.remove(crandom)
                    #for spr in player:
                        #if abs(spr.x - crandom.x) <= 40 and abs(crandom.y - spr.y) <= 40:
                                #player.remove(spr)
                    #break
                    

myapp = Ttt()
myapp.run()





    #def step(self):
            #if len(playeralive)>=3:
                #running = True


#pxvalues = [ ]
        #while running == True:
            #for p in playeralive:
                #append.pxvalues(p.x)
            #pxvalues.sort()
            #for n in range(len(playeralive)):
                #if pxvalues[n] == pxvalues[n+1] == pxvalues[n+2]:
                        #Sprite(playershape, (460, 110))
                        #Sprite(w, (400, 160))
                        #Sprite(i, (455, 165))
                        #Sprite(n, (470, 165))
                        #Sprite(s, (514, 174))
                        #Sprite(s, (514, 187))
                        #Sprite(scover, (522,174))
                        #Sprite(scover, (505,185))
