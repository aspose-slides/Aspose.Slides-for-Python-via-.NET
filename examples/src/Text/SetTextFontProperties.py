import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:SetTextFontProperties
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation
with slides.Presentation() as presentation:
    # Get first slide
    sld = presentation.slides[0]

    # Add an AutoShape of Rectangle type
    ashp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 50, 200, 50)

    # Remove any fill style associated with the AutoShape
    ashp.fill_format.fill_type = slides.FillType.NO_FILL

    # Access the TextFrame associated with the AutoShape
    tf = ashp.text_frame
    tf.text = "Aspose TextBox"

    # Access the Portion associated with the TextFrame
    port = tf.paragraphs[0].portions[0]

    # Set the Font for the Portion
    port.portion_format.latin_font = slides.FontData("Times New Roman")

    # Set Bold property of the Font
    port.portion_format.font_bold = 1

    # Set Italic property of the Font
    port.portion_format.font_italic = 1

    # Set Underline property of the Font
    port.portion_format.font_underline = slides.TextUnderlineType.SINGLE

    # Set the Height of the Font
    port.portion_format.font_height = 25

    # Set the color of the Font
    port.portion_format.fill_format.fill_type = slides.FillType.SOLID
    port.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue

    # Write the PPTX to disk 
    presentation.save(outDir + "text_SetTextFontProperties_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetTextFontProperties
