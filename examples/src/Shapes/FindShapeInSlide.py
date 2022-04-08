import aspose.slides as slides


#ExStart:FindShapeInSlide
# Method implementation to find a shape in a slide using its alternative text
def find_shape(slide, alttext):
    # Iterating through all shapes inside the slide
    for shape in slide.shapes:
        # If the alternative text of the slide matches with the required one then
        # Return the shape
        if shape.alternative_text == alttext:
            return shape
    return None


# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "shapes_find_shape.pptx") as p:
    slide = p.slides[0]
    # Alternative text of the shape to be found
    shape = find_shape(slide, "Shape1")
    if shape is not None:
        print("Shape Name: " + shape.name)

#ExEnd:FindShapeInSlide

