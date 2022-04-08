import aspose.slides as slides

#ExStart:ChangeSmartArtShapeColorStyle
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Creating a presentation instance
with slides.Presentation(dataDir + "smart_art_access.pptx") as presentation:

    # Traverse through every shape inside first slide
    for shape in presentation.slides[0].shapes:
    
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
        
            # Typecast shape to SmartArt
            # Checking SmartArt color type
            if shape.color_style == slides.smartart.SmartArtColorType.COLORED_FILL_ACCENT1:
            
                # Changing SmartArt color type
                shape.color_style = slides.smartart.SmartArtColorType.COLORFUL_ACCENT_COLORS

    # Saving Presentation
    presentation.save(outDir + "smart_art_change_color_style_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangeSmartArtShapeColorStyle
