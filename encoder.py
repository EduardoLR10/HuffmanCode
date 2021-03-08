import heapq

# Pop function for "priority_queue" using heap
def pop(heap):
    return heapq.heappop(heap)

# Push function for "priority_queue" using heap
def push(heap, value):
    heapq.heappush(heap, value)

# Recursive huffman algorithm
def huffmanCode(probabilities, symbolsDict):
    # Stop condition of recursion: less than 2 symbols in the probabilities heap
    if len(probabilities) <= 2:
        return

    # Getting the 2 lowest values using probability as the criteria
    lowest = pop(probabilities)
    sndLowest = pop(probabilities)

    # Creating new symbol from the two lowest ones
    newSymbol = (lowest[0] + sndLowest[0], lowest[1] + sndLowest[1])

    # Adding it to the heap
    push(probabilities, newSymbol)

    # Define values of the lowest ones using created symbol
    symbolsDict[lowest[1]] = newSymbol[1] + bytes('1', 'utf-8')
    symbolsDict[sndLowest[1]] = newSymbol[1] + bytes('0', 'utf-8')

    # Adding to dictionary new symbol
    symbolsDict[newSymbol[1]] = ''

    # Calling function again
    return huffmanCode(probabilities, symbolsDict)

# Recursive auxiliary function to replace all created symbols with their values
def translateSymbols(symbolsDict):

    # Getting the list of binary representations from dictionary
    symbolsList = list(symbolsDict.items())
    
    # The iterating process starts from the end to assure that a representation composed by other symbols can be translated
    for i in range(len(symbolsDict) - 1, -1, -1):
        symbol = symbolsList[i][1]

        # Getting only the unique values from a representation
        setVersion = set(symbol)

        # If the symbol is not composed by only 1s or 0s, it is composed by another symbol
        if(setVersion != {49} and setVersion != {48} and setVersion != {48, 49}):

            # The last symbols in this case is always a 0 or a 1
            lastCharacter = symbol[-1:]

            # Getting the representation without the last bit
            symbol = symbol[:-1]

            # Saving in the dictionary the new value of the symbol
            key = symbolsList[i][0]
            symbolsDict[key] = symbolsDict[symbol] + lastCharacter

    return symbolsDict

# Main function to encode
def encode(probabilities):
    
    # Saving the original symbols to return only used symbols
    originalList = dict.fromkeys(item[1] for item in probabilities)

    # Saving the original symbols for future manipulation
    symbolsDict = dict.fromkeys(item[1] for item in probabilities)
    
    # Executing the Huffman's Code until we have two symbols left
    huffmanCode(probabilities, symbolsDict)
    
    # Managing the remaining 2 or less symbols after Huffman
    remaining1 = pop(probabilities)
    symbolsDict[remaining1[1]] = bytes('1', 'utf-8')

    # Checking the existence of second symbol
    if len(probabilities) == 1:
        remaining2 = pop(probabilities)
        symbolsDict[remaining2[1]] = bytes('0', 'utf-8')

    # Using the result of the Huffman's Code to find values for all symbols recursively (fake symbols included)
    huffmanComplete = translateSymbols(symbolsDict)

    # Filtering only the symbols used in the file itself
    for element in originalList:
        originalList[element] = huffmanComplete[element]

    # Returning final dictionary
    return originalList