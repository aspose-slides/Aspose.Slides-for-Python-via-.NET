import aspose.slides as slides
import aspose.pydrawing as drawing

#ExStart:SubstitutePictureTitleOfOLEObjectFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    image = None
    slide = pres.slides[0]

    # Add Ole objects
    with open(dataDir + "book.xlsx", "rb") as file:
        allbytes = file.read()

    dataInfo = slides.dom.ole.OleEmbeddedDataInfo(allbytes, "xlsx")

    oof = slide.shapes.add_ole_object_frame(20, 20, 50, 50, dataInfo)
    oof.is_object_icon = True

    # Add image object
    image = pres.images.add_image(drawing.Bitmap(dataDir + "image1.jpg"))
    oof.substitute_picture_format.picture.image = image

    # Set caption to OLE icon
    oof.substitute_picture_title = "Caption example"

#ExEnd:SubstitutePictureTitleOfOLEObjectFrame
