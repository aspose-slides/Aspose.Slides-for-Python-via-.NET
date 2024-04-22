import aspose.slides as slides


def default_fonts_example(global_opts):
    # Use load options to define the default regular and asian fonts
    load_options = slides.LoadOptions()
    load_options.load_format = slides.LoadFormat.AUTO
    load_options.default_regular_font = "Wingdings"
    load_options.default_asian_font = "Wingdings"

    # Load the presentation
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx", load_options) as pptx:
        # Generate slide thumbnail
        pptx.slides[0].get_image(1, 1).save(global_opts.out_dir + "text_default_fonts_out.png", slides.ImageFormat.PNG)

        # Generate PDF
        pptx.save(global_opts.out_dir + "text_default_fonts_out.pdf", slides.export.SaveFormat.PDF)

        # Generate XPS
        pptx.save(global_opts.out_dir + "text_default_fonts_out.xps", slides.export.SaveFormat.XPS)
