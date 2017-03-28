#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0

 
import zbar  
import Image   
# create a reader  
scanner = zbar.ImageScanner()  
# configure the reader  
scanner.parse_config('enable')
# obtain image data  
pil = Image.open('advanceduse.png').convert('L')  
width, height = pil.size  
raw = pil.tostring()  
# wrap image data  
image = zbar.Image(width, height, 'Y800', raw)  
# scan the image for barcodes  
scanner.scan(image)  
# extract results  
print image.symbols
for symbol in image:  
    print symbol
    # do something useful with results  
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data  
# clean up  
del(image)
