import sys

def check_validity(name):
    for i in name:
        if ord(i) + 31 < 0x80 or ord(i) + 31 > 0x99:
            print("ERROR : invalid name")
            sys.exit(84)

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here
        if (len(sys.argv) < 3):
            sav[0x2598] = 0x84
            sav[0x2599] = 0x8F 
            sav[0x259A] = 0x88 
            sav[0x259B] = 0x93 
            sav[0x259C] = 0x84 
            sav[0x259D] = 0x82
            sav[0x259E] = 0x87 
        else:
            rename = sys.argv[2]
            check_validity(rename)
            for i in range(0x259F - 0x2598):
                sav[i + 0x2598] = ord(rename[i]) + 31 if len(rename) > i else 0x50

        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0)
        f.write(sav)
