import aspose.slides as slides

def shapes_add_ole_object_frame():
    #ExStart:AddOLEObjectFrame

    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate Prseetation class that represents the PPTX
    with slides.Presentation() as pres:
        # Access the first slide
        sld = pres.slides[0]

        # Load an excel file to stream
        with open(dataDir + "book.xlsx", "rb") as fs:
            bytes = fs.read()
        
            # Create a data object for embedding
            dataInfo = slides.dom.ole.OleEmbeddedDataInfo(bytes, "xlsx")

            # Add an Ole Object Frame shape
            oleObjectFrame = sld.shapes.add_ole_object_frame(0, 0, pres.slide_size.size.width, pres.slide_size.size.height, dataInfo)

            # Write the PPTX to disk
            pres.save(outDir + "shapes_add_ole_object_frame_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:AddOLEObjectFrame