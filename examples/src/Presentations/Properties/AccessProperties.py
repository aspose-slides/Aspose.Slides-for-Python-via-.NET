import aspose.slides as slides

def props_access_properties():
    #ExStart:AccessProperties
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Accessing the Document Properties of a Password Protected Presentation without Password
    # creating instance of load options to set the presentation access password
    loadOptions = slides.LoadOptions()

    # Setting the access password to None
    loadOptions.password = None

    # Setting the access to document properties
    loadOptions.only_load_document_properties = True

    # Opening the presentation file by passing the file path and load options to the constructor of Presentation class
    with slides.Presentation() as pres:

        # Getting Document Properties
        docProps = pres.document_properties

        print("Name of Application : " + docProps.name_of_application)
    #ExEnd:AccessProperties