import aspose.slides as slides


def props_access_properties():
    # Accessing the Document Properties of a Password Protected Presentation without Password
    # creating instance of load options to set the presentation access password
    load_options = slides.LoadOptions()

    # Setting the access password to None
    load_options.password = None

    # Setting the access to document properties
    load_options.only_load_document_properties = True

    # Opening the presentation file by passing the file path and load options to the constructor of Presentation class
    with slides.Presentation() as pres:
        # Getting Document Properties
        document_properties = pres.document_properties
        print("Name of Application : " + document_properties.name_of_application)
