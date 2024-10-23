from pymongo import MongoClient


uri = "mongodb+srv://arslantariq931:Hashmap12@statsfootball.ujhfl7y.mongodb.net/?retryWrites=true&w=majority&appName=StatsFootball"
client = MongoClient(uri)
db = client.get_database('Football')

def get_db():
    return db
