import aspose.slides as slides
 
def convert_to_tiff_image_pixel_format():
    #ExStart:PresentationToTIFFWithCustomImagePixelFormat
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a Presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        options = slides.export.TiffOptions()
        
        options.pixel_format = slides.export.ImagePixelFormat.FORMAT8BPP_INDEXED
        notesOptions = options.notes_comments_layouting
        notesOptions.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        """
        ImagePixelFormat contains the following values (as could be seen from documentation):
        Format1bppIndexed # 1 bits per pixel, indexed.
        Format4bppIndexed # 4 bits per pixel, indexed.
        Format8bppIndexed # 8 bits per pixel, indexed.
        Format24bppRgb # 24 bits per pixel, RGB.
        Format32bppArgb # 32 bits per pixel, ARGB.
        """

        # Save the presentation to TIFF with specified image size
        presentation.save(outDir + "convert_to_tiff_image_pixel_format_out.tiff", slides.export.SaveFormat.TIFF, options)
    #ExEnd:PresentationToTIFFWithCustomImagePixelFormat

