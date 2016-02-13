class Entity:
    def __init__(self, id, connection):
        self.id = id
        self.connection = connection

    def save_to_db(self):
        pass

    def load_from_db(self, id):
        pass

    def delete_from_db(self, table):
        with self.connection:
            self.connection.cursor().execute("delete from {} where id={}".format(table, self.id))

    def select_by_id(self, table, id):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SELECT * FROM {} where id={}'.format(table, id))
            return cur.fetchall()

    def __repr__(self):
        return self.__str__()


