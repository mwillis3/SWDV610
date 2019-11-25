def lists_vs_dictionaries():
    """Method to utilize examples of a list and dictionary"""
    myList = [i for i in range(1,1500)] # List example
    myDictionary = {111:"Manifestation",222:"Balance",333:"Recognition",
                     444:"On the right path",555:"Change",
                     666:"Shift your perspective",777:"Spiritual Evolution",
                     888:"Increased Abundance",999:"New Chapter",
                     1111:"Awakening Code"} # Dictionary example
    for j in range(len(myList)): # Loop through the established list 
        if myList[j] in myDictionary: # Search the dictionary for the current value in the list
            print(myList[j], myDictionary[myList[j]]) # If exists, print the value and corresponding object in the dictionary. 
        j += 1
            
lists_vs_dictionaries()