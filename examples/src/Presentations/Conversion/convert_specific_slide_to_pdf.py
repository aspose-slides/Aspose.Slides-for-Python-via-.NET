import aspose.slides as slides


def convert_specific_slide_to_pdf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Setting array of slides positions
        indexes = [1, 3]

        # Save the presentation to PDF
        presentation.save(global_opts.out_dir + "convert_specific_slide_to_pdf_out.pdf", indexes,
                          slides.export.SaveFormat.PDF)
