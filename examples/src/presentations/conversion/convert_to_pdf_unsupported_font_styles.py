import aspose.slides as slides


def convert_to_pdf_unsupported_font_styles(global_opts):
    with slides.Presentation() as presentation:
        pdf_options = slides.export.PdfOptions()
        pdf_options.rasterize_unsupported_font_styles = True
        presentation.save(global_opts.out_dir + "UnsupportedFontStyles.pdf", slides.export.SaveFormat.PDF, pdf_options)
