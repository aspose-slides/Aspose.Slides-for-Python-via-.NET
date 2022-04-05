import aspose.slides as slides
import aspose.pydrawing as drawing

def shapes_add_arrow_shaped_line():
    #ExStart:AddArrowShapedLine
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate PresentationEx class that represents the PPTX file
    with slides.Presentation() as pres:
        # Get the first slide
        sld = pres.slides[0]

        # Add an autoshape of type line
        shp = sld.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

        # Apply some formatting on the line
        shp.line_format.style = slides.LineStyle.THICK_BETWEEN_THIN
        shp.line_format.width = 10

        shp.line_format.dash_style = slides.LineDashStyle.DASH_DOT

        shp.line_format.begin_arrowhead_length = slides.LineArrowheadLength.SHORT
        shp.line_format.begin_arrowhead_style = slides.LineArrowheadStyle.OVAL

        shp.line_format.end_arrowhead_length = slides.LineArrowheadLength.LONG
        shp.line_format.end_arrowhead_style = slides.LineArrowheadStyle.TRIANGLE

        shp.line_format.fill_format.fill_type = slides.FillType.SOLID
        shp.line_format.fill_format.solid_fill_color.color = drawing.Color.maroon

        #Write the PPTX to Disk
        pres.save(outDir + "shapes_add_arrow_shaped_line_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AddArrowShapedLine