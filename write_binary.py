from note import Note

def name_num(name):
    val = 0

    match name:
        case 'c':
            val = 0x0c

        case 'd':
            val = 0x0d

        case 'e':
            val = 0x0e

        case 'f':
            val = 0x0f

        case 'g':
            val = 0x09

        case 'a':
            val = 0x0a

        case 'b':
            val = 0x0b

    return val

def oct_num(oct):
    val = 0

    match oct:
        case -1:
            val = 0x01

        case 0:
            val = 0x00

        case 1:
            val = 0x02

    return val

def sig_num(sig):
    val = 0

    match sig:
        case '':
            val = 0x00

        case '#':
            val = 0x01

        case 'b':
            val = 0x02

    return val

def note_bin(n: Note):
    binum = name_num(n.name)
    bioct = oct_num(n.oct)
    bisig = sig_num(n.sig)
    midi_val = n.midi_val

    res = ( ( (binum << 2) + bioct) << 2 ) + bisig
    return (res, midi_val)

def scale_bin(scale):
    binscale = list()
    
    for n in scale:
        res = note_bin(n)
        binscale.append(res[0])
        binscale.append(res[1])

    return binscale

def store_scale_file(filename, scale):
    binscale = scale_bin(scale)
    binfile = open(filename, "ab")

    for b in binscale:
        message = bin(b) + "  written!  " + hex(b)
        binfile.write(b.to_bytes(1, byteorder='big'))
        print(message, end="\r")

    binfile.close()