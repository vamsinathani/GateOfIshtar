# GateOfIshtar

GOAL:
   This game is about a champion crossing the gate which is guarded. Champion would lose his HP if attacked by the guards. 

gate_of_ishtar.py
    This is the file with all the code implementation. Also find gate_of_ishtar.exe file under dist for running this game
	
STEPS TO RUN THIS PROJECT:
1) Download the .exe file in dist folder on this project ( Example: C:\gate_of_ishtar\dist\gate_of_ishtar.exe)
2) Double click on .exe file
3) User will be prompted to enter CHAMPION and DATE_TIME_INTERVALS details
4) Valid CHAMPION values are ['Human', 'Wizard', 'Spirit', 'Giant', 'Vampire']
   DATE_TIME_INTERVALS have to be provided in this format ['YYYY-MM-DD HH:MM'] 
   If you are providing more than one DATE_TIME_INTERVAL they have to be comma separated. say: ['YYYY-MM-DD HH:MM', 'YYYY-MM-DD HH:MM']
5) Based on the user inputs, the output would mention how much HP the champion has lost and by whom the champion was attacked
6) Special use cases like "Holly days", "Invincible champion", "Champion cannot lose HP more than once every hour" are also taken into account. 

