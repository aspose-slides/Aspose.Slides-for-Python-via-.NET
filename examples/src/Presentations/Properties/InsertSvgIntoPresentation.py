import aspose.slides as slides

def insert_svg():
    #ExStart:InsertSvgIntoPresentation
    # The path to the documents directory.

    dataDir = "./examples/data/"
    outDir = "./examples/out/"


    with slides.Presentation() as p:
        with open(dataDir + "image3.svg", "rb") as file:
            svgContent = file.read()

        svgImage = slides.SvgImage(svgContent)
        ppImage = p.images.add_image(svgImage)
        p.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 0, 0, ppImage.width, ppImage.height, ppImage)
        p.save(outDir + "insert_svg_out.pptx", slides.export.SaveFormat.PPTX)

    
    #ExEnd:InsertSvgIntoPresentation
