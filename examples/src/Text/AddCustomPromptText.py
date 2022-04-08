import aspose.slides as slides


#ExStart:AddCustomPromptText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_add_custom_placeholder_text.pptx") as pres:
    slide = pres.slides[0]
    for shape in slide.slide.shapes: # iterate through the slide
        if shape.placeholder != None and type(shape) is slides.AutoShape:
            text = ""
            if shape.placeholder.type == slides.PlaceholderType.CENTERED_TITLE: # title - the text is empty, PowerPoint displays "Click to add title". 
                text = "Click to add custom title"
            elif shape.placeholder.type == slides.PlaceholderType.SUBTITLE: # the same for subtitle.
                text = "Click to add custom subtitle"

            shape.text_frame.text = text

            print("Placeholder with text: {0}".format(text))

    pres.save(outDir + "text_add_custom_placeholder_text_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:AddCustomPromptText
