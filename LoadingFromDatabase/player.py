from entity import Entity
from achievement import Achievement
from counter import Counter
from money import Money


class Player(Entity):
    instance_counter = 0

    def __init__(self, connection, name=None, password=None, email=None):
        Player.instance_counter += 1
        Entity.__init__(self, Player.instance_counter, connection)
        self.name = name
        self.password = password
        self.email = email

        self.achievements = []
        self.counters = []
        self.wallet = {}

    def add_counter(self, counter):
        self.counters.append(counter)

    def add_money(self, money):
        if money.type in self.wallet:
            self.wallet[money.type] += money.amount
        else:
            self.wallet[money.type] = money

        coins_collected_counter = self.get_counter("Coins collected")

        if coins_collected_counter and money.type == "Coin":
            coins_collected_counter.value += money.amount
            coins_collector_achievement = Achievement("Mega coins collector")
            if coins_collected_counter.value >= 100 and coins_collector_achievement not in self.achievements:
                self.achievements.append(coins_collector_achievement)

    def get_counter(self, description):
        for counter in self.counters:
            if counter.description == description:
                return counter

    def load_from_db(self, id):
        rows = self.select_by_id('player', id)
        for row in rows:
            self.id = row[0]
            self.name = row[1]
            self.password = row[2]
            self.email = row[3]

            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(
                    "select achievement_id from achievement_player where player_id={}".format(id))

                for achievement_player_row in cursor.fetchall():
                    achievement_id = achievement_player_row[0]
                    achievement = Achievement(self.connection)
                    self.achievements.append(achievement.load_from_db(achievement_id))

                cursor.execute(
                    "select counter_id from counter_player where player_id={}".format(id))

                for counter_player_row in cursor.fetchall():
                    counter_id = counter_player_row[0]
                    counter = Counter(self.connection)
                    self.counters.append(counter.load_from_db(counter_id))

                cursor.execute("select id from money where player_id={}".format(id))
                for money_row in cursor.fetchall():
                    money_id = money_row[0]
                    money = Money(self.connection)
                    money.load_from_db(money_id)
                    self.wallet[money.type] = money


    def delete_from_db(self):
        Entity.delete_from_db(self, "player")

    def __str__(self):
        return "Player id:{}, name:{}, password:{}, email:{}, achievements:{}, counters:{}, wallet:{}". \
            format(self.id, self.name, self.password, self.email, self.achievements, self.counters, self.wallet)
