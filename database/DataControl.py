import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
query_module_dir = os.path.dirname(os.path.join(script_dir, 'query.py'))
sys.path.append(query_module_dir)

# import query  # cannot move to top file due to the above code needed first


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
        print("Call")
        if cls not in cls._instances:
            print("adding to instances")
            print(f"Creating {cls.__name__} instance")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            return cls._instances[cls]
            # raise RuntimeError("Singleton already instantiated, not allowed to use this class in current scope.")
            # this is not how singletons work!!!


class DataControl(metaclass=SingletonControlMeta):
    def __init__(self):
        print("DataControl instance created")
        from query import db_connect, query_single_point, db_disconnect
        self.db_connect = db_connect
        self.query_single_point = query_single_point
        self.db_disconnect = db_disconnect

    def connect_database(self):
        return self.db_connect()

    def find_single_point(self, waypoint, connection):
        return self.query_single_point(waypoint, connection)

    def disconnect_database(self, connection):
        return self.db_disconnect(connection)
