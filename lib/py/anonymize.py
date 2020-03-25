import struct

from . import imgdump
    
handlers = {
    'PAGEMAP': imgdump.pagemap.shred,
    'MM': imgdump.mm.shred
}


def main(image):
    magic = image['magic']
    entries = handlers[magic](image['entries'])
    image['entries'] = entries
    return image
