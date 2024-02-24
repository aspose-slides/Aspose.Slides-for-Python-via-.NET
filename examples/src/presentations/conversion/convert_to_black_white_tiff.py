import aspose.slides as slides


def convert_to_black_white_tiff(global_opts):
    with slides.Presentation(global_opts.data_dir + "SimpleAnimations.pptx") as presentation:
        # Instantiate the TiffOptions class
        tiff_options = slides.export.TiffOptions()
        tiff_options.compression_type = slides.export.TiffCompressionTypes.CCITT4
        tiff_options.bw_conversion_mode = slides.export.BlackWhiteConversionMode.DITHERING

        # Save output file
        presentation.save(global_opts.out_dir + "BlackWhite_out.tiff", [2], slides.export.SaveFormat.TIFF, tiff_options)
