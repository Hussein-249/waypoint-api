import prettymaps as pm
from flask import Flask, sendfile
import matplotlib.pyplot as plt
import io


def map_from_waypoint(lon, lat):

    figure, axes = pm.plot(f'{lon}, {lat}',
                           preset='minimal'
                           )

    buf = io.BytesIO()

    plt.savefig(buf, format='png')
    buf.seek(0)

    plt.close(figure)

    return sendfile(buf, mimetype='image/png')

    # return buf
