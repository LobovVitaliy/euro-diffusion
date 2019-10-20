class Country(object):
    def __init__(self, name, xl, yl, xh, yh):
        self.cities = []
        self.name = name
        self.xl = xl
        self.yl = yl
        self.xh = xh
        self.yh = yh

    # adds a new city
    def add_city(self, city):
        self.cities.append(city)

    # checks the completion of the country
    def is_completed(self):
        return all(map(lambda c: c.completed, self.cities))
