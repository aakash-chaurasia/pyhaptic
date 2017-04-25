from displayBraille import cellsToChars

while(True) :
    try :
        inp = int(raw_input())
        print cellsToChars[inp]
    except :
        print "combination not found"