import aspose.slides as slides

#ExStart:CloneShapes

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class
with slides.Presentation(dataDir + "shapes_clone.pptx") as srcPres:
    sourceShapes = srcPres.slides[0].shapes
    blankLayout = srcPres.masters[0].layout_slides.get_by_type(slides.SlideLayoutType.BLANK)
    destSlide = srcPres.slides.add_empty_slide(blankLayout)
    destShapes = destSlide.shapes
    destShapes.add_clone(sourceShapes[1], 50, 150 + sourceShapes[0].height)
    destShapes.add_clone(sourceShapes[2])                 
    destShapes.insert_clone(0, sourceShapes[0], 50, 150)

    # Write the PPTX file to disk
    srcPres.save(outDir + "shapes_clone_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:CloneShapes




