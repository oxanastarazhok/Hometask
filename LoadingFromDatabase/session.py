from connection_util import connection
from entity import Entity
from player import Player


class Session(Entity):
    instance_counter = 0

    def __init__(self, connection):
        Session.instance_counter += 1
        Entity.__init__(self, Session.instance_counter, connection)
        self.start = None
        self.finish = None
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def load_from_db(self, id):
        rows = self.select_by_id('session', id)
        for row in rows:
            self.id = row[0]
            self.start = row[1]
            self.finish = row[2]
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("select id from player where session_id={}".format(id))
            for player_row in cursor.fetchall():
                player_id = player_row[0]
                player = Player(self.connection)
                player.load_from_db(player_id)
                self.add_player(player)

    def delete_from_db(self):
        Entity.delete_from_db(self, "session")

    def __str__(self):
        return "Session id:{}, start:{}, finish:{}, players:{}".format(self.id, self.start, self.finish, self.players)

if __name__ == '__main__':
    session = Session(connection)
    session.load_from_db(1)
    print(session)