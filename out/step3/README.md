# Step 3: Party editing

## How to find where the party is stored ?

You guessed it.

## Step 2.1: Spot the 7 differences

Start 2 games:
- Use the menu to switch your party order
- Open the saves with `vbindiff` and find the relevant address for the party

Hint: Think about how the party should be structured.
The game need to know:
	- How many Pokemon do you have in total in your party
	- What is the specy of each pokemon

## Step 2.2: Edit the save

Open one the save in an hexeditor:

- Replace your first Pokemon with a Mewtwo
To get the correct ID for Pokemon you could play for hours and check your inventory each time you catch a new Pokemon.
But the game is almost 25 years old so other people already did it: use [https://web.archive.org/web/20210308105333/https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_I)] for Pokemon indexes.
- Recalculate the save's checksum via the provided tool
- Start the game with your modified save and check if it worked

## Step 2.3: Write a program to give the player any Pokemon in his party.

You may want to use those functions:

- fopen
- fseek
- fwrite
- fclose

Don't forget to fix the save's checksum before testing with the emulator.