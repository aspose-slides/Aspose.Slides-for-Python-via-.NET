import aspose.slides as slides


def convert_to_password_protected_pdf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Instantiate the PdfOptions class
        pdf_options = slides.export.PdfOptions()

        # Setting PDF password
        pdf_options.password = "password"

        # Save the presentation to password-protected PDF
        presentation.save(global_opts.out_dir + "convert_to_password_protected_pdf_out.pdf", slides.export.SaveFormat.PDF, pdf_options)
