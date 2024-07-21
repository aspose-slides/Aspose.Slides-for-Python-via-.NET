import aspose.slides as slides


def export_ole_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresOleExample.pptx") as pres:
        options = slides.export.PdfOptions()
        # Include OLE data into exported PDF.
        options.include_ole_data = True
        # Save result
        pres.save(global_opts.out_dir + "PresOleExample.pdf", slides.export.SaveFormat.PDF, options)
