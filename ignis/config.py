from ignis import utils
from ignis.app import IgnisApp
import os
from modules import (
    Bar,
)

app = IgnisApp.get_default()

app.apply_css(
    os.path.join(utils.get_current_dir(), "style.css"),
)

for monitor in range(utils.get_n_monitors()):
    Bar(monitor)
