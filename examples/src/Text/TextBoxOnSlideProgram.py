import aspose.slides as slides


#ExStart:TextBoxOnSlideProgram
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation# Instantiate Presentation
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add an AutoShape of Rectangle type
    ashp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 150, 50)

    # Add TextFrame to the Rectangle
    ashp.add_text_frame(" ")

    # Accessing the text frame
    txtFrame = ashp.text_frame

    # Create the Paragraph object for text frame
    para = txtFrame.paragraphs[0]

    # Create Portion object for paragraph
    portion = para.portions[0]

    # Set Text
    portion.text = "Aspose TextBox"

    # Save the presentation to disk
    pres.save(outDir + "text_TextBox_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:TextBoxOnSlideProgram