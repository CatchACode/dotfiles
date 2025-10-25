#!/usr/bin/python3

import json
import subprocess
import socket
import os
import time
from collections import deque


HYPRLAND_INSTANCE_SIGNATURE = os.getenv('HYPRLAND_INSTANCE_SIGNATURE')
SOCKET_PATH = f"/tmp/hypr/{HYPRLAND_INSTANCE_SIGNATURE}/.socket2.sock"

def main():
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as socket_client:
        socket_client.connect(SOCKET_PATH)

        while True:
            monitor_str = subprocess.run(["hyprctl", "monitors", "-j"], capture_output=True)
            monitor_json = json.loads(monitor_str.stdout)
            current_workspace = int(mo)
