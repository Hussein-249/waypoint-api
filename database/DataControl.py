import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
query_module_dir = os.path.dirname(os.path.join(script_dir, 'query.py'))
sys.path.append(query_module_dir)


class SingletonControlMeta(type):
    _instances = {}

    # ensures single instances only
    def __call__(cls, *args, **kwargs):
        """Ensures that any class with SingletonControlMeta
            as the metaclass can not be instantiated more than once.
            Prevents potential query conflicts.
        """
        if cls not in cls._instances:
            # print(f"Creating {cls.__name__} instance")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DataControl(metaclass=SingletonControlMeta):
    def __init__(self):
        from query import _db_connect, query_single_point, db_disconnect
        self.db_connect = _db_connect
        self.query_single_point = query_single_point
        self.db_disconnect = db_disconnect

    @classmethod
    def connect_database(cls):
        return cls().db_connect()

    @classmethod
    def find_single_point(cls, waypoint, connection):
        return cls().query_single_point(waypoint, connection)

    @classmethod
    def disconnect_database(cls, connection):
        return cls().db_disconnect(connection)
