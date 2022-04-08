import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:FormatJoinStyles

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add three autoshapes of rectangle type
    shp1 = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 100, 150, 75)
    shp2 = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 100, 150, 75)
    shp3 = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 250, 150, 75)

    # Set the fill color of the rectangle shape
    shp1.fill_format.fill_type = slides.FillType.SOLID
    shp1.fill_format.solid_fill_color.color = drawing.Color.black
    shp2.fill_format.fill_type = slides.FillType.SOLID
    shp2.fill_format.solid_fill_color.color = drawing.Color.black
    shp3.fill_format.fill_type = slides.FillType.SOLID
    shp3.fill_format.solid_fill_color.color = drawing.Color.black

    # Set the line width
    shp1.line_format.width = 15
    shp2.line_format.width = 15
    shp3.line_format.width = 15

    # Set the color of the line of rectangle
    shp1.line_format.fill_format.fill_type = slides.FillType.SOLID
    shp1.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
    shp2.line_format.fill_format.fill_type = slides.FillType.SOLID
    shp2.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
    shp3.line_format.fill_format.fill_type = slides.FillType.SOLID
    shp3.line_format.fill_format.solid_fill_color.color = drawing.Color.blue

    # Set the Join Style
    shp1.line_format.join_style = slides.LineJoinStyle.MITER
    shp2.line_format.join_style = slides.LineJoinStyle.BEVEL
    shp3.line_format.join_style = slides.LineJoinStyle.ROUND

    # Add text to each rectangle
    shp1.text_frame.text = "This is Miter Join Style"
    shp2.text_frame.text = "This is Bevel Join Style"
    shp3.text_frame.text = "This is Round Join Style"

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_line_format_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:FormatJoinStyles