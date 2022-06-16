from note import Note

def num_to_name(num):
    val = str()

    match num:
        case 0x0c:
            val = 'c'

        case 0x0d:
            val = 'd'

        case 0x0e:
            val = 'e'

        case 0x0f:
            val = 'f'

        case 0x09:
            val = 'g'

        case 0x0a:
            val = 'a'

        case 0x0b:
            val = 'b'

    return val

def num_to_oct(num):
    val = 0

    match num:
        case 0x01:
            val = -1
        case 0x00:
            val = 0
        case 0x02:
            val = 1

    return val

def num_to_sig(num):
    val = str()

    match num:
        case 0x00:
            val = ''

        case 0x01:
            val = '#'

        case 0x02:
            val = 'b'

    return val

def process_values(val_list):
    i = 0
    scale_bank = list()
    scale = list()
    bugs = 0

    for j in range(0, len(val_list)):
        (x,y) = val_list[j]

        note = x
        midi_val = y

        if i == 8:
            scale_bank.append(scale)
            scale = list()
            i = 0

        
        n = decode_note(note, midi_val)
        scale.append(n)
        i = i+1

    return scale_bank


def decode_note(num, midi_val):
    b_sig = num % pow(2,2)
    b_oct = (num >> 2) % pow(2,2)
    b_name = (num >> 4)
    m_val = midi_val

    name = num_to_name(b_name)
    oct = num_to_oct(b_oct)
    sig = num_to_sig(b_sig)

    n = Note(name, oct, sig, m_val)

    return n

def open_scale_file(filename):
    binfile = open(filename, "rb")
    arr = binfile.read()
    binfile.close()

    byte_list = to_list(arr)

    note = 0
    midi_val = 0
    notuple = tuple()
    note_list = list()

    for i in range(0,len(byte_list)):
        b = byte_list[i]

        if i % 2 == 0:
            note = b

        else:
            midi_val = b
            notuple = (note, midi_val)
            note_list.append(notuple)

    sb = process_values(note_list)
    return sb 



def to_list(bytes_arr):
    l = list()
    for b in bytes_arr:
        l.append(b)

    return l