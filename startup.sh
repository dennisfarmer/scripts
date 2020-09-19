#!/usr/bin/env bash


# -----------------------------------------------
# Executed by crontab on startup:
# -----------------------------------------------

# Swap esc and capslock
xmodmap ~/.config/.Xmodmap

# C++ Auto Compile for Visual Studio Code
# Bind Alt + Esc to Ctrl + Shift + B
autokey-gtk

# Kite - ML powered code completions
/home/dennisfarmer/.local/share/kite/kited --system-boot

# Redshift - Color temperature adjustment tool
# redshift-gtk
