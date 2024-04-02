import prettymaps as pm
from flask import send_from_directory
import os

MAP_ID = 1000

STATIC_FOLDER = os.path.join(os.getcwd(), 'static')

MAP_FOLDER = os.path.join(STATIC_FOLDER, 'maps')

if not os.path.exists(MAP_FOLDER):
    os.makedirs(MAP_FOLDER)


def map_from_waypoint(lon, lat):

    figure, axes = pm.plot(f'{lon}, {lat}',
                           preset='minimal'
                           )

    map_path = os.path.join(MAP_FOLDER, 'map.png')

    # buf.seek(0)

    pm.save_fig(figure, map_path)

    return send_from_directory(MAP_FOLDER, 'map.png')
