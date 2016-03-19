from PIL import Image
from glob import glob
import os

def split(filename):
    mainname, subname = os.path.splitext(filename)
    # print mainname
    newindex = int(mainname) * 2
    indexL = "%05d" % (newindex - 1)
    indexR = "%05d" % newindex
    # print indexL, indexR

    img = Image.open(filename)
    # print img.size, img.mode, img.format

    xaxis, yaxis = img.size
    xaxishalf = xaxis/2

    leftimg = img.crop((0, 0, xaxishalf, yaxis))
    leftimg.save('output/'+indexL+'.jpg', 'JPEG')
    # leftimg.show()

    rightimg = img.crop((xaxishalf, 0, xaxis, yaxis))
    # rightimg.show()
    rightimg.save('output/'+indexR+'.jpg', 'JPEG')

def traverse():
    if not os.path.exists('output'):
        os.mkdir('output')

    for jpg in glob('*.jpg'):
        split(jpg)

if __name__ == '__main__':
    traverse()
    print 'done'
