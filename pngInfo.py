from PIL import Image
from sys import argv

#Author: Mitesh Vaid; Alias(Emvee)

try:
    p=argv[1]
    im=Image.open(p)
    data=im.info
    data['filename']=p
    print(data)
except IndexError:
    print('Please Enter Filename')

