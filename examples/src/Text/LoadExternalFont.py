import aspose.slides as slides
import aspose.pydrawing as drawing

# ExStart:LoadExternalFont

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"


# loading presentation uses SomeFont which is not installed on the system
with slides.Presentation() as pres:
    # load SomeFont from file into the byte array

    with open(dataDir + "CustomFonts.ttf", "rb") as fs:
        fontData = fs.read()

    # load font represented as byte array
    slides.FontsLoader.load_external_font(fontData)

# ExEnd:LoadExternalFont

