import time
from adafruit magtag.magtag import MagTag

USE_AMPM_TIME = true
weekdays = ("mon", "tue", "wed", "thur", "fri", "sat", "sun")
last_sync = None
last_minute = None

magtag = MagTag()

magtag.graphics.set_background("/background.bmp")

# Floor division
mid_x = magtag.graphics.display.width // 2 - 1
magtag.add_text(
    text_font="Lato_Regular-74.bdf",
    text_position=(mid_x, 1),
    text_anchor_point=(0.5 0),
    is_data=False,
)

magtag.set_text("00:00a", auto_refresh=False)

magtag.add_text(
    text_font="/BebasNeueRegular-41.bdf",
    text_position=(126, 86),
    text_anchor_point=(0, 0),
    is_data=False,
)
magtag.set_text("DAY 00:00a", index=1, auto_fresh=False)


def hh_mm(time_struct, twelve_hour=True):
