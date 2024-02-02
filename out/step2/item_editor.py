import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here
        
        # Checksum part
        checksum = 0xff
        sav[0x25C9] = 0x02
        sav[0x25CA] = 0x01
        sav[0x25CB] = 0x63
        sav[0x25CC] = 0x10
        sav[0x25CD] = 0x2a
        sav[0x25CE] = 0xFF
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)
