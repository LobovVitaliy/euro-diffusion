from city import City
from country import Country


class Algorithm(object):
    def __init__(self):
        self.countries = []

    # parses country from string and adds this country
    def add_country(self, string):
        name, *coordinates = string.split()

        if len(name) > 25:
            raise Exception('Name has more than 25 characters')

        # translate into integer value ​​and
        # add a new coordinate system relative to the point (0;0)
        xl, yl, xh, yh = map(lambda p: int(p) - 1, coordinates)

        if not 0 <= xl <= 9:
            raise Exception('1 ≤ xl ≤ 10')

        if not 0 <= yl <= 9:
            raise Exception('1 ≤ yl ≤ 10')

        if not 0 <= xh <= 9:
            raise Exception('1 ≤ xh ≤ 10')

        if not 0 <= yl <= 9:
            raise Exception('1 ≤ yl ≤ 10')

        self.countries.append(Country(name, xl, yl, xh, yh))

    # creates an empty area where cities are located
    # depending on the position of countries
    def create_empty_area(self):
        # all x coordinates
        xs = []
        # all y coordinates
        ys = []

        # fills xs and ys lists
        for country in self.countries:
            xs.extend((country.xl, country.xh))
            ys.extend((country.yl, country.yh))

        # finds the extreme x coordinates
        min_x = min(xs)
        max_x = max(xs)

        # finds the extreme y coordinates
        min_y = min(ys)
        max_y = max(ys)

        # builds a rectangular area
        y_range = range(max_y - min_y + 1)
        x_range = range(max_x - min_x + 1)
        return [[None for _ in y_range] for _ in x_range]

    # creates cities
    def create_cities(self, area):
        country_count = len(self.countries)
        country_index = 0

        for country in self.countries:
            for i in range(country.xh - country.xl + 1):
                for j in range(country.yh - country.yl + 1):
                    x = country.xl + i
                    y = country.yl + j

                    city = City(country_count, country_index)

                    area[x][y] = city
                    country.add_city(city)

            country_index += 1

    # adds neighbors
    def add_neighbors(self, area):
        w = len(area)
        h = len(area[0])

        for x in range(w):
            for y in range(h):
                city = area[x][y]

                if city:
                    neighbors = []

                    # checks for neighbors and
                    # adds them to the neighbors list

                    # east neighbor
                    if x + 1 <= w - 1 and area[x + 1][y]:
                        neighbors.append(area[x + 1][y])

                    # west neighbor
                    if x - 1 >= 0 and area[x - 1][y]:
                        neighbors.append(area[x - 1][y])

                    # north neighbor
                    if y + 1 <= h - 1 and area[x][y + 1]:
                        neighbors.append(area[x][y + 1])

                    # south neighbor
                    if y - 1 >= 0 and area[x][y - 1]:
                        neighbors.append(area[x][y - 1])

                    city.neighbors = neighbors

    # initializes cities and their neighbors
    def init(self):
        # creates an empty cities area
        area = self.create_empty_area()

        # creates cities
        self.create_cities(area)

        # adds neighbors
        self.add_neighbors(area)

    # checks the completion of all countries
    def is_completed(self):
        return all(map(lambda x: x.is_completed(), self.countries))

    # runs the algorithm
    def run(self):
        # initializes cities
        self.init()

        result = {}
        days = 0

        # main part of the algorithm
        while True:
            # cities share coins with their neighbors
            for country in self.countries:
                for city in country.cities:
                    city.share_with_neighbors()

                # if the country is completed,
                # it is saved in the results
                if country.is_completed():
                    if country.name not in result:
                        result[country.name] = days

            # if all countries are completed,
            # the algorithm ends
            if self.is_completed():
                break

            # at the end of the day,
            # cities update their coin stock
            for country in self.countries:
                for city in country.cities:
                    city.update()

            days += 1

        # sorts the result of the algorithm
        return sorted(result.items(), key=lambda x: (x[1], x[0]))
