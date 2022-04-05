import aspose.slides as slides

def save_to_file():
    #ExStart:SaveToFile
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as presentation:

        #...do some work here...

        # Save your presentation to a file
        presentation.save(outDir + "save_to_file_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SaveToFile