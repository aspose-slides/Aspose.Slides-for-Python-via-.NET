import aspose.pydrawing as drawing
import aspose.slides as slides


def add_image_inside_table_cell_and_crop(global_opts):
    # Instantiate Presentation class object
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [150, 150, 150, 150]
        dbl_rows = [100, 100, 100, 100, 90]

        # Add table shape to slide
        tbl = slide.shapes.add_table(50, 50, dbl_cols, dbl_rows)

        # Creating a Image object to hold the image file
        image = slides.Images.from_file(global_opts.data_dir + "image1.jpg")

        # Create an object using the bitmap object
        imgx1 = presentation.images.add_image(image)

        # Add image to first table cell
        tbl.rows[0][0].cell_format.fill_format.fill_type = slides.FillType.PICTURE
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.picture.image = imgx1
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.crop_right = 20
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.crop_left = 20
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.crop_top = 20
        tbl.rows[0][0].cell_format.fill_format.picture_fill_format.crop_bottom = 20

        # Save PPTX to Disk
        presentation.save(global_opts.out_dir + "tables_add_crop_image_to_cell_out.pptx", slides.export.SaveFormat.PPTX)
