#!/usr/bin/python3

# Capture a PNG while still running in the preview mode.

from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)

preview_config = picam2.preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.capture_file("test.png")
