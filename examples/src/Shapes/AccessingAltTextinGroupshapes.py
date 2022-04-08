import aspose.slides as slides

def shapes_accessing_alt_text():
    #ExStart:AccessingAltTextinGroupshapes
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(dataDir + "shapes_accessing_alt_text.pptx") as pres:
        # Get the first slide
        sld = pres.slides[0]

        for shape in sld.shapes:
            if type(shape) is slides.GroupShape:
                # Accessing the group shape.

                for shape2 in shape.shapes:
                    # Accessing the AltText property
                    print(shape2.alternative_text)
    #ExEnd:AccessingAltTextinGroupshapes

shapes_accessing_alt_text()
