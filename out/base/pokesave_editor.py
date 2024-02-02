import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here

        
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)
