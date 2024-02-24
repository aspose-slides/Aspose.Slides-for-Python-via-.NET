import aspose.slides as slides


def convert_to_handout(global_opts):
    with slides.Presentation(global_opts.data_dir + "HandoutExample.pptx") as pres:
        # Set conversion options
        pdf_options = slides.export.PdfOptions()
        pdf_options.show_hidden_slides = True
        slides_layout_options = slides.export.HandoutLayoutingOptions()
        slides_layout_options.handout = slides.export.HandoutType.HANDOUTS_4_HORIZONTAL
        pdf_options.slides_layout_options = slides_layout_options
        
        # Save result
        pres.save(global_opts.out_dir + "HandoutExample.pdf", slides.export.SaveFormat.PDF, pdf_options)
