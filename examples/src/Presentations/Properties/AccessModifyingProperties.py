import aspose.slides as slides

def props_access_modifying_properties():
    #ExStart:AccessModifyingProperties
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instanciate the Presentation class that represents the PPTX
    with slides.Presentation(dataDir + "props_access_modifying_properties.pptx") as presentation:

        # Create a reference to document_properties object associated with Prsentation
        documentProperties = presentation.document_properties

        # Access and modify custom properties
        for i in range(documentProperties.count_of_custom_properties):
            # Display names and values of custom properties
            print("Custom Property Name : " + documentProperties.get_custom_property_name(i))
            print("Custom Property Value : " + documentProperties.get_custom_property_value(i))

            # Modify values of custom properties
            documentProperties.set_custom_property_value(i, "New Value " + str(i + 1))

        # Save your presentation to a file
        presentation.save(outDir + "props_access_modifying_properties_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AccessModifyingProperties