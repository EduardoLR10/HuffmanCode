import my_io
import heapq
import math

# Calculate size of file in bytes
def calculateSize(filename):
    return (len(my_io.readBinaryFile(filename)))

# Calculate probability of a given list of content
def calculateProbability(content):
    # Get total amount of elements in content
    total = len(content)

    # Get only the unique elements in content
    elementsSet = set(content)

    # Calculating the probability of each element
    probability = []
    for element in elementsSet:
        heapq.heappush(probability, (content.count(element) / total, element))
    return probability

# Calculate entropy from a list of probabilities
def calculateEntropy(probabilities):
    
    entropy = 0
    for probability in probabilities:
        entropy += -(probability[0] * math.log(probability[0], 2))

    return entropy

# Calculate average length from a given huffman tree and probabilities
def calculateAverageLength(huffCode, probabilities):
    average = 0
    
    for probability in probabilities:
        average += probability[0] * len(huffCode[probability[1]])
    
    return average

# Generate overhead of the compressed file's header from a given huffman tree
def getTree(huffCode):
    tree = []

    # First in the header is the size of the huffman tree
    size = bytes([len(huffCode.items()) - 1])
    tree.append(size)

    # Writing the tree itself
    for key, value in huffCode.items():
        tree.append(key)
        tree.append(bytes([len((str(value))[2:-1])]))
        tree.append(value)

    return tree

# Get the huffman tree from a compressed file
def getDict(compressedFilename):
    file = open(compressedFilename, "rb")

    # Getting the size of the tree
    dict_size = int.from_bytes(file.read(1), "big") + 1

    # Generating the dictionary
    dict = {}
    for i in range(0, dict_size):
        value = file.read(1)
        size = file.read(1)
        key = ""
        for i in range(0, int.from_bytes(size, "big")):
            key += (str(file.read(1)))[2:-1]    
        dict[key] = value             

    return [dict, file]