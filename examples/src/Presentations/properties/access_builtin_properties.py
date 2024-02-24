import aspose.slides as slides


def props_access_builtin_properties(global_opts):
    # Instantiate the Presentation class that represents the presentation
    with slides.Presentation(global_opts.data_dir + "props_builtin.pptx") as pres:
        # Create a reference to IDocumentProperties object associated with Presentation
        document_properties = pres.document_properties

        # Display the builtin properties
        print("Category : " + document_properties.category)
        print("Current Status : " + document_properties.content_status)
        print("Creation Date : " + str(document_properties.created_time))
        print("Author : " + document_properties.author)
        print("Description : " + document_properties.comments)
        print("KeyWords : " + document_properties.keywords)
        print("Last Modified By : " + str(document_properties.last_saved_by))
        print("Supervisor : " + document_properties.manager)
        print("Modified Date : " + str(document_properties.last_saved_time))
        print("Presentation Format : " + document_properties.presentation_format)
        print("Last Print Date : " + str(document_properties.last_printed))
        print("Is Shared between producers : " + str(document_properties.shared_doc))
        print("Subject : " + document_properties.subject)
        print("Title : " + document_properties.title)
