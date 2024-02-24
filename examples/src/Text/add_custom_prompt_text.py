import aspose.slides as slides


def add_custom_prompt_text(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_add_custom_placeholder_text.pptx") as pres:
        slide = pres.slides[0]
        # iterate through the slide
        for shape in slide.slide.shapes:
            if type(shape) is slides.AutoShape and shape.placeholder is not None:
                text = ""
                # title - the text is empty, PowerPoint displays "Click to add title".
                if shape.placeholder.type == slides.PlaceholderType.CENTERED_TITLE:
                    text = "Click to add custom title"
                # the same for subtitle.
                elif shape.placeholder.type == slides.PlaceholderType.SUBTITLE:
                    text = "Click to add custom subtitle"

                shape.text_frame.text = text

                print("Placeholder with text: {0}".format(text))

        pres.save(global_opts.out_dir + "text_add_custom_placeholder_text_out.pptx", slides.export.SaveFormat.PPTX)
