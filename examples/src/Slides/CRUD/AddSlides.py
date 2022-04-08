import aspose.slides as slides


#ExStart:AddSlides
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the presentation file
with slides.Presentation() as pres:
    # Instantiate SlideCollection calss
    for layout in pres.layout_slides:
        pres.slides.add_empty_slide(layout)

    # Save the PPTX file to the Disk
    pres.save(outDir + "crud_add_empty_slide_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddSlides