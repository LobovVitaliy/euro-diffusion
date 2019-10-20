class City(object):
    INITIAL_COIN_COUNT = 1000000
    REPRESENTATIVE_PORTION = 1000

    def __init__(self, country_count, country_index):
        self.completed = False
        self.neighbors = None
        self.country_count = country_count

        self.coins = [0] * country_count
        self.cache = [0] * country_count

        self.coins[country_index] = self.INITIAL_COIN_COUNT

    # shares coins with neighbors
    def share_with_neighbors(self):

        # city ​​completion check
        if all(map(lambda c: c > 0, self.coins)):
            self.completed = True

        index = 0

        for coin_count in self.coins:
            if coin_count >= self.REPRESENTATIVE_PORTION:
                share = coin_count // self.REPRESENTATIVE_PORTION

                for city in self.neighbors:
                    city.cache[index] += share
                    self.coins[index] -= share

            index += 1

    # updates coins daily
    def update(self):
        for i in range(self.country_count):
            self.coins[i] += self.cache[i]
            self.cache[i] = 0
