import aspose.slides as slides


#ExStart:ReplacingText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX
with slides.Presentation(dataDir + "text_default_fonts.pptx") as pres:
    # Access first slide
    sld = pres.slides[0]

    # Iterate through shapes to find the placeholder
    for shp in sld.shapes:
        if shp.placeholder is not None:
            # Change the text of each placeholder
            shp.text_frame.text = "This is Placeholder"

    # Save the PPTX to Disk
    pres.save(outDir + "text_replacing_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ReplacingText