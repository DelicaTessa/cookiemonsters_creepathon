#!/usr/bin/python

from PIL import Image

img = Image.open("bag.png")

background = Image.open("person.png")

background.paste(img, (0, 0), img)
background.save('combined.png',"PNG")