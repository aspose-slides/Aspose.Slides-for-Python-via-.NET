import aspose.slides as slides
import aspose.pydrawing as drawing

#ExStart:FormattedRectangle
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"


# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:

    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 50)

    # Apply some formatting to rectangle shape
    shp.fill_format.fill_type = slides.FillType.SOLID
    shp.fill_format.solid_fill_color.color = drawing.Color.chocolate

    # Apply some formatting to the line of rectangle
    shp.line_format.fill_format.fill_type = slides.FillType.SOLID
    shp.line_format.fill_format.solid_fill_color.color = drawing.Color.black
    shp.line_format.width = 5

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_formatted_rectangle_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:FormattedRectangle