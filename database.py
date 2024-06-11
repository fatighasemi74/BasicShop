class InMemoryDatabase:
    db = None

    @classmethod
    def get_db(cls):
        if cls.db is None:
            cls.db = {}
        return cls.db