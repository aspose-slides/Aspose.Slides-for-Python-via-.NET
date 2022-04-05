import aspose.slides as slides

def save_as_predefined_view_type():
    #ExStart:SaveAsPredefinedViewType
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Opening the presentation file
    with slides.Presentation() as presentation:

        # Setting view type 
        presentation.view_properties.last_view = slides.ViewType.SLIDE_MASTER_VIEW

        # Saving presentation
        presentation.save(outDir + "save_as_predefined_view_type_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SaveAsPredefinedViewType
