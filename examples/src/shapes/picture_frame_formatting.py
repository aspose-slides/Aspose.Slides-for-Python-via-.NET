import aspose.slides as slides
import aspose.pydrawing as drawing


def picture_frame_formatting(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Instantiate the Image class
        img = slides.Images.from_file(global_opts.data_dir + "image1.jpg")
        imgx = pres.images.add_image(img)

        # Add Picture Frame with height and width equivalent of Picture
        pf = slide.shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 150, imgx.width, imgx.height, imgx)

        # Apply some formatting to PictureFrame
        pf.line_format.fill_format.fill_type = slides.FillType.SOLID
        pf.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
        pf.line_format.width = 20
        pf.rotation = 45

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_picture_frame_format_out.pptx", slides.export.SaveFormat.PPTX)
