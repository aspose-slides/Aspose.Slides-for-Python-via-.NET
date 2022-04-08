import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:TableFromScratch
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX# Instantiate Presentation class that represents PPTX
with slides.Presentation(dataDir + "tables_update.pptx") as presentation:
    # Access the first slide
    slide = presentation.slides[0]

    # Initialize None Table
    table = None

    # Iterate through the shapes and set a reference to the table found
    for shape in slide.shapes:
        if type(shape) is slides.Table:
            # Set the text of the first column of second row
            shape.rows[0][1].text_frame.text = "New"

    # Write the PPTX to Disk
    presentation.save(outDir + "tables_update_table_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:TableFromScratch