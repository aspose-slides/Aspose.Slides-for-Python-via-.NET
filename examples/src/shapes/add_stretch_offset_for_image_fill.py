import aspose.pydrawing as drawing
import aspose.slides as slides


def add_stretch_offset_for_image_fill(global_opts):
    # Instantiate Prseetation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Instantiate the Image class
        img = drawing.Bitmap(global_opts.data_dir + "image1.jpg")
        imgx = pres.images.add_image(img)

        # Add Picture Frame with height and width equivalent of Picture
        slide.shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 150, imgx.width, imgx.height, imgx)

        # Write the PPTX file to disk
        pres.save(global_opts.data_dir + "shapes_add_stretch_offset_out.pptx", slides.export.SaveFormat.PPTX)
