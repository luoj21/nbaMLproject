import mysql.connector

''' Connects user to MySQL database'''


class MySQLConnector():
    
    def __init__(self, host: str, user: str, password: str):
        self.host = host
        self.user = user
        self.password = password

    def connect_to_db(self):
        self.mydb = mysql.connector.connect(
        host= self.host,
        user= self.user,
        password = self.password
      )
        
        print("## Connected to database ##")
        
        
    def disconnect_from_db(self):
        self.mydb.cursor().close()
        self.mydb.close()
        del self.mydb
        print("## Disconnected from database ##")
      
        
    def create_nba_db(self):
        self.mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS NBA_DB")
        
    def create_stats_table(self):
        
      self.mydb.cursor().execute("USE NBA_DB")
      self.mydb.cursor().execute("""
                      CREATE TABLE IF NOT EXISTS PER_GAME_STATS (
                      player_id INT NOT NULL,
                      season INT NOT NULL,       
                      pos VARCHAR(50),
                      age INT,
                      team VARCHAR(50),
                      games FLOAT,
                      games_started FLOAT,  
                      mp FLOAT,
                      fg FLOAT,
                      fga FLOAT,
                      fg_perc FLOAT,
                      three_point FLOAT,
                      three_point_att FLOAT,
                      three_point_perc FLOAT,
                      two_point FLOAT,
                      two_point_att FLOAT,
                      two_point_perc FLOAT,
                      efg FLOAT,     
                      ft FLOAT,
                      fta FLOAT,
                      ft_perc FLOAT,
                      orb FLOAT,
                      drb FLOAT,
                      trb FLOAT,
                      ast FLOAT,
                      stl FLOAT,
                      blk FLOAT,
                      tov FLOAT,
                      pf FLOAT,
                      pts FLOAT,
                      PRIMARY KEY (player_id, season),
                      FOREIGN KEY (player_id) REFERENCES PER_SEASON_INCOME(player_id));
      """)

    
    def load_data(self, file_path: str, table_name: str):

      self.mydb.cursor().execute("USE NBA_DB")
      self.mydb.cursor().execute(f"""LOAD DATA INFILE '{file_path}'
                      INTO TABLE {table_name}
                      FIELDS TERMINATED BY ','
                      LINES TERMINATED BY '\n' 
                      IGNORE 1 LINES;""")

      self.mydb.commit()


    def create_income_table(self):
        
        self.mydb.cursor().execute("USE NBA_DB")
        self.mydb.cursor().execute("""CREATE TABLE IF NOT EXISTS PER_SEASON_INCOME (
                                   player_id INT NOT NULL,
                                   season INT NOT NULL,
                                   income FLOAT,
                                   adj_income FLOAT,
                                   PRIMARY KEY (player_id, season),
                                   FOREIGN KEY (player_id) REFERENCES PLAYERS_TABLE(player_id));""")


    def create_players_table(self):
      self.mydb.cursor().execute("USE NBA_DB")
      self.mydb.cursor().execute("""CREATE TABLE IF NOT EXISTS PLAYERS_TABLE (
                                 player_id INT NOT NULL,
                                 player VARCHAR(100),
                                 PRIMARY KEY (player_id)
      );""")
      self.mydb.commit()
       

    def clear_table(self, database: str, table: str):
        
        self.mydb.cursor().execute(f"USE {database}")
        self.mydb.cursor().execute(f"""TRUNCATE TABLE {table}""")



''' Original DB structure

t1: Income
(Season , player_id), player, income

t2: Stats
(Season, player_id), player, ppg, stls, reb, etc...

Normalized DB structure

t1: Income
(Season (CPK/FK), player_id, (CPK/FK)) income

t2: Stats
(Season (CPK/FK), player_id, (CPK/FK)), ppg, stls, reb, etc...

t3: Player Names
player_id (PK), player
'''