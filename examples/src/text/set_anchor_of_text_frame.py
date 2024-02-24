import aspose.pydrawing as drawing
import aspose.slides as slides


def set_anchor_of_text_frame(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        # Get the first slide
        slide = presentation.slides[0]

        # Add an AutoShape of Rectangle type
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 350, 350)

        # Add TextFrame to the Rectangle
        auto_shape.add_text_frame(" ")
        auto_shape.fill_format.fill_type = slides.FillType.NO_FILL

        # Accessing the text frame
        text_frame = auto_shape.text_frame
        text_frame.text_frame_format.anchoring_type = slides.TextAnchorType.BOTTOM

        # Create the Paragraph object for text frame
        para = text_frame.paragraphs[0]

        # Create Portion object for paragraph
        portion = para.portions[0]
        portion.text = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog."
        portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
        portion.portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Save Presentation
        presentation.save(global_opts.out_dir + "text_set_anchor_text_out.pptx", slides.export.SaveFormat.PPTX)
