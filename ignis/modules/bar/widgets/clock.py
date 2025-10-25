import datetime
from ignis import utils
from ignis.variable import Variable
from ignis import widgets


CURRENT_TIME = Variable(
    value=utils.poll.Poll(
        1000, 
        lambda x: datetime.datetime.now().strftime("%H:%M")
    ).bind("output")
)

CURRENT_DATE = Variable(
    value=utils.poll.Poll(
        60*1000,
        lambda x: datetime.datetime.now().strftime("%a %B %d")
    ).bind("output")
)

class Clock(widgets.Box):
    def __init__(self):
        super().__init__(
            spacing=2,
            child=[
                widgets.Label(label=CURRENT_TIME.value),
                widgets.Label(label=CURRENT_DATE.value)
            ],
            css_classes=["clock"]
        )
