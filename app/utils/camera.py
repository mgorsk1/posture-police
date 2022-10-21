import time

from picamera import PiCamera


def setup():
    global camera

    # allow the camera to warmup
    time.sleep(1)

    camera = PiCamera()
    camera.resolution = ('600', '400')
    camera.framerate = int('24')

    return camera
