import aspose.slides as slides


def compression_level_example(global_opts):
    # The path to output files
    out_file_level1 = global_opts.out_dir + "PresentationCompressionLevel1.pptx"
    out_file_level9 = global_opts.out_dir + "PresentationCompressionLevel9.pptx"

    with slides.Presentation() as pres:
        # Fastest compression with the lowest compression ratio.
        pptx_options = slides.export.PptxOptions()
        pptx_options.compression_level = slides.export.CompressionLevel.LEVEL1
        pres.save(out_file_level1, slides.export.SaveFormat.PPTX, pptx_options)

        # Maximum compression. Produces the smallest file size with the slowest processing speed.
        pptx_options = slides.export.PptxOptions()
        pptx_options.compression_level = slides.export.CompressionLevel.LEVEL9
        pres.save(out_file_level9, slides.export.SaveFormat.PPTX, pptx_options)
