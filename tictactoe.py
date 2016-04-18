
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 0.9)
thinline = LineStyle(1, black)

vline = RectangleAsset(20, 300, thinline, black)
hline = RectangleAsset(300, 20, thinline, black)

Sprite(vline, (110, 10))
Sprite(vline, (210, 10))
Sprite(hline, (10, 110))
Sprite(hline, (10, 210))

#choice = input("Would you like to be X's or O's? )

myapp = App()
myapp.run()