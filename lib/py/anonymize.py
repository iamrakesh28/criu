import struct

from images import magic
from images import MagicException

def shred():
    print("test message")
    
handlers = {
    'INVENTORY': shred
}

def __rhandler(f):
    # Images v1.1 NOTE: First read "first" magic.
    img_magic, = struct.unpack('i', f.read(4))
    if img_magic in (magic.by_name['IMG_COMMON'],
                     magic.by_name['IMG_SERVICE']):
        img_magic, = struct.unpack('i', f.read(4))

    try:
        m = magic.by_val[img_magic]
    except:
        raise MagicException(img_magic)

    try:
        handler = handlers[m]
    except:
        raise Exception("No handler found for image with magic " + m)

    return m, handler

def main(f):
    images = {}
    m, handler = __rhandler(f)
    handler()
