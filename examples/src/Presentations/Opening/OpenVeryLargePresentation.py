import aspose.slides as slides
import os

def open_very_large_presentation():
    #ExStart:OpenVeryLargePresentation
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    loadOptions = slides.LoadOptions()
    loadOptions.blob_management_options = slides.BlobManagementOptions()
    loadOptions.blob_management_options.presentation_locking_behavior = slides.PresentationLockingBehavior.KEEP_LOCKED

    with slides.Presentation(dataDir + "large_presentation.pptx", loadOptions) as pres:
        # the huge presentation is loaded and ready to use, but the memory consumption is still low.

        # make any changes to the presentation.
        pres.slides[0].name = "Very large presentation"

        # presentation will be saved to the other file, the memory consumptions still low during saving.
        pres.save(outDir + "veryLargePresentation-copy.pptx", slides.export.SaveFormat.PPTX)

        # can't do that! PermissionError exception will be thrown, because the file is locked while pres objects will
        # not be disposed
        # os.remove(dataDir + "large_presentation.pptx")

    # it's ok to do it here, the source file is not locked by pres object
    # os.remove(dataDir + "large_presentation.pptx")
    
    #ExEnd:OpenVeryLargePresentation

