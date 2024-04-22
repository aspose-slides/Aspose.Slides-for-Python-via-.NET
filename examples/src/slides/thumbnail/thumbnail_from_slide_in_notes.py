import aspose.pydrawing as drawing
import aspose.slides as slides


def thumbnail_from_slide_in_notes(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Access the first slide
        slide = pres.slides[0]

        # User defined dimension
        desired_x = 1200
        desired_y = 800

        # Getting scaled value  of X and Y
        scale_x = (1.0 / pres.slide_size.size.width) * desired_x
        scale_y = (1.0 / pres.slide_size.size.height) * desired_y

        # Create a full scale image
        bmp = slide.get_image(scale_x, scale_y)
        # Save the image to disk in JPEG format
        bmp.save(global_opts.out_dir + "thumbnail_get_from_notes_out.jpg", slides.ImageFormat.JPEG)
