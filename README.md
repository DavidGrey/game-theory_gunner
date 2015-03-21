##Game Theory Gunner

Game Theory Gunner is a simple learning AI made to play the hand game "Shotgun" - It begins without an understanding of the stategy of the game, but learns over time.



###Rules
  The player starts off competing with the AI; both begin with 1 bullet in their gun.
  
Both the player and the AI have 3 options for each round.

####Fire:
- You must have a bullet in order to fire.
- If your opponent reloads, he will die.
- If your opponent fires or blocks, you will both be uninjured.
    
####Reload:
- Increases your ammo count by 1 - You may have up to 6 bullets in your gun at onces.
- Leaves you open to your opponents fire.
    
####Block:
- Protects you from fire for 1 round.
- Both players may block up to 3 times in a row
      
      
The game continues until one player dies or rage quits.

Note that you don't do `make install`; this program is meant to be run from this directory.

### Windows

You have a few options, depending on what you have installed.

- Pure Cygwin: follow the Unix/Linux/OS X instructions above. The resulting DLL can *only* be used with Cygwin programs, so
  
