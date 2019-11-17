import re

reduta = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

a = re.findall("a",reduta)
e = re.findall("e",reduta)
y = re.findall("y",reduta)
i = re.findall("i",reduta)
o = re.findall("o",reduta)
ą = re.findall("ą",reduta)
ę = re.findall("ę",reduta)
u = re.findall("u",reduta)
ó = re.findall("ó",reduta)

print("a - ",len(a),"\ne - ",len(e),"\ny - ",len(y),"\ni - ",len(i),"\no - ",len(o),"\ną - ",len(ą),"\nę - ",len(ę),"\nu - ",len(u),"\nó - ",len(ó))

