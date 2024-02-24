import aspose.slides as slides


def export_ink_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "InkOptions.pptx") as pres:
        pdf_options = slides.export.PdfOptions()
        # Hide ink objects
        pdf_options.ink_options.hide_ink = True
        # Save result
        pres.save(global_opts.out_dir + "HideInkDemo.pdf", slides.export.SaveFormat.PDF, pdf_options)

        # Show Ink objects
        pdf_options.ink_options.hide_ink = False
        # Set using ROP operation for rendering brush
        pdf_options.ink_options.interpret_mask_op_as_opacity = False
        # Save result
        pres.save(global_opts.out_dir + "ROPInkDemo.pdf", slides.export.SaveFormat.PDF, pdf_options)
