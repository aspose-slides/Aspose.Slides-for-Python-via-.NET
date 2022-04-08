import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:FontProperties
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a PPTX file# Instantiate a Presentation object that represents a PPTX file
with slides.Presentation(dataDir + "text_default_fonts.pptx") as pres:
    # Accessing a slide using its slide position
    slide = pres.slides[0]

    # Accessing the first and second placeholder in the slide and typecasting it
    tf1 = slide.shapes[0].text_frame
    tf2 = slide.shapes[1].text_frame

    # Accessing the first Paragraph
    para1 = tf1.paragraphs[0]
    para2 = tf2.paragraphs[0]

    # Accessing the first portion
    port1 = para1.portions[0]
    port2 = para2.portions[0]

    # Define new fonts
    fd1 = slides.FontData("Elephant")
    fd2 = slides.FontData("Castellar")

    # Assign new fonts to portion
    port1.portion_format.latin_font = fd1
    port2.portion_format.latin_font = fd2

    # Set font to Bold
    port1.portion_format.font_bold = 1
    port2.portion_format.font_bold = 1

    # Set font to Italic
    port1.portion_format.font_italic = 1
    port2.portion_format.font_italic = 1

    # Set font color
    port1.portion_format.fill_format.fill_type = slides.FillType.SOLID
    port1.portion_format.fill_format.solid_fill_color.color = drawing.Color.purple
    port2.portion_format.fill_format.fill_type = slides.FillType.SOLID
    port2.portion_format.fill_format.solid_fill_color.color = drawing.Color.peru

    #Write the PPTX to disk
    pres.save(outDir + "text_font_properties_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:FontProperties