import encoder
import utils
import my_io
import decoder
import math

def main():

    # Reading file name
    filename = my_io.getFilename()

    # Reading input file
    content = my_io.readBinaryFile(filename)

    # Calculating probabilities for each symbol
    probabilities = utils.calculateProbability(content)
    savedProbability = probabilities.copy()

    entropy = utils.calculateEntropy(probabilities)
    
    huffCode = encoder.encode(probabilities)
    
    averageLength = utils.calculateAverageLength(huffCode, savedProbability)
    
    originalSize = utils.calculateSize(filename)
    
    compressedName, overhead = my_io.compressFile(filename, huffCode)

    #print(overhead)

    compressedSize = utils.calculateSize(compressedName)

    my_io.showEntropy(entropy)
    my_io.showAverageLength(averageLength)
    my_io.showFileSize(1, originalSize, 0)
    my_io.showFileSize(2, compressedSize, overhead)
    my_io.showCompression(originalSize, compressedSize)

    decompressedFilename = decoder.decode(filename)

    decompressedSize = utils.calculateSize(decompressedFilename)

    my_io.showFileSize(3, decompressedSize, 0)    

if __name__ == "__main__":
    main()