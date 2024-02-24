import aspose.pydrawing as drawing
import aspose.slides as slides


def convert_to_tiff_custom_size(global_opts):
    # Instantiate a Presentation object that represents a Presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the TiffOptions class
        tiff_options = slides.export.TiffOptions()

        # Setting compression type
        tiff_options.compression_type = slides.export.TiffCompressionTypes.DEFAULT

        notes_options = tiff_options.notes_comments_layouting
        notes_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL
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
        tiff_options.dpi_x = 200
        tiff_options.dpi_y = 100

        # Set Image Size
        tiff_options.image_size = drawing.Size(1728, 1078)

        # Save the presentation to TIFF with specified image size
        pres.save(global_opts.out_dir + "convert_to_tiff_custom_size_out.tiff", slides.export.SaveFormat.TIFF,
                  tiff_options)
