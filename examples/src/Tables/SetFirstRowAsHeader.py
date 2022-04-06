import aspose.slides as slides

#ExStart:SetFirstRowAsHeader

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX
with slides.Presentation(dataDir + "tables.pptx") as pres:

    # Access the first slide
    slide = pres.slides[0]

    # Iterate through the shapes and set a reference to the table found
    for shape in slide.shapes:
        if type(shape) is slides.Table:
            #Set the first row of a table as header with a special formatting.
            shape.first_row = True

#ExEnd:SetFirstRowAsHeader
