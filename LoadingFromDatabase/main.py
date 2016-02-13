from datetime import datetime

import MySQLdb

from counter import Counter
from money import Money
from player import Player
from session import Session

connection = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb', autocommit=True)


session = Session()
session.start = datetime.now()
oxana = Player("Oxana", "1234", "oxana@gmail.com")
session.add_player(oxana)

oxana.add_counter(Counter("Coins collected", 0))

coins = Money("Coin", 100)
oxana.add_money(coins)

session.finish = datetime.now()
# session.save_to_db()