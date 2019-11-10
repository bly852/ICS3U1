print ("---------------------------------------------------------------\n|         2019 Canadian Federal Election Voting Form          |\n---------------------------------------------------------------\n| 1 | Justin Trudeau         | Liberal Party of Canada        |\n| 2 | Andrew Scheer          | Conservative Party of Canada   |\n| 3 | Jagmeet Singh          | New Democratic Party of Canada |\n| 4 | Elizabeth May          | Green Party of Canada          |\n| 5 | Yves-François Blanchet | Bloc Québécois Party of Canada |\n| 6 | Maxime Bernier         | People's Party of Canada       |\n---------------------------------------------------------------")
liberal = 0
pc = 0
ndp = 0
green = 0
quebec = 0
people = 0

voting = 1
while voting == 1:
    try:
        vote = int(input("\nEnter your vote (0 to exit): "))
    except ValueError or NameError:
        vote = 7
    
    if vote == 0:
        voting = 0
    elif vote == 1:
        liberal = liberal+1
    elif vote == 2:
        pc = pc+1
    elif vote == 3:
        ndp = ndp+1
    elif vote == 4:
        green = green+1
    elif vote == 5:
        quebec = quebec+1
    elif vote == 6:
        people = people+1
    else:
        print("That is not a valid vote!")


if liberal > max(pc, ndp, green, quebec, people):
    print ("\nJustin Trudeau won!")
elif pc > max(liberal, ndp, green, quebec, people):
    print ("\nAndrew Scheer Won!")
elif ndp > max(liberal, pc, green, quebec, people):
    print ("\nJagmeet Singh won!")
elif green > max(liberal, pc, ndp, quebec, people):
    print ("\nElizabeth May won!")
elif quebec > max(liberal, pc, ndp, green, people):
    print ("\nYves-François Blanchet won!")
elif people > max(liberal, pc, ndp, green, quebec):
    print ("\nMaxime Bernier won!")


try:
    total = liberal + pc + ndp + green + quebec + people
    
    liberalP = str(round(liberal/total*100)) 
    print ("\nJustin Trudeau earned " + liberalP + "% of the votes.")

    pcP = str(round(pc/total*100))
    print ("Andrew Scheer earned " + pcP + "% of the votes.")

    ndpP = str(round(ndp/total*100))
    print ("Jagmeet Singh earned " + ndpP + "% of the votes.")

    greenP = str(round(green/total*100))
    print ("Elizabeth May earned " + greenP + "% of the votes.")

    quebecP = str(round(quebec/total*100))
    print ("Yves-François Blanchet earned " + quebecP + "% of the votes.")

    peopleP = str(round(people/total*100))
    print ("Maxime Bernier earned " + peopleP + "% of the votes.")
except ZeroDivisionError:
    print("\nThere were no valid votes!")