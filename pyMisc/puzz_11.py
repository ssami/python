# puzz_11.py
#!/usr/bin/python

from PIL import Image

im = Image.open('cave.jpg')
pixels = list(im.getdata())
pix1 = [x for x in pixels[::2]]
pix2 = [x for x in pixels[1::2]]

im1 = Image.new('RGB', im.size)
im1.putdata(pix1)

im2 = Image.new('RGB', im.size)
im2.putdata(pix2)

im1.show()
im2.show()