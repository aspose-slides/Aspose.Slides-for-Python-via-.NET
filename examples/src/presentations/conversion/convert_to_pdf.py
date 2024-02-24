import aspose.slides as slides


def convert_to_pdf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Save the presentation to PDF with default options
        presentation.save(global_opts.out_dir + "convert_to_pdf_out.pdf", slides.export.SaveFormat.PDF)
