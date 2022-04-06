import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:SetAlternativeText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp1 = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 40, 150, 50)
    shp2 = sld.shapes.add_auto_shape(slides.ShapeType.MOON, 160, 40, 150, 50)
    shp2.fill_format.fill_type = slides.FillType.SOLID
    shp2.fill_format.solid_fill_color.color = drawing.Color.gray

    for shape in sld.shapes:
        if type(shape) == slides.AutoShape:
            shape.alternative_text = "User Defined"

    # Save presentation to disk
    pres.save(outDir + "shapes_set_alternative_text_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetAlternativeText