from openrgb import OpenRGBClient
import time
import json
from openrgb.utils import RGBColor

white = RGBColor(255, 255, 255)
black = RGBColor(0, 0, 0)
red = RGBColor(255, 0, 0)

# Bypass the OpenRGB 1.0/1.1 plugin packet mismatch
OpenRGBClient.update_plugins = lambda self: None

client = OpenRGBClient()
# EVision Keyboard 320F:5000


device = client.get_devices_by_name("EVision Keyboard 320F:5000")[0]
device.set_color(red)
device.set_mode("Custom")
matrix = [
    range(2, 11),
    range(24, 33),
    range(44, 53),
    range(65, 74),
    range(86, 95)
]
from pathlib import Path

frames_path = Path(__file__).resolve().with_name("bad_apple_9x5.json")
with frames_path.open() as frames:
    for row in frames:
        frame_layout = json.loads(row)
        frame = [red] * len(device.leds)

        for leds, pixels in zip(matrix, frame_layout):
            for led, pixel in zip(leds, pixels):
                frame[led] = white if pixel else black

        device.set_colors(frame, fast=True)
        time.sleep(1 / 30)
