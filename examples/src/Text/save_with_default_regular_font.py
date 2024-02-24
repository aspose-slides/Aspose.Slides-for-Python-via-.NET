import aspose.slides as slides


def save_with_default_regular_font(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as pres:
        html_options = slides.export.HtmlOptions()
        html_options.default_regular_font = "Arial Black"
        pres.save(global_opts.out_dir + "text_Presentation-out-ArialBlack.html", slides.export.SaveFormat.HTML,
                  html_options)

        html_options.default_regular_font = "Lucida Console"
        pres.save(global_opts.out_dir + "text_Presentation-out-LucidaConsole.html", slides.export.SaveFormat.HTML,
                  html_options)

        pdf_options = slides.export.PdfOptions()
        pdf_options.default_regular_font = "Arial Black"
        pres.save(global_opts.out_dir + "text_Presentation-out-ArialBlack.pdf", slides.export.SaveFormat.PDF,
                  pdf_options)
