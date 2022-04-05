import aspose.slides as slides

def save_remove_write_protection():
    #ExStart:RemoveWriteProtection
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Opening the presentation file
    with slides.Presentation(dataDir+ "save_remove_write_protection.pptx") as presentation:
        # Checking if presentation is write protected
        if presentation.protection_manager.is_write_protected:
            # Removing Write protection                
            presentation.protection_manager.remove_write_protection()

        # Saving presentation
        presentation.save(outDir + "save_remove_write_protection_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:RemoveWriteProtection