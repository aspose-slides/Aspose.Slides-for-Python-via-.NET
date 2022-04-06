import aspose.slides as slides


#ExStart:ChangSmartArtShapeStyle
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "smart_art_access.pptx") as presentation:
    # Traverse through every shape inside first slide
    for shape in presentation.slides[0].shapes:
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
            # Typecast shape to SmartArt
            # Checking SmartArt style
            if shape.quick_style == slides.smartart.SmartArtQuickStyleType.SIMPLE_FILL:
                # Changing SmartArt Style
                shape.quick_style = slides.smartart.SmartArtQuickStyleType.CARTOON

    # Saving Presentation
    presentation.save(outDir + "smart_art_change_quick_style_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangSmartArtShapeStyle