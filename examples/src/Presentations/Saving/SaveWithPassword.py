import aspose.slides as slides

def save_with_password():
    #ExStart:SaveWithPassword
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as pres:

        #....do some work here.....

        # Setting Password
        pres.protection_manager.encrypt("pass")

        # Save your presentation to a file
        pres.save(outDir + "save_with_password_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SaveWithPassword