from note import Note
import random
import abjad
from midiutil import MIDIFile
import time
import sys
import write_binary as wb
import read_binary as rb
import multiprocessing as mp

test_scale = [
    Note.C(0, '#'),
    Note.D(0, ''),
    Note.E(0, 'b'),
    Note.F(0, ''),
    Note.G(0, ''),
    Note.A(0, 'b'),
    Note.B(0, 'b')
]

scale_1 = [
    Note.D(0, '#'),
    Note.F(0, ''),
    Note.G(0, 'b'),
    Note.A(0, 'b'),
    Note.A(0, ''),
    Note.B(0, ''),
    Note.C(1, ''),
]

scale_2 = [
    Note.E(0, ''),
    Note.F(0, ''),
    Note.G(0, ''),
    Note.A(0, 'b'),
    Note.B(0, 'b'),
    Note.C(1, 'b'),
    Note.D(1, 'b')
]

scale_3 = [
    Note.G(0, '#'),
    Note.B(0, ''),
    Note.C(1, '#'),
    Note.D(1, ''),
    Note.E(1, ''),
    Note.F(1, '#'),
    Note.F(1, '')
]

scale_4 = [
    Note.A(0, ''),
    Note.B(0, 'b'),
    Note.C(1, ''),
    Note.D(1, 'b'),
    Note.E(1, 'b'),
    Note.F(1, '#'),
    Note.G(1, '')
]

scale_5 = [
    Note.D(0, '#'),
    Note.F(0, ''),
    Note.G(0, ''),
    Note.A(0, 'b'),
    Note.B(0, 'b'),
    Note.B(0, ''),
    Note.C(1, '')
]



def gen_patterns():
    pattern_base = list()

    while len(pattern_base) != 243:
        pattern = list()
        for i in range(0, 5):
            num = random.randrange(-1, 2)

            while num == 2:
                num = random.randrange(-1, 2)

            pattern.append(num)


        if pattern not in pattern_base:
            pattern_base.append(pattern)
    
    return pattern_base

def shift(hold1, hold2, scale, pattern):
    new_scale = list()
    first = scale[hold1]
    last = scale[hold2]

    changed_index = 0

    for i in scale:

        if i == first or i == last:
            new_scale.append(i)

        else:
            shift_val = pattern[changed_index]

            note = i

            note.oct = note.oct + shift_val
            
            match shift_val:
                case -1:
                    note.midi_val = note.midi_val - 12

                case 0:
                    note.midi_val = note.midi_val

                case 1:
                    note.midi_val = note.midi_val + 12

            if note.oct > 1:
                note.oct = 1
                note.midi_val = note.midi_val - 12

            elif note.oct < -1:
                note.oct = -1    
                note.midi_val = note.midi_val + 12        

            new_scale.append(note)
            changed_index = changed_index + 1

    scale_finish = Note.copy(first)
    scale_finish.oct = scale_finish.oct + 1
    new_scale.append(scale_finish)

    return new_scale

def pick_first_last():
    fl_bank = list()
    toopl = tuple()
    changed = False

    for j in range(0, 7):
        first = j

        for i in range(0, 7):
            last = i

            if first == last:
                last = last + 1
                toopl = (first, last)
                chaged = True
                fl_bank.append(toopl)

            else:
                toopl = (first, last)

                if not changed:
                    last = last + 1
                    changed = False
                    fl_bank.append(toopl)


    doubled = tuple()
    for k in fl_bank:
        if k == doubled:
            fl_bank.remove(k)

        else:
            doubled = k

    fl_bank = undouble(fl_bank)

    #Reverse-double check
    for j in fl_bank:
        if fl_bank.index(j) == 0:
            prev = j

        else:
            prev = fl_bank[fl_bank.index(j) - 1]

            for i in fl_bank:
                curr_a = i[0]
                curr_b = i[1]

                prev_a = prev[0]
                prev_b = prev[1]

                if curr_a == prev_b and prev_a == curr_b:
                    fl_bank.remove(i)

    fl_bank.remove(fl_bank[-1])

    #print(fl_bank)

    return fl_bank


def print_scale(scale):
    for i in scale:
        Note.print_note(i)

def note_to_str(note: Note):
    strong = str()
    strong = strong + note.name

    match note.sig:
        case ' ':
            strong = strong + ''

        case '#':
            strong = strong + 's'

        case 'b':
            strong = strong + 'f'

    match note.oct:
        case -1:
            strong = strong +  ""

        case 0:
            strong = strong + "'"

        case 1:
            strong = strong + "''"

    return strong

def render_scale(new_scale):
    strincc = str()
    for n in new_scale:
        n_str = note_to_str(n)

        if new_scale.index(n) == 0:
            n_str = n_str + "8"

        elif new_scale.index(n) == (len(new_scale)-1):
            n_str = n_str + "8"

        strincc = strincc + " " + n_str

    #print(strincc)
    return strincc


def midi_scale(new_scale, t, mf: MIDIFile):
    #mf = MIDIFile(1)
    track = 0

    time = 0
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)  

    channel = 0
    volume = 100

    for n in new_scale:
        pitch = n.midi_val
        time  = t
        duration = 1
        mf.addNote(track, channel, pitch, time, duration, volume)


def chord_gen(scale, filename):
    tic: float = time.perf_counter()

    msg = "generate patterns...               >-----"
    print(msg, end="\r")
    patterns = gen_patterns()
    time.sleep(1)

    msg = "generate pickup patterns...        >>----"
    print(msg, end="\r")
    last_first = pick_first_last()
    time.sleep(1)
    
    msg = "preparing for chord generation...  >>>---"
    print(msg, end="\r")
    suaus = str()
    chord_file = MIDIFile(1)
    t = 0
    time.sleep(1)
    
    #print("Pattern amount: " + str(len(patterns)))
    #print("LF amount: " + str(len(last_first)))

    for (x,y) in last_first:
        for p in patterns: 
            msg = "generating chord " + str(t) + "        >>>>---"
            new_scale = shift(x, y, scale, p)
            #print_scale(new_scale)
            res = render_scale(new_scale)
            midi_scale(new_scale, t, chord_file)
            suaus = suaus + " " + res
            t = t+1
            #print(res)
            print(msg, end="\r")

            msg = "writing srf file                  >>>>>--"
            print(msg, end = "\r")
            srf_name = filename + ".srf"
            wb.store_scale_file(srf_name, new_scale)

            #input("Press enter....")

    msg = "generate midi file...             >>>>>>-"
    print(msg, end = "\r")
    mid_file = filename + ".mid"
    with open(mid_file, "wb") as outf:
        chord_file.writeFile(outf)


    msg = "rendering score...                >>>>>>>"
    print(msg, end="\r")
    voice = abjad.Voice(suaus, name="Voice_1")
    staff = abjad.Staff([voice], name="Staff_1")
    pool = mp.Pool(2)
    pool.map(abjad.show, [staff])
    #abjad.show(staff)
    
    toc: float = time.perf_counter()
    print("generated " + str(t) + "chords in " + str(toc-tic) + "seconds")

def open_srf(filename):
    tic: float = time.perf_counter()

    msg = "opening and reading srf file      >----"
    srf_file = filename + ".srf"
    print(msg, end= "\r")
    scales = rb.open_scale_file(filename)

    msg = "preparing for scale rendering...  >>---"
    print(msg, end= "\r")
    t = 0
    chord_file = MIDIFile(1)
    suaus = str()

    for s in scales:
        msg = "reading chord " + str(t) + "  >>>--"
        print(msg, end= "\r")
        res = render_scale(s)
        midi_scale(s, t, chord_file)
        t = t+1
        suaus = suaus + " " + res

    msg = "generate midi file...             >>>>-"
    print(msg, end = "\r")
    mid_file = "r_" + filename + ".mid"
    with open(mid_file, "wb") as outf:
        chord_file.writeFile(outf)


    msg = "rendering score...                >>>>>"
    print(msg, end="\r")
    voice = abjad.Voice(suaus, name="Voice_1")
    staff = abjad.Staff([voice], name="Staff_1")
    abjad.show(staff)

    toc: float = time.perf_counter()
    print("generated " + str(t) + "chords in " + str(toc-tic) + "seconds")


def main():
    argv = sys.argv

    if len(argv) == 2:
        filename = argv[1]
        open_srf(filename)

    else:
        chord_gen(scale_1, "scales/scale_x")
        #chord_gen(scale_2, "scales/scale_2")
        #chord_gen(scale_3, "scales/scale_3")
        #chord_gen(scale_4, "scales/scale_4")
        #chord_gen(scale_5, "scales/scale_5")


def undouble(list):
    doubled = tuple()
    for k in list:
        if k == doubled:
            list.remove(k)

        else:
            doubled = k

    return list

if __name__ == "__main__":
    main()

