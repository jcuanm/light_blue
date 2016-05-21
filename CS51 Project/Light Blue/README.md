Light Blue

CS51 Final Project - 2015

Collin Styring, Phillip Huang, Javier Cuan-Martinez, Chris Chen.

-------------------------------------------------------------------------------

Explanation of Files:

	Final Submission/code/:

	-lightblue.py
		This is the index file for all user interface and interaction 
		with Light Blue. Within this file function calls to files 
		including chess.py, graph.py, weighting.py exist. 

	-chess.py
		This is a file downloaded from the internet which includes a 
		lot of infrastructure for chess gameplay. This file was 
		created by William McGugan and was found at this URL: 
		http://www.willmcgugan.com/blog/tech/2006/6/18/chesspy/. 
		Many corrections had to be made to this file for it to be 
		run without error.

	-graph.py
		This is the file which handles building and traversing large 
		graphs of chess data. This is where most of the functionality 
		exists for recommending and storing moves.

	-parser.py
		This is the file responsible for parsing PGN files and feeding 
		the graph. This file is used on the front end to build graphs. 
		Note* This file will not need to be run for testing since 
		example graphs are already included in Final Submission/data/.
		The command: "python parser.py" was used to build these graphs.

	-weighting.py
		This file contains all of the weighting algorithmic 
		functionality for info stored in the graphs. This contains 
		weighting algorithms based on elo (player ranking), win/loss 
		data, popularity (move frequency), as well as a lightblue 
		proprietary weighting algorithm that combines the elements 
		above into a more specific value.

	-file_split.py
		This file was used to split large PGN files with multiple chess
		games into many small PGN files, each containing a single chess
		game.This file uses regular expressions to search for 
		"\r\n\r\n\r\n".

	-reg_exp.py
		This is a regular expressions file that was built to extract 
		game result and player info data from PGN files. This data 
		includes which player won, player ranking data, as well as 
		piece color. This data was then used to reccomend moves based 
		on many different game factors.

	-instructions.py
		This file contains detailed instructions for user game play.
		These instructions are printed at the beginning of the script.
		*NOTE* THESE ARE NOT THE INSTRUCTIONS REQUIRED FOR PREPARING 
		AND RUNNING LIGHT BLUE. THESE INSTRUCTIONS ARE LOCATED AT THE 
		BOTTOM OF THIS README.MD FILE. RUNNING LIGHTBLUE WITHOUT THE 
		PREPARATION DESCRIBED AT THE BOTTOM OF THIS FILE IS NOT 
		POSSIBLE.

	-testing.py
		Testing file. *No need to run*

	-valuetest.py
		More thorough value testing file. *No need to run*




	Final Submission/data/

	Graph files ending in elo include moves weighted by the highest elo 
	(player ranking).
	Graph files ending in lightblue include moves weighted using the unique
	 lightblue proprietary weighting algorithm (explained in detail within 
	 final report).
	Graph files ending in pop include moves weighted using 
	 popularity/frequency with which a move was chosen (the more frequent, 
	 the higher the weight).
	Graph files ending in static do not learn from data received from 
	 user game play.
	Graph files ending in wl include moves weighted using the number of 
	 times the particular move led to a win (the more wins, the higher 
	 the weighting).

	/100 games/:
	Raw graph data saved based on different weighting types.
	These graphs include 100 games played by World Master, Magnus Carlsen.

	-Carlsen100elo

	-Carlsen100lightblue

	-Carlsen100pop

	-Carlsen100static

	-Carlsen100wl


	/20 games/:
	Raw graph data saved based on different weighting types.
	These graphs include 20 games played by World Master, Magnus Carlsen.

	-Carlsen20elo

	-Carlsen20lightblue

	-Carlsen20pop

	-Carlsen20static	

	-Carlsen20wl

-------------------------------------------------------------------------------

Instructions for Preparing and Running Light Blue:

	     1) Copy graph data including Magnus Carlsen's 100 games from the 
	     	"Final Submission/data/100 games/" directory into the working 
		directory with the code (Final Submission/code/). *NOTE* IF THE
		CARLSEN100... GRAPHS ARE NOT IN THE CODE DIRECTORY, THE PROGRAM 
		WILL NOT HAVE ANY DATA TO USE FOR RECOMMENDING MOVES, AND 
		THEREFORE WILL NOT RUN. *ASIDE* THE CURRENT CODE IS NOT SET UP 
		TO RUN THE CARLSEN20... FILES, THESE FILES WERE USED DURING 
		PRELIMINARY TESTING AND WERE INCLUDED TO SHOW THOROUGH THOUGHT 
		AND ANALYSIS. THEY ARE NOT TO BE RUN WITH LIGHT BLUE.
	     2) After all 5 Carlsen100... files are moved into the /code/ 
	     	directory, type "python lightblue.py" into the terminal when 
		currently stationed in the /code/ directory and begin using 
		Light Blue. *NOTE* THIS IS THE ONLY PYTHON COMMAND NEEDED TO 
		RUN THIS PROGRAM. ALL FILES ARE CONNECTED WITHIN THE CODE.
	     3) At this point the program is easy to use. Just follow the 
	        instructions printed at the begining of the script and begin 
		playing virtual chess. The current game will be recorded and 
		board configurations will be displayed as well as recommended 
		moves. *NOTE* BE SURE TO INPUT MOVES IN CORRECT STANDARD 
		ALGEBRAIC NOTATION DESIGNED FOR CHESS. THIS IS EXPLAINED IN 
		THE PRINTED SCRIPT INSTRUCTIONS.