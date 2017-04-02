# A Place for Homu

This thing will let you monitor a segment of reddit's [place](https://reddit.com/r/place) using some MJPEG magic.

Uses Flask and Pillow, can get that with Pip

To get around JPEG being awful for pixel art, blows the image up 10x before sending it to the browser.

To change the resolution, change `final_width` and `final_height` in place.py;  
To change where the image is centered, change `center_x`, `center_y`

Original place grabbing script: https://gist.github.com/teaearlgraycold/f36596a45772bb8d59bc3a9fa7b3417e  
Original MJPEG example: http://www.chioka.in/python-live-video-streaming-example/
