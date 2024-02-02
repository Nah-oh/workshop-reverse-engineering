# Step 2: Inventory editing

## How to find where the inventory is stored ?

By using the same principle.

## Step 2.1: Spot the 7 differences

Start 2 games:
- Use the shop to load your inventories with various item
- Make sure to have a different amount of those items between the 2 saves
- Open the saves with `vbindiff` and find the relevant address for the player's inventory

Hint: Think about how the inventory should be structured.
The game need to know:
	- How many items do you have in total
	- What kind of item do you have and in which quantity

## Step 2.2: Edit the save

Open one the save in an hexeditor:

- Give the player 99 Master Balls and 42 Helix Fossils
To get the correct ID for items you could play for hours and check your inventory each time you discover a new kind of item.
But the game is almost 25 years old so other people already did it: use [https://web.archive.org/web/20231208053826/https://bulbapedia.bulbagarden.net/wiki/List_of_items_by_index_number_(Generation_I)] for item indexes.
- Recalculate the save's checksum via the provided tool
- Start the game with your modified save and check if it worked

## Step 2.3: Write a program to give the player anything you want.

You may want to use those functions:

- fopen
- fseek
- fwrite
- fclose

You also may want to represent the inventory with an appropriate structure.

Don't forget to fix the save's checksum before testing with the emulator.