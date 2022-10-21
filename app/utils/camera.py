import time

from picamera import PiCamera
# from picamera.array import PiRGBArray


def setup():
    global camera

    # allow the camera to warmup
    time.sleep(1)

    camera = PiCamera()
    camera.resolution = ('600', '400')
    camera.framerate = int('24')
    # raw_capture = PiRGBArray(camera, size=camera.resolution)
