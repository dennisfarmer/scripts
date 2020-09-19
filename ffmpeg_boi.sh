ffmpeg -ss 4.5 -t 6.5 -i simplescreenrecorder-2020-06-14_08.51.13.mkv -vf "scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output2.gif
