
Using DSLR as webcam
====================

```
gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video4
```

Show webcam video:

```
guvcview -d /dev/video4
```


Alternative with borderless window:

```
mplayer tv:// -tv driver=v4l2:device=/dev/video4:width=300:height=200 -vo xv -geometry 100%:100% -noborder
```

Use "T" to keep the window on top


