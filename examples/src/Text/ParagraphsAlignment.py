import aspose.slides as slides


#ExStart:ParagraphsAlignment
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a PPTX file

with slides.Presentation(dataDir + "text_paragraphs_alignment.pptx") as pres:
    # Accessing first slide
    slide = pres.slides[0]

    # Accessing the first and second placeholder in the slide and typecasting it
    tf1 = slide.shapes[0].text_frame
    tf2 = slide.shapes[1].text_frame

    # Change the text in both placeholders
    tf1.text = "Center Align by Aspose"
    tf2.text = "Center Align by Aspose"

    # Getting the first paragraph of the placeholders
    para1 = tf1.paragraphs[0]
    para2 = tf2.paragraphs[0]

    # Aligning the text paragraph to center
    para1.paragraph_format.alignment = slides.TextAlignment.CENTER
    para2.paragraph_format.alignment = slides.TextAlignment.CENTER

    #Writing the presentation as a PPTX file
    pres.save(outDir + "text_paragraphs_alignment_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ParagraphsAlignment