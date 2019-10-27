from city import City
from country import Country


class Algorithm(object):
    MAX_XY_VALUE = 10

    def __init__(self):
        self.countries = []

    @staticmethod
    def check_max_xy_value(country_name, value, coord):
        if not 1 <= value <= Algorithm.MAX_XY_VALUE:
            raise Exception('In {}: value {} is not in range 1 ≤ {} ≤ {}'
                            .format(country_name, value, coord, Algorithm.MAX_XY_VALUE))

    @staticmethod
    def check_xy_range(country_name, value_l, value_h, coord_l, coord_h):
        if value_l > value_h:
            raise Exception('In {}: value {}:{} > {}:{}'
                            .format(country_name, coord_l, value_l, coord_h, value_h))

    # parses country from string and adds this country
    def add_country(self, string):
        name, *coordinates = string.split()

        if len(name) > 25:
            raise Exception('Name has more than 25 characters')

        xl, yl, xh, yh = map(int, coordinates)

        Algorithm.check_max_xy_value(name, xl, 'xl')
        Algorithm.check_max_xy_value(name, yl, 'yl')
        Algorithm.check_max_xy_value(name, xh, 'xh')
        Algorithm.check_max_xy_value(name, yh, 'yh')

        Algorithm.check_xy_range(name, xl, xh, 'xl', 'xh')
        Algorithm.check_xy_range(name, yl, yh, 'yl', 'yh')

        self.countries.append(Country(name, xl - 1, yl - 1, xh - 1, yh - 1))

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

        # builds a rectangular area
        y_range = range(max(ys) - min(ys) + 1)
        x_range = range(max(xs) - min(xs) + 1)

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
