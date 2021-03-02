import my_io
import heapq
import math

def calculateSize(filename):
    return (len(my_io.readBinaryFile(filename)))

def calculateProbability(content):
    total = len(content)
    elementsSet = set(content)
    probability = []
    for element in elementsSet:
        heapq.heappush(probability, (content.count(element) / total, element))
    return probability

def calculateEntropy(probabilities):
    
    entropy = 0

    for probability in probabilities:
        entropy += -(probability[0] * math.log(probability[0], 2))

    return entropy

def calculateAverageLength(huffCode, probabilities):
    average = 0
    
    for probability in probabilities:
        average += probability[0] * len(huffCode[probability[1]])
    
    return average


def getTree(huffCode):
    tree = []
    size = bytes([len(huffCode.items()) - 1])
    #print(size)

    tree.append(size)

    for key, value in huffCode.items():
        tree.append(key)
        tree.append(bytes([len((str(value))[2:-1])]))
        tree.append(value)

    return tree

def getDict(compressedFilename):
    file = open(compressedFilename, "rb")

    dict_size = int.from_bytes(file.read(1), "big") + 1

    dict = {}

    for i in range(0, dict_size):
        value = file.read(1)
        if not value:
            break
        size = file.read(1)
        key = ""
        for i in range(0, int.from_bytes(size, "big")):
            key += (str(file.read(1)))[2:-1]    
        dict[key] = value             

    #print(dict)

    return [dict, file]