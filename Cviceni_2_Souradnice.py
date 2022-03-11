# V tomto úkolu chceme zjistit vzdálenost mezi 2 body na základě jejich polohy.
# Poloha bude vždy indikována dvěmi souřadnicemi (x, y).
#
# Čili budeme mít například:
#
# Bod 1 se souřadnicemi x=1 a y=1
# Bod 2 se souřadnicemi x=2 a y=2
# Vzorec pro výpočet této vzdálenosti je: √ ( (x1-x2)2 + (y1 - y2)2 )
#
# Tvým úkolem je napsat OOP řešení pro tento problém.
# Naše doporučení je si zkusit vyřešit úkol sám jak v procedurálním, tak OO programování.
# ---------------------------------------------------------------------------------------

import math

# ------------------ procedralni reseni -------------------------------------------------
# ---------------------- bez funkce -----------------------------------------------------

# # bod1
# x1, y1 = (1, 1)
#
# # bod2
# x2, y2 = (2, 2)
#
# vzdalenost = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print(vzdalenost)

# ------------------ procedralni reseni -------------------------------------------------
# ----------------------- ve funkci -----------------------------------------------------

# def vzdalenost(p1, p2) -> float:
#     distance = math.sqrt((p1[0] - p2[1])**2 + (p1[1] - p2[0])**2)
#     return distance
#
#
# print(vzdalenost((1, 1), (2, 2)))

# ------------------ OOP reseni ---------------------------------------------------------

# class Distance:
#     # def __init__(self, p1, p2):
#     #     self.p1 = p1
#     #     self.p2 = p2
#
#     def vzdalenost(self, p1, p2) -> float:
#         distance = math.sqrt((p1[0] - p2[1]) ** 2 + (p1[1] - p2[0]) ** 2)
#         return distance
#
# dist = Distance()
# print(dist.vzdalenost((1,1), (2,2)))

# ------------------ OOP reseni ze zadani -----------------------------------------------


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


point1 = Point(1, 1)
point2 = Point(2, 2)

print(point1.distance(point2))
