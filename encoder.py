import heapq
import my_io
import utils

def pop(heap):
    return heapq.heappop(heap)

def push(heap, value):
    heapq.heappush(heap, value)

def huffmanCode(probabilities, symbolsDict):
    if len(probabilities) <= 2:
        return

    lowest = pop(probabilities)
    sndLowest = pop(probabilities)

    newSymbol = (lowest[0] + sndLowest[0], lowest[1] + sndLowest[1])

    push(probabilities, newSymbol)

    symbolsDict[lowest[1]] = newSymbol[1] + bytes('1', 'utf-8')
    symbolsDict[sndLowest[1]] = newSymbol[1] + bytes('0', 'utf-8')
    symbolsDict[newSymbol[1]] = ''
    return huffmanCode(probabilities, symbolsDict)


def completeSymbols(symbolsDict):
    symbolsList = list(symbolsDict.items())
    for i in range(len(symbolsDict) - 1, -1, -1):
        symbol = symbolsList[i][1]
        setVersion = set(symbol)
        if(setVersion != {49} and setVersion != {48} and setVersion != {48, 49}):
            lastCharacter = symbol[-1:]
            symbol = symbol[:-1]
            key = symbolsList[i][0]
            symbolsDict[key] = symbolsDict[symbol] + lastCharacter

    return symbolsDict

def encode(probabilities):
    
    # Saving the original symbols to return only used symbols
    originalList = dict.fromkeys(item[1] for item in probabilities)

    # Saving the original symbols for future manipulation
    symbolsDict = dict.fromkeys(item[1] for item in probabilities)
    
    # Executing the Huffman's Code until we have two symbols left
    huffmanCode(probabilities, symbolsDict)
    
    # Managing the remaining 2 symbols after Huffman
    remaining1 = pop(probabilities)
    symbolsDict[remaining1[1]] = bytes('1', 'utf-8')

    if len(probabilities) == 1:
        remaining2 = pop(probabilities)
        symbolsDict[remaining2[1]] = bytes('0', 'utf-8')

    # Using the result of the Huffman's Code to find values for all symbols (fake symbols included)
    huffmanComplete = completeSymbols(symbolsDict)

    # Filtering only the symbols used in the file
    for element in originalList:
        originalList[element] = huffmanComplete[element]

    # Returning final dictionary
    return originalList