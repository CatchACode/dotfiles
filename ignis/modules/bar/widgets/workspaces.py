from ignis import widgets
from ignis.services.hyprland import HyprlandService, HyprlandWorkspace

hyprland = HyprlandService.get_default()

class WorkspaceButton(widgets.Button):
    def __init__(self, workspace: HyprlandWorkspace) -> None:
        super().__init__(
            css_classes=["workspace-button"],
            on_click=lambda x: workspace.switch_to(),
            #halign="start",
            #valign="center",
            child=widgets.Label(label=f"{workspace.id}"),
        )
        if workspace.id == hyprland.active_workspace.id:
            self.add_css_class("active")

WORKSPACE_MONITOR_MAPPING = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 1,
    5 : 1,
    6 : 1,
    7 : 1,
    8 : 1,
    9 : 1,
    10: 1,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
}

class WorkspaceTitel(widgets.Label):
    def __init__(self, monitor: int):
        # TODO: Figure out how to get each monitor to display seperate active window...
        super().__init__(
            css_classes=["workspace-titel"],
            valign="center",
            label=hyprland.active_window.bind("title")
        )

class Workspaces(widgets.Box):
    def __init__(self, monitor: int) -> None:
        if hyprland.is_available:
            child = [
                widgets.EventBox(
                    css_classes=["workspaces"],
                    child=hyprland.bind_many(
                        ["workspaces", "active_workspace"],
                        transform=lambda workspaces, *_: [
                            WorkspaceButton(i) for i in workspaces if (
                                WORKSPACE_MONITOR_MAPPING.get(i.id) == monitor
                                )
                        ],
                    ),
                ),
            ]
        else:
            child = []
        super().__init__(child=child)
