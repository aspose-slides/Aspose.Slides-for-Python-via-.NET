import aspose.slides as slides

#ExStart:SetFileTypeForAnEmbeddingObject

with slides.Presentation() as pres:
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Add known Ole objects
    with open(dataDir + "test.zip", "rb") as file:
        fileBytes = file.read()

        # Create Ole embedded file info
        dataInfo = slides.dom.ole.OleEmbeddedDataInfo(fileBytes, "zip")

        # Create OLE object
        oleFrame = pres.slides[0].shapes.add_ole_object_frame(150, 20, 50, 50, dataInfo)
        oleFrame.is_object_icon = True


    pres.save(outDir + "shapes_set_ole_object_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:SetFileTypeForAnEmbeddingObject