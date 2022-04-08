import aspose.slides as slides

def props_modify_builtin_properties():
    #ExStart:ModifyBuiltinProperties
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate the Presentation class that represents the Presentation
    with slides.Presentation(dataDir + "props_access_modifying_properties.pptx") as presentation:

        # Create a reference to IDocumentProperties object associated with Presentation
        documentProperties = presentation.document_properties

        # Set the builtin properties
        documentProperties.author = "Aspose.Slides for .NET"
        documentProperties.title = "Modifying Presentation Properties"
        documentProperties.subject = "Aspose Subject"
        documentProperties.comments = "Aspose Description"
        documentProperties.manager = "Aspose Manager"

        # Save your presentation to a file
        presentation.save(outDir + "props_modify_builtin_properties_out.pptx", slides.export.SaveFormat.PPTX)
        #ExEnd:ModifyBuiltinProperties