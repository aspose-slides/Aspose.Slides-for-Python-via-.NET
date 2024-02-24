import aspose.slides as slides
import aspose.pydrawing as drawing


def highlight_text_using_regex(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as presentation:
        options = slides.TextHighlightingOptions()

        # highlighting all words with 10 symbols or longer
        presentation.slides[0].shapes[0].text_frame.highlight_regex(".*", drawing.Color.blue, options)
        presentation.save(global_opts.out_dir + "text_highlight_regex_out.pptx", slides.export.SaveFormat.PPTX)
