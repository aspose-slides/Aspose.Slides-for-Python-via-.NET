import aspose.slides as slides


#ExStart:SetBackgroundToGradient
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate the Presentation class that represents the presentation file
with slides.Presentation() as pres:
    # Apply Gradiant effect to the Background
    pres.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
    pres.slides[0].background.fill_format.fill_type = slides.FillType.GRADIENT
    pres.slides[0].background.fill_format.gradient_format.tile_flip = slides.TileFlip.FLIP_BOTH

    #Write the presentation to disk
    pres.save(outDir + "background_gradient_format_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetBackgroundToGradient