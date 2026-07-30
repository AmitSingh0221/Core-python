class india():
    def country(self):
        print("India is a country")

    def language(self):
        print("India has many languages")

    def culture(self):
        print("India has a rich culture")


class USA():
    def country(self):
        print("USA is a country")

    def language(self):
        print("USA has many languages")

    def culture(self):
        print("USA has a rich culture")


ind = india()
usa = USA()
for con in (ind, usa):
    con.country()
    con.language()
    con.culture()