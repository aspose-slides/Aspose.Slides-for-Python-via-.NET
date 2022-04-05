import aspose.slides as slides

def props_add_custom_document_properties():
    #ExStart:AddCustomDocumentProperties
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate the Presentation class
    with slides.Presentation() as presentation:

        # Getting Document Properties
        documentProperties = presentation.document_properties

        # Adding Custom properties
        documentProperties.set_custom_property_value("New Custom", 12)
        documentProperties.set_custom_property_value("My Nam", "Mudassir")
        documentProperties.set_custom_property_value("Custom", 124)

        # Getting property name at particular index
        getPropertyName = documentProperties.get_custom_property_name(2)

        # Removing selected property
        documentProperties.remove_custom_property(getPropertyName)

        # Saving presentation
        presentation.save(outDir + "props_add_custom_document_properties_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AddCustomDocumentProperties
