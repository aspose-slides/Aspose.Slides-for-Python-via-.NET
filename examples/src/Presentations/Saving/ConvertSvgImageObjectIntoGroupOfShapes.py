import aspose.slides as slides

def save_convert_svg_to_group_of_shapes():
    #ExStart:ConvertSvgImageObjectIntoGroupOfShapes
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir+ "save_convert_svg_to_group_of_shapes.pptx") as pres:
        pFrame = pres.slides[0].shapes[0]
        svgImage = pFrame.picture_format.picture.image.svg_image
        if svgImage != None:
            # Convert svg image into group of shapes
            groupShape = pres.slides[0].shapes.add_group_shape(svgImage, pFrame.frame.x, pFrame.frame.y,
                pFrame.frame.width, pFrame.frame.height)
            # remove source svg image from presentation
            pres.slides[0].shapes.remove(pFrame)

        pres.save(outDir + "save_convert_svg_to_group_of_shapes_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:ConvertSvgImageObjectIntoGroupOfShapes
