# shred sets virtual addresses to 0

def shred(img):
        for entry in img:
                if 'vaddr' in entry:
                        entry['vaddr'] = 0

        return img
