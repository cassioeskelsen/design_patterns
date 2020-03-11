class DbConfig():

    def __init__(self):
        self.database = ""
        self.user = ""
        self.password = ""

class DataRepository:

    def __init__(self, config):
        self.db_config = config


    def connect(self):
        print("")
        print(f'Connecting to {self.db_config.database} with {self.db_config.user} and password {self.db_config.password}...')
        print("")
        # connecting stuff..


if __name__ == "__main__":

    confMongo = DbConfig()
    confMongo.database = "Mongo@localhost"
    confMongo.user = "root"
    confMongo.password = "password"

    repository = DataRepository(confMongo)
    repository.connect()

