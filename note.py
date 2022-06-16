class Note:
    def __init__(self, name: str, oct: int, sig: str, midi_val: int):
        self.name = name
        self.oct = oct
        self.sig = sig
        self.midi_val = midi_val

    def C(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 36 
            case(-1, "#"):
                val = 37
            case(-1, "b"):
                val = 35

            case(0, ""):
                val = 48
            case(0, "#"):
                val = 49
            case(0, "b"): 
                val = 47

            case(1, ""):
                val = 60
            case(1, "#"):
                val = 61
            case(1, "b"):
                val = 59

        #assert val != 0

        return Note("c", oct, sig, val)

    def D(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 38
            case(-1, "#"):
                val = 39
            case(-1, "b"):
                val = 37

            case(0, ""):
                val = 50
            case(0, "#"):
                val = 51
            case(0, "b"): 
                val = 49

            case(1, ""):
                val = 62
            case(1, "#"):
                val = 63
            case(1, "b"):
                val = 61   

        #assert val != 0

        return Note("d", oct, sig, val)

    def E(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 40 
            case(-1, "#"):
                val = 41
            case(-1, "b"):
                val = 39

            case(0, ""):
                val = 52
            case(0, "#"):
                val = 53
            case(0, "b"): 
                val = 51

            case(1, ""):
                val = 64
            case(1, "#"):
                val = 65
            case(1, "b"):
                val = 63   

        #assert val != 0
        return Note("e", oct, sig, val)

    def F(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 41 
            case(-1, "#"):
                val = 42
            case(-1, "b"):
                val = 40

            case(0, ""):
                val = 53
            case(0, "#"):
                val = 54
            case(0, "b"): 
                val = 52

            case(1, ""):
                val = 65
            case(1, "#"):
                val = 66
            case(1, "b"):
                val = 64   

        #ssert val != 0
        return Note("f", oct, sig, val)

    def G(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 43 
            case(-1, "#"):
                val = 44
            case(-1, "b"):
                val = 42

            case(0, ""):
                val = 55
            case(0, "#"):
                val = 56
            case(0, "b"): 
                val = 54

            case(1, ""):
                val = 67
            case(1, "#"):
                val = 68
            case(1, "b"):
                val = 66   

        #assert val != 0
        return Note("g", oct, sig, val)

    def A(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 45 
            case(-1, "#"):
                val = 46
            case(-1, "b"):
                val = 44

            case(0, ""):
                val = 57
            case(0, "#"):
                val = 58
            case(0, "b"): 
                val = 56

            case(1, ""):
                val = 69
            case(1, "#"):
                val = 70
            case(1, "b"):
                val = 68   

        #assert val != 0
        return Note("a", oct, sig, val)

    def B(oct, sig):
        val = 0

        match (oct, sig):
            case(-1, ""):
                val = 47 
            case(-1, "#"):
                val = 48
            case(-1, "b"):
                val = 46

            case(0, ""):
                val = 59
            case(0, "#"):
                val = 60
            case(0, "b"): 
                val = 58

            case(1, ""):
                val = 71
            case(1, "#"):
                val = 72
            case(1, "b"):
                val = 70   

        #assert val != 0
        return Note("b", oct, sig, val)

    def print_note(self):
        print("Note(" + self.name + ", " + str(self.oct) + ", " + self.sig + ", " + str(self.midi_val) + ")")

    def copy(object):
        ze_copy = Note(object.name, object.oct, object.sig, object.midi_val)
        return ze_copy