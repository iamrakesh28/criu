import struct

import pagemap
    
handlers = {
    'PAGEMAP': pagemap.shred
}


def main(image):
    magic = image['magic']
    entries = handlers[magic](image['entries'])
    image['entries'] = entries
    return images
