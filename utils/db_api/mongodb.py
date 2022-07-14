import pymongo

# подключаемся к базе данных
db_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = db_client['database']

#  инициализируем коллекции
users = db['users']