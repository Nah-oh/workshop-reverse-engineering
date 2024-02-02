import sys
import string

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read())
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)