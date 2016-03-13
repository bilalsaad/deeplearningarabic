from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper
import os
from scipy.misc import imread, imsave
import image_functions

FONT_PREFIX= "/Library/Fonts/"
FONTS = ["Arial Unicode.ttf",
         "Al Nile.ttf",
         "AlBayan.tff",
         "Baghdad.tff",
         "Damascus.tff",
         "DecoTypeNash.tff",
         "Nadeem.ttc"]


#here we want to create data for the words in words.txt
#for each word in words.txt we want to createa directory with ~100 images
def create_images(label,count=100):
    # here we want to create count images of label with 
    # different filters/rotations etc..
    img = Image.new("L", (100, 100),200)
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf",30)
    label_correct = arabic_reshaper.reshape(label)
    label_correct = get_display(label_correct)
    draw.text((22,22),label_correct,font=font)
    img.save('pics/' +label + '.png')
    img.close()


def create_copies(direc, org):
    image_data = imread(direc+org).astype(np.float32)
    prefix = direc+'/test_out'
    index=0
    funcs = image_functions.get()
    for f in funcs:
        ims = f(image_data)
        for im in ims:
            imsave(prefix + str(index) +'.png', im)
            index+=1
def create_data(word, label,fontsize = 50, loc = (25,25) ):
    if not os.path.exists('pics/' + label):
        os.makedirs('pics/' + label)
    img = Image.new("L", (100, 100),256)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", fontsize)
    label_correct = arabic_reshaper.reshape(word)
    label_correct = get_display(label_correct)
    draw.text(loc,label_correct,font=font)
    direc = 'pics/'+label
    img.save(direc + '/original.png')
    img.close()
    #now we've created the base picture - now we can process it a bit more
    create_copies(direc, '/original.png')

    
def process_word(line,f=create_data):
    line = line.split()
    word, label = unicode(line[0], 'utf-8'), line[1].rstrip()
    f(word,label)
def create_words(f = 'words_and_labels.txt', process=process_word):
    words=open(f, 'r');
    for line in words:
        process(line)
    words.close()

if __name__=='__main__':
    create_words('words_and_labels.txt', process_word);
