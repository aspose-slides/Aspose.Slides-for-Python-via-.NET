import aspose.slides as slides


def convert_to_pdf_hidden_slides(global_opts):
    with slides.Presentation(global_opts.data_dir + "presentation_with_hidden_slides.pptx") as presentation:
        # Instantiate the PdfOptions class
        pdf_options = slides.export.PdfOptions()

        # Specify that the generated document should include hidden slides
        pdf_options.show_hidden_slides = True

        # Save the presentation to PDF with specified options
        presentation.save(global_opts.out_dir + "convert_to_pdf_hidden_slides_out.pdf", slides.export.SaveFormat.PDF,
                          pdf_options)
