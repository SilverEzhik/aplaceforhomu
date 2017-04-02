import requests
from PIL import Image

bitmap_width = 1000
bitmap_height = 1000
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

def bitmap_to_png(bitmap, png_name):
    header_size = 3
    img = Image.new('RGB', (bitmap_width, bitmap_height), color=colours[0])

    for i, byte in enumerate(bitmap[(header_size + 1):]):
        x1 = (i * 2) % bitmap_width
        y1 = min((i * 2) // bitmap_width, bitmap_height - 1)
        x2 = (x1 + 1) % bitmap_width
        y2 = y1 + 1 if (x1 + 1) > (bitmap_width - 1) else y1

        # The upper nibble represents the first pixel, and the lower nibble
        # represents the second pixel
        color1 = colours[byte >> 4]
        color2 = colours[byte & 0x0F]

        img.putpixel((x1, y1), color1)
        img.putpixel((x2, y2), color2)

    img.save(png_name)

resp = requests.get('https://www.reddit.com/api/place/board-bitmap')
bitmap_to_png(resp.content, 'out.png')
