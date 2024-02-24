import aspose.slides as slides


def convert_to_tiff_image_pixel_format(global_opts):
    # Instantiate a Presentation object that represents a Presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        tiff_options = slides.export.TiffOptions()
        tiff_options.pixel_format = slides.export.ImagePixelFormat.FORMAT_8BPP_INDEXED

        notes_comments_layouting_options = tiff_options.notes_comments_layouting
        notes_comments_layouting_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        """
        ImagePixelFormat contains the following values (as could be seen from documentation):
        Format1bppIndexed # 1 bits per pixel, indexed.
        Format4bppIndexed # 4 bits per pixel, indexed.
        Format8bppIndexed # 8 bits per pixel, indexed.
        Format24bppRgb # 24 bits per pixel, RGB.
        Format32bppArgb # 32 bits per pixel, ARGB.
        """

        # Save the presentation to TIFF with specified image size
        presentation.save(global_opts.out_dir + "convert_to_tiff_image_pixel_format_out.tiff",
                          slides.export.SaveFormat.TIFF, tiff_options)
