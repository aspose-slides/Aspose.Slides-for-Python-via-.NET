import aspose.slides as slides


def props_modify_builtin_properties(global_opts):
    # Instantiate the Presentation class that represents the Presentation
    with slides.Presentation(global_opts.data_dir + "props_access_modifying_properties.pptx") as presentation:
        # Create a reference to IDocumentProperties object associated with Presentation
        document_properties = presentation.document_properties

        # Set the builtin properties
        document_properties.author = "Aspose.Slides for .NET"
        document_properties.title = "Modifying Presentation Properties"
        document_properties.subject = "Aspose Subject"
        document_properties.comments = "Aspose Description"
        document_properties.manager = "Aspose Manager"

        # Save your presentation to a file
        presentation.save(global_opts.out_dir + "props_modify_builtin_properties_out.pptx", slides.export.SaveFormat.PPTX)
