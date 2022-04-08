import aspose.slides as slides

# ExStart:AddColumnInTexBoxes
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Get the first slide of presentation
    slide = presentation.slides[0]

    # Add an AutoShape of Rectangle type
    shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)

    # Add TextFrame to the Rectangle
    shape.add_text_frame("All these columns are limited to be within a single text container -- " +
    "you can add or delete text and the new or remaining text automatically adjusts " +
    "itself to flow within the container. You cannot have text flow from one container " +
    "to other though -- we told you PowerPoint's column options for text are limited!")

    # Get text format of TextFrame
    format = shape.text_frame.text_frame_format

    # Specify number of columns in TextFrame
    format.column_count = 3

    # Specify spacing between columns
    format.column_spacing = 10

    # Save created presentation
    presentation.save(outDir + "text_add_text_frame_out.pptx", slides.export.SaveFormat.PPTX)
# ExEnd:AddColumnInTexBoxes