import aspose.pydrawing as drawing
import aspose.slides as slides


dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create table
    tbl = pres.slides[0].shapes.add_table(50, 50,  [50, 70] , [ 50, 50, 50 ])

    # Create paragraths
    paragraph0 = slides.Paragraph()
    paragraph0.portions.add(slides.Portion("Text "))
    paragraph0.portions.add(slides.Portion("in0"))
    paragraph0.portions.add(slides.Portion(" Cell"))

    paragraph1 = slides.Paragraph()
    paragraph1.text = "On0"

    paragraph2 = slides.Paragraph()
    paragraph2.portions.add(slides.Portion("Hi there "))
    paragraph2.portions.add(slides.Portion("col0"))

    cell = tbl.rows[1][1]

    # Add text into the table cell
    cell.text_frame.paragraphs.clear()
    cell.text_frame.paragraphs.add(paragraph0)
    cell.text_frame.paragraphs.add(paragraph1)
    cell.text_frame.paragraphs.add(paragraph2)

    # Add TextFrame
    autoShape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 400, 100, 60, 120)
    autoShape.text_frame.text = "Text in shape"
    autoShape.text_frame.paragraphs[0].paragraph_format.alignment = slides.TextAlignment.LEFT

    # Getting coordinates of the left top corner of the table cell.
    x = tbl.x + cell.offset_x
    y = tbl.y + cell.offset_y

    # Using IParagrap.get_rect() and IPortion.get_rect() methods in order to add frame to portions and paragraphs.
    for para in cell.text_frame.paragraphs:
        if para.text == "":
            continue

        rect = para.get_rect()
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE,
                rect.x + x, rect.y + y, rect.width, rect.height)

        shape.fill_format.fill_type = slides.FillType.NO_FILL
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.yellow
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID


        for portion in para.portions:
            if "0" in portion.text:
                rect = portion.get_rect()
                shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE,
                        rect.x + x, rect.y + y, rect.width, rect.height)

                shape.fill_format.fill_type = slides.FillType.NO_FILL

    # Add frame to AutoShape paragraphs.
    for para in autoShape.text_frame.paragraphs:
        rect = para.get_rect()
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE,
                rect.x + autoShape.x, rect.y + autoShape.y, rect.width, rect.height)

        shape.fill_format.fill_type = slides.FillType.NO_FILL
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.yellow
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID

    pres.save(outDir + "text_get_rect_out.pptx", slides.export.SaveFormat.PPTX)
