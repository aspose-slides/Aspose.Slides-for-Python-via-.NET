import aspose.pydrawing as drawing
import aspose.slides as slides

def convert_to_tiff_custom_size():
    #ExStart:ConvertWithCustomSize
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a Presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the TiffOptions class
        opts = slides.export.TiffOptions()

        # Setting compression type
        opts.compression_type = slides.export.TiffCompressionTypes.DEFAULT

        notesOptions = opts.notes_comments_layouting
        notesOptions.notes_position = slides.export.NotesPositions.BOTTOM_FULL
        # Compression Types

        # Default - Specifies the default compression scheme (LZW).
        # None - Specifies no compression.
        # CCITT3
        # CCITT4
        # LZW
        # RLE

        # Depth depends on the compression type and cannot be set manually.
        # Resolution unit  is always equal to “2” (dots per inch)

        # Setting image DPI
        opts.dpi_x = 200
        opts.dpi_y = 100

        # Set Image Size
        opts.image_size = drawing.Size(1728, 1078)

        # Save the presentation to TIFF with specified image size
        pres.save(outDir + "convert_to_tiff_custom_size_out.tiff", slides.export.SaveFormat.TIFF, opts)
    #ExEnd:ConvertWithCustomSize