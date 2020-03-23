import struct

from . import imgdump
    
handlers = {
    'PAGEMAP': imgdump.pagemap.shred
}


def main(image):
    print('hi')
    magic = image['magic']
    entries = handlers[magic](image['entries'])
    image['entries'] = entries
    return image
