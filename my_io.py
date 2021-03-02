import utils
import bitstring

def getFilename():
    print("Insira o arquivo que sofrerá compressão (com extensão):")
    filename = input()
    return filename

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

def compressFile(filename, translateDict):

    # Generating name of compressed file
    cfilename = filename[:-4] + "_compressed.du"

    # Opening files to translation
    input = open(filename, "rb")
    output = open(cfilename, "wb")

    # Saving Huffman Tree in the file's header
    tree = utils.getTree(translateDict)

    overhead = 0
    for i in range(0, len(tree)):
        if (i % 3) == 0 and i != 0:
            overhead += len(tree[i])
        else:
            overhead += 1

    for item in tree:
        output.write(item)

    # Start translation of the original file
    bitArray = ""

    #print(translateDict)

    # Write into the output file using dictionary
    while True:
        byte = input.read(1)
        if not byte:
            break
        else:
            bitArray += translateDict[byte].decode("utf-8")

    # Counting useless bits
    artificialBits = bytes([0])
    
    if (len(bitArray) % 8):
        quo = int(int(len(bitArray) / 8) + 1)
        artificialBits = bytes([8 * quo - len(bitArray)])

    #print((format(artificialBits, 'b')))
    deployArray = bitstring.BitArray("0b" + bitArray)

    #print((deployArray.bin))

    #print((deployArray.tobytes()))
    #print(artificialBits)
    output.write(artificialBits)
    output.write(deployArray.tobytes())

    return [cfilename, overhead]

def showFileSize(option, size, overhead):
    if option == 1:
        print("Original File Size (bytes): " + str(size))
    elif option == 2:
        print("Compressed File Size (bytes): " + str(size))
        print("Compressed File Size (bits) with overhead: " + str(size * 8))
        print("Compressed File Size (bits) without overhead: " + str((size * 8) - (overhead * 8)))
    else:
        print("Decompressed File Size (bytes): " + str(size))

def showCompression(original, compressed):
    print("Compression: " + "{:.2f}".format(100 - ((compressed * 100) / original)) + "%")

def showEntropy(entropy):
    print("Entropy: " + "{:.2f}".format(entropy))

def showAverageLength(average):
    print("Average Length: " + "{:.2f}".format(average))


