#!/usr/bin/env bash

get_last_workspace-window() {
  WORKSPACE_ID=$1
  hyprctl workspaces -j | jq -Mc --argjson id "$WORKSPACE_ID" '.[] | select(.id == $id) | .lastwindowtitle'
}

get_last_workspace_window $1

socat -u UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock - | while read -r; do
  get_last_workspace_window $1
done


