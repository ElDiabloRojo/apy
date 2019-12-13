"""Default configuration settings"""

DEBUG = True
TESTING = False
LOGGER_NAME = 'api-server'
LOG_FILENAME = 'api-server.log'

MONGO_DBNAME = 'restdb'
MONGO_URI = 'mongodb://user:secretPassword@mongo:27017/restdb'