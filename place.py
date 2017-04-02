# https://gist.github.com/teaearlgraycold/f36596a45772bb8d59bc3a9fa7b3417e
import requests
import io
from PIL import Image

bitmap_width = 1000
bitmap_height = 1000

final_width = 100
final_height = 100

center_x = 411
center_y = 206

origin_x = int(center_x - final_width/2)
origin_y = int(center_y - final_height/2)

if origin_x < 0:
    origin_x = 0
if origin_y < 0:
    origin_y = 0

colours = [
    (0xff, 0xff, 0xff), # #FFFFFF
    (0xe4, 0xe4, 0xe4), # #E4E4E4
    (0x88, 0x88, 0x88), # #888888
    (0x22, 0x22, 0x22), # #222222
    (0xff, 0xa7, 0xd1), # #FFA7D1
    (0xe5, 0x00, 0x00), # #E50000
    (0xe5, 0x95, 0x00), # #E59500
    (0xa0, 0x6a, 0x42), # #A06A42
    (0xe5, 0xd9, 0x00), # #E5D900
    (0x94, 0xe0, 0x44), # #94E044
    (0x02, 0xbe, 0x01), # #02BE01
    (0x00, 0xd3, 0xdd), # #00D3DD
    (0x00, 0x83, 0xc7), # #0083C7
    (0x00, 0x00, 0xea), # #0000EA
    (0xcf, 0x6e, 0xe4), # #CF6EE4
    (0x82, 0x00, 0x80)  # #820080
]

def check_bounds(x, y):
    if (x >= origin_x) and (x < (origin_x + final_width)) and (y >= origin_y) and (y < (origin_y + final_height)):
        return True
    else:
        return False

def bitmap_to_jpg():
    # print("grabbing board...")
    bitmap = requests.get('https://www.reddit.com/api/place/board-bitmap').content
    header_size = 3
    img = Image.new('RGB', (final_width, final_height), color=colours[0])

    # I'm scared to mess around with the byte stuff so I don't touch it
    for i, byte in enumerate(bitmap[(header_size + 1):]):
        x1 = (i * 2) % bitmap_width
        y1 = min((i * 2) // bitmap_width, bitmap_height - 1)
        x2 = (x1 + 1) % bitmap_width
        y2 = y1 + 1 if (x1 + 1) > (bitmap_width - 1) else y1

        # The upper nibble represents the first pixel, and the lower nibble
        # represents the second pixel
        if check_bounds(x1,y1) == True:
            color1 = colours[byte >> 4]
            img.putpixel((x1 - origin_x, y1 - origin_y), color1)
        if check_bounds(x2,y2) == True:
            color2 = colours[byte & 0x0F]
            img.putpixel((x2 - origin_x, y2 - origin_y), color2)

    
    # https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
    strIO = io.BytesIO()
    img.resize((final_width * 10, final_height * 10), Image.NEAREST).save(strIO, 'JPEG', quality=100)
    strIO.seek(0)
    return strIO.getvalue()
    #img.save(png_name)

#import sys
#sys.stdout.buffer.write(bitmap_to_png().getvalue())
