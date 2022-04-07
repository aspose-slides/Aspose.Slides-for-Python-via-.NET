import aspose.slides as slides


#ExStart:TextBoxHyperlink
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents a PPTX
with slides.Presentation() as pptxPresentation:

    # Get first slide
    slide = pptxPresentation.slides[0]

    # Add an AutoShape of Rectangle Type
    pptxShape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 150, 150, 50)

    # Cast the shape to AutoShape
    pptxAutoShape = pptxShape

    # Access text_frame associated with the AutoShape
    pptxAutoShape.add_text_frame("")

    text_frame = pptxAutoShape.text_frame

    # Add some text to the frame
    text_frame.paragraphs[0].portions[0].text = "Aspose.Slides"

    # Set Hyperlink for the portion text
    manager = text_frame.paragraphs[0].portions[0].portion_format.hyperlink_manager
    manager.set_external_hyperlink_click("http:#www.aspose.com")
    # Save the PPTX Presentation
    pptxPresentation.save(outDir + "text_set_external_hyperlink_click_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:TextBoxHyperlink