import aspose.slides as slides

def convert_to_black_white_tiff():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "SimpleAnimations.pptx") as presentation:
        # Instantiate the TiffOptions class
        options = slides.export.TiffOptions()
        options.compression_type = slides.export.TiffCompressionTypes.CCITT4
        options.bw_conversion_mode = slides.export.BlackWhiteConversionMode.DITHERING

        # Save output file
        presentation.save(outDir + "BlackWhite_out.tiff", [ 2 ], slides.export.SaveFormat.TIFF, options)

