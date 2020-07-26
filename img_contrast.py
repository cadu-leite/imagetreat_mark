from PIL import Image

'''
Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)

Io                                - Output pixel valu
Ii                                 - Input pixel valu
Mini                         - Minimum pixel value in the input imag
Maxi                        - Maximum pixel value in the input imag
Mino                        - Minimum pixel value in the output imag
Maxo                       - Maximum pixel value in the output image
'''
def normalizeRed(intensity):

    iI = intensity
    minI = 86
    maxI = 230
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeGreen(intensity):
    iI = intensity
    minI = 90
    maxI = 225
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeBlue(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def contrast(img, level):
    # imageObject = Image.open("./glare4.jpg")

    # Split the red, green and blue bands from the Image
    multiBands = img.split()

    # Apply point operations that does contrast stretching on each color band
    normalizedRedBand = multiBands[0].point(normalizeRed)
    normalizedGreenBand = multiBands[1].point(normalizeGreen)
    normalizedBlueBand = multiBands[2].point(normalizeBlue)

    # Create a new image from the contrast stretched red, green and blue brands
    normalizedImage = Image.merge(
        "RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))

    # Display the image before contrast stretching
    img.show()

    # Display the image after contrast stretching
    normalizedImage.show()
