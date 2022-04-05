import aspose.slides as slides

def props_update_presentation_properties():
    #ExStart:UpdatePresentationProperties

    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # read the info of presentation 
    info = slides.PresentationFactory.instance.get_presentation_info(dataDir + "props_access_modifying_properties.pptx")

    # obtain the current properties 
    props = info.read_document_properties()

    # set the new values of Author and Title fields 
    props.author = "New Author"
    props.title = "New Title"

    # update the presentation with a new values 
    info.update_document_properties(props)
    
    # to save changes to the original file please uncomment the next line
    # info.write_binded_presentation(dataDir + "props_access_modifying_properties.pptx")
    #ExEnd:UpdatePresentationProperties
