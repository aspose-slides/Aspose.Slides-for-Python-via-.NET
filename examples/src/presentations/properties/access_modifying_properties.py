import aspose.slides as slides


def props_access_modifying_properties(global_opts):
    # Instantiate the Presentation class that represents the PPTX
    with slides.Presentation(global_opts.data_dir + "props_access_modifying_properties.pptx") as presentation:
        # Create a reference to document_properties object associated with Presentation
        document_properties = presentation.document_properties

        # Access and modify custom properties
        for i in range(document_properties.count_of_custom_properties):
            # Display names and values of custom properties
            print("Custom Property Name : " + document_properties.get_custom_property_name(i))
            print("Custom Property Value : " + document_properties.get_custom_property_value(i))

            # Modify values of custom properties
            document_properties.set_custom_property_value(i, "New Value " + str(i + 1))

        # Save your presentation to a file
        presentation.save(global_opts.out_dir + "props_access_modifying_properties_out.pptx",
                          slides.export.SaveFormat.PPTX)
