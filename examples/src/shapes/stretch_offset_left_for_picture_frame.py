import aspose.pydrawing as drawing
import aspose.slides as slides


def stretch_offset_left_for_picture_frame(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Instantiate the Image class
        img = drawing.Bitmap(global_opts.data_dir + "image1.jpg")
        imgx = pres.images.add_image(img)

        # Add an AutoShape of Rectangle type
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)

        # Set shape's fill type
        auto_shape.fill_format.fill_type = slides.FillType.PICTURE

        # Set shape's picture fill mode
        auto_shape.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

        # Set image to fill the shape
        auto_shape.fill_format.picture_fill_format.picture.image = imgx

        # Specify image offsets from the corresponding edge of the shape's bounding box
        auto_shape.fill_format.picture_fill_format.stretch_offset_left = 25
        auto_shape.fill_format.picture_fill_format.stretch_offset_right = 25
        auto_shape.fill_format.picture_fill_format.stretch_offset_top = -20
        auto_shape.fill_format.picture_fill_format.stretch_offset_bottom = -10

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_stretch_offset_out.pptx", slides.export.SaveFormat.PPTX)
