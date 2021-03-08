import utils
import bitstring

# Get input file name
def getFilename():
    print("Insira o arquivo que sofrerá compressão (com extensão):")
    filename = input()
    return filename

# Get a list of bytes from a file
def readBinaryFile(filename):
    
    # Opening input file
    file = open(filename, "rb")

    content = []

    # Reading byte by byte
    while True:
        byte = file.read(1)
        if not byte:
            break
        else:
            #print(byte)
            content.append(byte)

    return content

# Save the compressed file
def compressFile(filename, translateDict):

    # Generating name of compressed file
    cfilename = filename[:-4] + ".du"

    # Opening files to translation
    input = open(filename, "rb")
    output = open(cfilename, "wb")

    # Getting Huffman Tree
    tree = utils.getTree(translateDict)

    # Calculate total overhead size
    overhead = 0
    for i in range(0, len(tree)):
        # Counts all bits as a single byte each
        if (i % 3) == 0 and i != 0:
            overhead += len(tree[i])
        # A single byte
        else:
            overhead += 1

    # Saving the Huffman Tree in the file's header
    for item in tree:
        output.write(item)

    # Start translation of the original file
    bitArray = ""

    # Write into the output file using dictionary, byte by byte
    while True:
        byte = input.read(1)
        if not byte:
            break
        else:
            bitArray += translateDict[byte].decode("utf-8")

    # Counting useless bits
    artificialBits = bytes([0])
    
    # Checking if will be necessary to add artificial bits
    if (len(bitArray) % 8):
        quo = int(int(len(bitArray) / 8) + 1)
        artificialBits = bytes([8 * quo - len(bitArray)])

    # Creating bitstream from string
    deployArray = bitstring.BitArray("0b" + bitArray)

    # Writing how many of the final bits are useless
    output.write(artificialBits)

    # Writing bitstream
    output.write(deployArray.tobytes())

    return [cfilename, overhead]

# Show size information
def showFileSize(option, size, overhead):
    if option == 1:
        print("Original File Size (bytes): " + str(size))
    elif option == 2:
        print("Compressed File Size (bytes): " + str(size))
        print("Compressed File Size (bits) with overhead: " + str(size * 8))
        print("Compressed File Size (bits) without overhead: " + str((size * 8) - (overhead * 8)))
    else:
        print("Decompressed File Size (bytes): " + str(size))

# Show compression ratio
def showCompression(original, compressed):
    print("Compression: " + "{:.2f}".format(100 - ((compressed * 100) / original)) + "%")

# Show entropy on screen
def showEntropy(entropy):
    print("Entropy: " + "{:.2f}".format(entropy))

# Show average length on screen
def showAverageLength(average):
    print("Average Length: " + "{:.2f}".format(average))


