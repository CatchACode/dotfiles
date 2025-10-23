#! /bin/bash

active_workspace() {
  local monitorID=$1
  hyprctl monitors -j | jq --arg monitorID "$monitorID" '.[] | select(.id == ($monitorID | tonumber))'
}

workspaces() {
  active_workspace "$1"
}


workspaces 1
