import aspose.slides as slides
import aspose.pydrawing as drawing

#ExStart:FillShapesPattern
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

    # Set the fill type to Pattern
    shp.fill_format.fill_type = slides.FillType.PATTERN

    # Set the pattern style
    shp.fill_format.pattern_format.pattern_style = slides.PatternStyle.TRELLIS

    # Set the pattern back and fore colors
    shp.fill_format.pattern_format.back_color.color = drawing.Color.light_gray
    shp.fill_format.pattern_format.fore_color.color = drawing.Color.yellow

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_filltype_pattern_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:FillShapesPattern