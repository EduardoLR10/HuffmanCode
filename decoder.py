import my_io
import utils
from bitstring import BitArray


def decode(filename):
    dict, input = utils.getDict(filename[:-4] + "_compressed.du")

    #print(dict)

    compressedFilename = filename[:-4]
    extension = filename[-4:]

    decompressedFilename = compressedFilename + "Decompressed" + extension

    output = open(decompressedFilename, "wb")

    artifitialBits = int.from_bytes(input.read(1), "big")
    #print(artifitialBits)
    buffer = 0
    buffer2 = 0
    key = ""

    auxPointer = input
    #print(len(auxPointer.read()))

    buffer = input.read(1)
    #print(buffer)
    if buffer:
        while True:
            buffer2 = input.read(1)
            if not buffer2:
                bitArray = (BitArray(buffer)).bin
                for i in range(0, len(bitArray) - artifitialBits):
                    key += str(bitArray[i])
                    if key in dict:
                        output.write(dict[key])
                        key = ""
                break
            else:
                for bit in (BitArray(buffer)).bin:
                    key += str(bit)
                    if key in dict:
                        output.write(dict[key])
                        key = ""
                buffer = buffer2

    return decompressedFilename