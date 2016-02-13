import MySQLdb

from entity import Entity


class Counter(Entity):
    instance_counter = 0

    def __init__(self, connection, description=None, value=None, ):
        Counter.instance_counter += 1
        Entity.__init__(self, Counter.instance_counter, connection)
        self.value = value
        self.description = description

    def load_from_db(self, id):
        rows = self.select_by_id('counter', id)
        for row in rows:
            self.id = row[0]
            self.description = row[1]
            self.value = row[2]

    def save_to_db(self):
        with self.connection:
            if self.select_by_id('counter', self.id):
                self.connection.cursor().execute("update counter set value={}, description='{}' where id={}".format(self.value, self.description, self.id))
            else:
                self.connection.cursor().execute("insert into counter values ({}, '{}', {})".format(self.id, self.description, self.value))

    def delete_from_db(self, table):
        Entity.delete_from_db(self, 'counter')

    def __str__(self):
        return 'Counter id:{} , description: {}, value: {}'.format(self.id, self.description, self.value)


if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb', autocommit=True)
    counter = Counter(connection)
    counter.description = 'Miles passed counter2'
    counter.value = 10
    counter.save_to_db()

    another_counter = Counter(connection)
    another_counter.id = 8
    another_counter.description = 'Counter with id 2'
    another_counter.value = 6
    another_counter.save_to_db()
