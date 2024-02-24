import aspose.pydrawing as drawing
import aspose.slides as slides


def font_family_example(global_opts):
    # Instantiate Presentation Class
    with slides.Presentation() as pres:
        # Get first slide
        slide = pres.slides[0]

        # Add an AutoShape of Rectangle type
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 50, 200, 50)

        # Remove any fill style associated with the AutoShape
        auto_shape.fill_format.fill_type = slides.FillType.NO_FILL

        # Access the TextFrame associated with the AutoShape
        tf = auto_shape.text_frame
        tf.text = "Aspose TextBox"

        # Access the Portion associated with the TextFrame
        port = tf.paragraphs[0].portions[0]

        # Set the Font for the Portion
        port.portion_format.latin_font = slides.FontData("Times New Roman")

        # Set Bold property of the Font
        port.portion_format.font_bold = slides.NullableBool.TRUE

        # Set Italic property of the Font
        port.portion_format.font_italic = slides.NullableBool.TRUE

        # Set Underline property of the Font
        port.portion_format.font_underline = slides.TextUnderlineType.SINGLE

        # Set the Height of the Font
        port.portion_format.font_height = 25

        # Set the color of the Font
        port.portion_format.fill_format.fill_type = slides.FillType.SOLID
        port.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "text_font_family_out.pptx", slides.export.SaveFormat.PPTX)
