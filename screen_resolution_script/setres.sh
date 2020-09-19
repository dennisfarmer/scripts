#!usr/bin/env bash
xrandr --newmode "2464x1440_60.00" 299.25 2464 2640 2904 3344 1440 1443 1453 1493 -hsync +vsync && xrandr --addmode eDP-1 "2464x1440_60.00" && xrandr --output eDP-1 --mode "2464x1440_60.00"
