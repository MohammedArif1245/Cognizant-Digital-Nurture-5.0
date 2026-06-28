class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Database Instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Database Connected")


db1 = Database()
db2 = Database()

print(db1)
print(db2)

print(db1 is db2)