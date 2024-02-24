import aspose.pydrawing as drawing
import aspose.slides as slides


def create_bounds_shape_thumbnail(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Create a Appearance bound shape image
        with presentation.slides[0].shapes[0].get_thumbnail(slides.ShapeThumbnailBounds.APPEARANCE, 1, 1) as bitmap:
            # Save the image to disk in PNG format
            bitmap.save(global_opts.out_dir + "shapes_get_thumbnail_bound_shape_out.png", drawing.imaging.ImageFormat.png)
