from PIL import Image
from glob import glob
import os
import zipfile

new_index = 1
prefix = 'kindle_'
def split(filename):
    indexL = "%05d" % (2 * new_index)
    indexR = "%05d" % (2 * new_index - 1)
    # print indexL, indexR

    img = Image.open(filename)
    # print img.size, img.mode, img.format

    xaxis, yaxis = img.size
    xaxishalf = xaxis/2

    leftimg = img.crop((0, 0, xaxishalf, yaxis))
    leftimg.save(prefix+indexL+'.jpg', 'JPEG')
    # leftimg.show()

    rightimg = img.crop((xaxishalf, 0, xaxis, yaxis))
    # rightimg.show()
    rightimg.save(prefix+indexR+'.jpg', 'JPEG')

def comicsplit():
    global new_index
    new_index = 1
    allcomic = []

    all = os.listdir('.')
    for comic in sorted(all):
        main, sub = os.path.splitext(comic)
        if 'jpg' in sub or 'JPEG' in sub or 'JPG' in sub:
            allcomic.append(comic)

    for jpg in allcomic:
        if prefix in jpg:
            # os.remove(jpg)
            continue
        print jpg

        split(jpg)
        new_index += 1

def unzip():
    for zname in glob('*.zip'):
        print zname
        zfile = zipfile.ZipFile(zname)
        for name in zfile.namelist():
            (dirname, filename) = os.path.splitext(zname)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
                print "Decompressing " + dirname
            zfile.extract(name, dirname)

def traverse():
    print os.getcwd()
    unzip()

    allfile = os.listdir('.')
    for comic in allfile:
        if os.path.isdir(comic):
            os.chdir(comic)
            traverse()
            comicsplit()
            os.chdir('..')

if __name__ == '__main__':
    traverse()
