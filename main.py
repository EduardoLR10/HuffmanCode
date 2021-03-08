import encoder
import utils
import my_io
import decoder

def main():

    # Reading file name
    filename = my_io.getFilename()

    # Reading input file
    content = my_io.readBinaryFile(filename)

    # Calculating probabilities for each symbol
    probabilities = utils.calculateProbability(content)

    # Saving probabilities for future use
    savedProbability = probabilities.copy()

    # Calculatin entropy
    entropy = utils.calculateEntropy(probabilities)
    
    # Encoding the file
    huffCode = encoder.encode(probabilities)
    
    # Calculating average length
    averageLength = utils.calculateAverageLength(huffCode, savedProbability)
    
    # Getting the name of the compressed file and the overhead tree
    compressedName, overhead = my_io.compressFile(filename, huffCode)

    # Getting the name of the decompressed file after it is decoded
    decompressedFilename = decoder.decode(filename)

    # Calculating files' sizes (original, compressed, decompressed)
    originalSize = utils.calculateSize(filename)
    compressedSize = utils.calculateSize(compressedName)
    decompressedSize = utils.calculateSize(decompressedFilename)

    # Showing information on scree, such as sizes, entropy, average length and comparisons on screen
    my_io.showEntropy(entropy)
    my_io.showAverageLength(averageLength)
    my_io.showFileSize(1, originalSize, 0)
    my_io.showFileSize(2, compressedSize, overhead)
    my_io.showCompression(originalSize, compressedSize)
    my_io.showFileSize(3, decompressedSize, 0)    

if __name__ == "__main__":
    main()