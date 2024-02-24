import aspose.slides as slides


def props_add_custom_document_properties(global_opts):
    # Instantiate the Presentation class
    with slides.Presentation() as presentation:
        # Getting Document Properties
        document_properties = presentation.document_properties

        # Adding Custom properties
        document_properties.set_custom_property_value("New Custom", 12)
        document_properties.set_custom_property_value("My Nam", "Mudassir")
        document_properties.set_custom_property_value("Custom", 124)

        # Getting property name at particular index
        property_name = document_properties.get_custom_property_name(2)

        # Removing selected property
        document_properties.remove_custom_property(property_name)

        # Saving presentation
        presentation.save(global_opts.out_dir + "props_add_custom_document_properties_out.pptx",
                          slides.export.SaveFormat.PPTX)
