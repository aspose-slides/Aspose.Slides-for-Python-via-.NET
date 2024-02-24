import aspose.pydrawing as drawing
import aspose.slides as slides


def create_scaling_factor_thumbnail(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as p:
        # Create a full scale image
        with p.slides[0].shapes[0].get_thumbnail(slides.ShapeThumbnailBounds.SHAPE, 2, 2) as bitmap:
            # Save the image to disk in PNG format
            bitmap.save(global_opts.out_dir + "shapes_create_scaling_thumbnail_out.png",
                        drawing.imaging.ImageFormat.png)
