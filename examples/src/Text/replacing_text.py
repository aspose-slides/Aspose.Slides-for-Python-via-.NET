import aspose.slides as slides


def replacing_text(global_opts):
    # Instantiate Presentation class that represents PPTX
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as pres:
        # Access first slide
        slide = pres.slides[0]

        # Iterate through shapes to find the placeholder
        for shape in slide.shapes:
            if shape.placeholder is not None:
                # Change the text of each placeholder
                shape.text_frame.text = "This is Placeholder"

        # Save the PPTX to Disk
        pres.save(global_opts.out_dir + "text_replacing_out.pptx", slides.export.SaveFormat.PPTX)
