
def convert_lon_relative_dist(longitude: str) -> float:
    """
    Converts a degrees-minutes-seconds value to decimal value
    :param longitude:
    :return:
    """
    # remove both the ' and " (minutes and seconds characters) from the waypoint
    numeric_str = longitude.replace("'", "").replace('"', "")

    # might not be efficient, should be revised if possible
    numeric_str = numeric_str.split(" ")

    degrees = float(numeric_str[0])
    minutes = float(numeric_str[1])
    seconds = float(numeric_str[2])

    minutes_dec = minutes / 60
    seconds_dec = seconds / 60

    converted = float(degrees + minutes_dec + seconds_dec)

    return converted


def convert_lat_relative_dist(latitude: str) -> float:
    # remove both the ' and " (minutes and seconds characters) from the waypoint
    numeric_str = latitude.replace("'", "").replace('"', "")

    # might not be efficient, should be revised if possible
    numeric_str = numeric_str.split(" ")

    main = float(numeric_str[0])
    minutes = float(numeric_str[1])
    seconds = float(numeric_str[2])

    minutes_dec = minutes / 60
    seconds_dec = seconds / 60

    converted = float(main + minutes_dec + seconds_dec)

    return converted


def extract_lat_from_waypoint(waypoint: dict) -> str:
    """
    Extracts the latitude value as a string from a waypoint dict from the postgres database.
    """
    latitude = waypoint['lat'][:-1]
    return latitude


def extract_lon_from_waypoint(waypoint: dict) -> str:
    """
    Extracts the longitude value as a string from a waypoint dict from the postgres database.
    """
    longitude = waypoint['lon'][:-1]
    return longitude
