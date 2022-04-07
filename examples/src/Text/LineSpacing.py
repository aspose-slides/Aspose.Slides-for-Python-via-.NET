import aspose.slides as slides

#ExStart:LineSpacing

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "text_fonts.pptx") as presentation:

    # Obtain a slide's reference by its index
    sld = presentation.slides[0]

    # Access the TextFrame
    tf1 = (sld.shapes[0]).text_frame

    # Access the Paragraph
    para1 = tf1.paragraphs[0]

    # Set properties of Paragraph
    para1.paragraph_format.space_within = 80
    para1.paragraph_format.space_before = 40
    para1.paragraph_format.space_after = 40
    # Save Presentation
    presentation.save(outDir + "text_line_spacing_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:LineSpacing