
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 0.9)
thinline = LineStyle(1, black)

vline = RectangleAsset(10, 300, thinline, black)
hline = RectangleAsset(300, 20, thinline, black)

Sprite(vline, (140, 40))
Sprite(vline, (240, 40))
Sprite(hline, (40, 140))
Sprite(hline, (40, 240))

#choice = input("Would you like to be X's or O's? )

myapp = App()
myapp.run()