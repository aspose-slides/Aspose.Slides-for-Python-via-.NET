import aspose.slides as slides


def highlight_text(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as presentation:
        options = slides.TextSearchOptions()
        options.whole_words_only = True
    
        presentation.slides[0].shapes[0].text_frame.highlight_text("title", slides.Color.light_blue)
        presentation.slides[0].shapes[0].text_frame.highlight_text("to", slides.Color.violet, options, None)

        presentation.save(global_opts.out_dir + "text_highlight_text_out.pptx", slides.export.SaveFormat.PPTX)
