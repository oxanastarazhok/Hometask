import MySQLdb

from entity import Entity


class Money(Entity):
    instance_counter = 0

    def __init__(self, connection, type=None, amount=None):
        Money.instance_counter += 1
        Entity.__init__(self, Money.instance_counter, connection)
        self.type = type
        self.amount = amount

    def load_from_db(self, id):
        rows = self.select_by_id('money', id)
        for row in rows:
            self.id = row[0]
            self.type = row[1]
            self.amount = row[2]

    def save_to_db(self):
        with self.connection:
            if self.select_by_id('money', self.id):
                self.connection.cursor().execute(
                    "update money set type='{}', amount={} where id={}".format(self.type, self.amount, self.id))
            else:
                self.connection.cursor().execute("insert into money (type, amount, id) values ('{}',{},{})".format(self.type, self.amount, self.id))

    def delete_from_db(self):
        Entity.delete_from_db(self, "money")

    def __str__(self):
        return 'Money id:{}, type:{} , amount: {}'.format(self.id, self.type, self.amount)


if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb', autocommit=True)
    coins = Money(connection)
    dollars = Money(connection)
    coins.load_from_db(1)
    dollars.load_from_db(2)
    coins.id = 3
    coins.save_to_db()
    coins.delete_from_db()

    print(coins)
    print(dollars)
