from ignis import widgets

from .widgets import Workspaces, Clock, WorkspaceTitel, Tray

class Bar(widgets.window.Window):
    __gtype_name__ = "Bar"

    def __init__(self, monitor:int):
        super().__init__(
            anchor=["left", "bottom", "right"],
            exclusivity="exclusive",
            monitor=monitor,
            namespace=f"ignis_BAR_{monitor}",
            layer="top",
            kb_mode="none",
            child=widgets.centerbox.CenterBox(
                css_classes=["bar-widgets"],
                start_widget=widgets.box.Box(
                    valign="center",
                    css_classes=["start-widgets"],
                    child=[
                        WorkspaceTitel(monitor)
                    ],
                ),
                center_widget=widgets.box.Box(
                    vertical=True,
                    child=[
                        Workspaces(monitor),
                    ]
                ),
                end_widget=widgets.box.Box(
                        child=[
                        Tray(),
                        Clock(),
                ]),

            ),
            css_classes=["bar"],
        )
