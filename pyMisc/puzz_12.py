#!/usr/bin/python

# Copied solution from http://intelligentgeek.blogspot.com/2006/03/python-challenge-12-dealing-evil.html


evil = open('evil2.gfx','r').read()
img1 = open('img1.jpg','w')
img2 = open('img2.jpg','w')
img3 = open('img3.jpg','w')
img4 = open('img4.jpg','w')
img5 = open('img5.jpg','w')

for b in range(0,len(evil),5):
    img1.write(evil[b])
    img2.write(evil[b+1])
    img3.write(evil[b+2])
    img4.write(evil[b+3])
    img5.write(evil[b+4])

img1.close()
img2.close()
img3.close()
img4.close()
img5.close()