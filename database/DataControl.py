class SingletonControlMeta(type):
    _instances = {}

    # ensures single instances only
    def __call__(cls, *args, **kwargs):
        """Ensures that any class with SingletonControlMeta
            as the metaclass can not be instantiated more than once.
            Prevents code from being called outside of ownership of
            object.
            Prevents potential query conflicts.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super.__call__(*args, **kwargs)
        else:
            raise RuntimeError("Singleton already instantiated, not allowed to use this class in current scope.")


class DataControl(metaclass=SingletonControlMeta):
    import query

    def __init__(self):
        pass

    def __connect_database(self):
        return self.query.db_connect()

    def __find_single_point(self, waypoint, connection):
        return self.query.query_single_point(waypoint, connection)

    def __disconnect_database(self, connection):
        return self.query.db_disconnect(connection)
