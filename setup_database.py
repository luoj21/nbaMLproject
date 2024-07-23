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
                      rk INT NOT NULL,
                      player VARCHAR(100),         
                      pos VARCHAR(50),
                      age FLOAT,
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
                      season INT NOT NULL,
                      FOREIGN KEY (rk, season) REFERENCES PER_SEASON_INCOME(player_id, season));
      """)

    
    ''' Loads a player seasonal statistics csv into the PER_GAME_STATS table,
    where the season is specified'''
    def load_stats_data(self, season: int):

      data_folder = '/Users/jasonluo/Documents/nbaProj/per_game_stats_data'
      self.mydb.cursor().execute("USE NBA_DB")
      self.mydb.cursor().execute(f"""LOAD DATA INFILE '{data_folder}/{season}_player_data.csv'
                      INTO TABLE PER_GAME_STATS
                      FIELDS TERMINATED BY ','
                      LINES TERMINATED BY '\n' 
                      IGNORE 1 LINES;""")

      self.mydb.commit()



    def create_income_table(self):
        
        self.mydb.cursor().execute("USE NBA_DB")
        self.mydb.cursor().execute("""CREATE TABLE IF NOT EXISTS PER_SEASON_INCOME (
                                   player_id INT NOT NULL,
                                   player VARCHAR(100),
                                   income FLOAT,
                                   adj_income FLOAT,
                                   season INT NOT NULL,
                                   PRIMARY KEY (player_id, season));""")
    

    def load_income_data(self, season: int):

      data_folder = '/Users/jasonluo/Documents/nbaProj/player_season_income'
      self.mydb.cursor().execute("USE NBA_DB")
      self.mydb.cursor().execute(f"""LOAD DATA INFILE '{data_folder}/{season}_income_data.csv'
                      INTO TABLE PER_SEASON_INCOME
                      FIELDS TERMINATED BY ','
                      LINES TERMINATED BY '\n' 
                      IGNORE 1 LINES;""")

      self.mydb.commit()

    

    def clear_table(self, database: str, table: str):
        
        self.mydb.cursor().execute(f"USE {database}")
        self.mydb.cursor().execute(f"""TRUNCATE TABLE {table}""")
