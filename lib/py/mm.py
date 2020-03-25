# sets all addresses in mm_entry to 0

def shred(img):
    mm_to_zero = ['mm_start_code', 'mm_end_code', 'mm_start_data', 'mm_end_data','mm_start_stack', 'mm_start_brk','mm_brk', 'mm_arg_start', 'mm_arg_end','mm_env_start', 'mm_env_end',]
    for seg in mm_to_zero:
        img[0][seg] = 0
    return img
