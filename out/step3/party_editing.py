import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Change the first pokémon into Mewtwo
        sav[0x2F2D] = 0x83

        # Pokémon rename
        sav[0x307E] = 0x8C
        sav[0x307F] = 0x84
        sav[0x3080] = 0x96
        sav[0x3081] = 0x93
        sav[0x3082] = 0x96
        sav[0x3083] = 0x8E
        sav[0x3084] = 0x50
        sav[0x3085] = 0x50
        sav[0x3086] = 0x50
        # Checksum part
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)
