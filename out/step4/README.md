# Step 4: Stat editing

Editing a Pokemon's statistics (HP, Attack, Defense, etc.) to make it stronger.
Conveniently your Pokemon's stat are stored just after your party composition in the save.

Locate the offset of your first party member stats.

## Step 2.2: Edit the save

Open your save in an hexeditor:

- Replace your first Pokemon with a Mewtwo
- Set the following properties (or just put anything allowing you to beat the game with the save provided in this step, you don't have time to make a 100% legit hacked Pokemon in this worshop):
	- Current HP: 351
	- Level: 100
	- Status condition: OK
	- Type 1: Psychic (the type)
	- Type 2: Psychic (the type)
	- Move 1: Psychic (the move)
	- Move 2, 3, 4: None
	- Original Trainer ID: 97440
	- Experience points: 1 250 000
	- Attack,Defense,Speed,Special EV data: the maximum value
	- IV data: the maximum value
	- Move 1 PP value: any value between 0 and 16
	- Max HP: 416
	- Attack: 350
	- Defense: 306
	- Special: 447
	- Speed: 394 
- Get help from [https://web.archive.org/web/20231217174613/https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_I)]

Hint: different properties have different value range.
There is 165 moves in the game: 1 byte (0-255) is enough to represent 1 move
The maximum amount of experience point is 1250000 so 3 bytes are needed

## Step 2.3: Write a program to modify the stat of the first party member's stats.

Same thing: you may want to use a structure.
Think about how to represent a value on 3 bytes.

You may want to use those functions:

- fopen
- fseek
- fwrite
- fclose

Don't forget to fix the save's checksum before testing with the emulator.

## Conclusion & Bonus

Congratulations ! You can now cheat in a kid's game.

As a bonus you may want to implement a graphical user interface for your save editor.
Multiple tools exist for that: Zenity (Easiest), Tkinter (Easy), Web Interface (Easy enough), GTK, wxWidgets, Qt.
