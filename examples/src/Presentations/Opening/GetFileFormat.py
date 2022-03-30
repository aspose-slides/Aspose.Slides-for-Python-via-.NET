import aspose.slides as slides


def get_file_format():
    #ExStart:get_file_format
    #The path to the documents directory.
    dataDir = "./examples/data/"
    info = slides.PresentationFactory.instance.get_presentation_info(dataDir + "HelloWorld.pptx")
    if info.load_format == slides.LoadFormat.PPTX:
        print("pptx")
    elif info.load_format == slides.LoadFormat.UNKNOWN:
        print("unknown")
    #ExEnd:GetFileFormat

