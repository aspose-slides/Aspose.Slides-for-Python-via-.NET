import aspose.slides as slides

def props_access_builtin_properties():
    #ExStart:AccessBuiltinProperties

    dataDir = "./examples/data/"

    # Instantiate the Presentation class that represents the presentation
    with slides.Presentation(dataDir + "props_builtin.pptx") as pres:
        # Create a reference to IDocumentProperties object associated with Presentation
        documentProperties = pres.document_properties

        # Display the builtin properties
        print("Category : " + documentProperties.category)
        print("Current Status : " + documentProperties.content_status)
        print("Creation Date : " + str(documentProperties.created_time))
        print("Author : " + documentProperties.author)
        print("Description : " + documentProperties.comments)
        print("KeyWords : " + documentProperties.keywords)
        print("Last Modified By : " + str(documentProperties.last_saved_by))
        print("Supervisor : " + documentProperties.manager)
        print("Modified Date : " + str(documentProperties.last_saved_time))
        print("Presentation Format : " + documentProperties.presentation_format)
        print("Last Print Date : " + str(documentProperties.last_printed))
        print("Is Shared between producers : " + str(documentProperties.shared_doc))
        print("Subject : " + documentProperties.subject)
        print("Title : " + documentProperties.title)
    #ExEnd:AccessBuiltinProperties        