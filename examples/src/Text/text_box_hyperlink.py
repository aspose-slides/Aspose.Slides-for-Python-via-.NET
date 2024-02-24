import aspose.slides as slides


def text_box_hyperlink(global_opts):
    # Instantiate a Presentation class that represents a PPTX
    with slides.Presentation() as pptx_presentation:
        # Get first slide
        slide = pptx_presentation.slides[0]

        # Add an AutoShape of Rectangle Type
        pptx_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 150, 150, 50)

        # Cast the shape to AutoShape
        pptx_auto_shape = pptx_shape

        # Access text_frame associated with the AutoShape
        pptx_auto_shape.add_text_frame("")

        text_frame = pptx_auto_shape.text_frame

        # Add some text to the frame
        text_frame.paragraphs[0].portions[0].text = "Aspose.Slides"

        # Set Hyperlink for the portion text
        manager = text_frame.paragraphs[0].portions[0].portion_format.hyperlink_manager
        manager.set_external_hyperlink_click("http:#www.aspose.com")

        # Save the PPTX Presentation
        pptx_presentation.save(global_opts.out_dir + "text_set_external_hyperlink_click_out.pptx",
                               slides.export.SaveFormat.PPTX)
