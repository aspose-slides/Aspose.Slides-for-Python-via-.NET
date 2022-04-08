import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:AddImageinsideTableCell
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class object
with slides.Presentation() as presentation:
    # Access first slide
    islide = presentation.slides[0]

    # Define columns with widths and rows with heights
    dblCols = [ 150, 150, 150, 150 ]
    dblRows = [ 100, 100, 100, 100, 90 ]

    # Add table shape to slide
    tbl = islide.shapes.add_table(50, 50, dblCols, dblRows)

    # Creating a Image object to hold the image file
    image = drawing.Bitmap(dataDir + "image1.jpg")

    # Create an object using the bitmap object
    imgx1 = presentation.images.add_image(image)

    # Add image to first table cell
    tbl.rows[0][0].cell_format.fill_format.fill_type = slides.FillType.PICTURE
    tbl.rows[0][0].cell_format.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH
    tbl.rows[0][0].cell_format.fill_format.picture_fill_format.picture.image = imgx1

    # Save PPTX to Disk
    presentation.save(outDir + "tables_add_image_to_cell_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddImageinsideTableCell