from ignis import utils
from ignis.css_manager import CssInfoPath, CssManager
import os
from modules import (
    Bar,
)

css_manager = CssManager.get_default()


css_manager.apply_css(
    CssInfoPath(
        name="main",
        compiler_function=lambda path: utils.sass_compile(path=path),
        path=os.path.join(
            utils.get_current_dir(), "style.css"
        )
    )
)

for monitor in range(utils.get_n_monitors()):
    Bar(monitor)
