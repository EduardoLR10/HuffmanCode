import utils
from bitstring import BitArray

# Main function to decode a file
def decode(filename):

    # Getting the huffman tree of the file and the compressed file's file pointer
    dict, input = utils.getDict(filename[:-4] + ".du")

    # Manipulating strings to generate the new name of the decompressed file
    compressedFilename = filename[:-4]
    extension = filename[-4:]
    decompressedFilename = compressedFilename + "Decompressed" + extension

    # Reading the artifitial bits of the last byte of the compressed file
    artifitialBits = int.from_bytes(input.read(1), "big")

    # Auxiliary variables
    buffer = 0
    buffer2 = 0
    key = ""

    # Start writing the decompressed file and reading the content of the compressed one
    output = open(decompressedFilename, "wb")
    buffer = input.read(1)
    if buffer:
        while True:
            buffer2 = input.read(1)
            # If the second read was not sucessful, it means that buffer contains the last byte of the compressed file
            if not buffer2:
                bitArray = (BitArray(buffer)).bin

                # In this case, we just read the bits that we know are useful
                for i in range(0, len(bitArray) - artifitialBits):
                    key += str(bitArray[i])
                    if key in dict:
                        output.write(dict[key])
                        key = ""
                break
            else:
                # If buffer2 contains a byte, we are not at the end of the compressed file
                for bit in (BitArray(buffer)).bin:
                    key += str(bit)

                    # Check if the accumulated bits form a known key in the tree
                    if key in dict:
                        output.write(dict[key])
                        key = ""

                buffer = buffer2

    return decompressedFilename