from ast import operator
from audioop import reverse
import sys, os
import operator
import re

num_arguments = len(sys.argv)
argument_list = (sys.argv)
#print ('Number of arguments:', num_arguments, 'arguments.')
#print ('Argument List:', argument_list)

#checking to see if there are 2 command line arguments (pythong script and the year)
if num_arguments != 2:
    print()
    print("You must provide exactly 2 arguments for this script to run. You did not provide exactly 2 :(")
    print("The first argument must be the name of the script: baseball.py")
    print("The second argument should be the year you would like to calculate the batting averages for.")
    print("As of right now, only years 1930, 1940, 1941, 1942, 1943, and 1944 are supported")
    print("An example of a correct input is: baseball.py 1930")

elif not sys.argv[1].isdigit():
    print()
    print("Your second argument must be an integer. You did not input an integer.")
    print(f"You entered: {sys.argv[1]}")
    print("As of right now, only years 1930, 1940, 1941, 1942, 1943, and 1944 are supported")
    print("An example of a correct input is: baseball.py 1930")

else:
    year = a = int(sys.argv[1])
    #making sure the year provided is one of the supporteed years
    if year not in [1930, 1940, 1941, 1942, 1943, 1944] :
        print()
        print("Your second argument must be one of the supported years")
        print(f"You entered: {year}")
        print("As of right now, only years 1930, 1940, 1941, 1942, 1943, and 1944 are supported")
        print("An example of a correct input is: baseball.py 1930")

    else:
        
        player_dict = {}

        with open(f"cardinals-{year}.txt") as f:
            for line in f:
                
                #filtering out the beginning lines, empty lines, and lines describing who they are playing
                if not line.startswith("=") and not line.startswith("\n") and not line.startswith("#"):
                    # compile, match and group from: https://docs.python.org/3/howto/regex.html
                    #following line of code inspired from: https://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
                    p1 = re.compile('.+?(?= batted)')
                    m1 = p1.match(line)
                    name = m1.group()
                    #print(name)

                    #getting # times batted
                    p2 = re.compile('\d+')
                    m2 = p2.search(line) 
                    batted = int(m2.group())
                    #print(batted)

                    #getting # hits, had to use two regex, to split it up twice
                    p3 = re.compile('\\b\d+\shits\\b')
                    m3 = p3.search(line)
                    hits_string = m3.group()

                    p4 = re.compile('\d+')
                    m4 = p4.search(hits_string)
                    hits = int(m4.group())

                    # if player is already in dictionary, we just add the total bat and total hits to current values
                    if name in player_dict.keys():
                        
                        player_dict[name][0] += batted
                        player_dict[name][1] += hits
                    
                    #if player not already in dictionary, we create dictionary with key being name, value being an array
                    # with 0 index being bats and 1 index being hits
                    else:
                        player_dict[name] = [batted,hits]


        player_avg = {}
        #filling up dictionary with player as key and batting average as value
        for player in player_dict.keys():
            batting_average = format(round(player_dict[player][1]/player_dict[player][0],3), '.3f')
            player_avg[player] = batting_average

        #making either set or list (idk which one) from the dictionary. this makes it sorted
        sorted_player_avg = sorted(player_avg.items(), key = operator.itemgetter(1), reverse = True)
        
        #going over the tuple pairs and printing what we want
        for pair in sorted_player_avg:
            print(f"{pair[0]}: {pair[1]}")

                    


