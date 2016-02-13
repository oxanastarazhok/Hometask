import MySQLdb

from entity import Entity


class Achievement(Entity):
    instance_counter = 0

    def __init__(self, connection, description=None):
        Achievement.instance_counter += 1
        Entity.__init__(self, Achievement.instance_counter, connection)
        self.description = description

    def load_from_db(self, id):
        rows = self.select_by_id('achievement', id)
        for row in rows:
            self.id = row[0]
            self.description = row[1]

    def save_to_db(self):
        rows = self.select_by_id('achievement', self.id)
        with self.connection:
            if rows:
                self.connection.cursor().execute("update achievement set description='{}' where id={}".format(self.description, self.id))
            else:
                self.connection.cursor().execute("insert into achievement values ({}, '{}')".format(self.id, self.description))

    def delete_from_db(self):
        Entity.delete_from_db(self, "achievement")

    def __str__(self):
        return 'Achievement id:{} , description: {}'.format(self.id, self.description)


if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb', autocommit=True)
    another_achievement = Achievement(connection)
    another_achievement.id = 5
    another_achievement.description = "another one achievement"
    another_achievement.save_to_db()
