import aspose.slides as slides

def load_format_enumeration():
    #ExStart:LoadFormatEnumeration
    # The path to the documents directory.
    dataDir = "./examples/data/"
    is_old_format = slides.PresentationFactory.instance.get_presentation_info(dataDir + "presentation.ppt").load_format == slides.LoadFormat.PPT95
    #ExEnd:LoadFormatEnumeration
