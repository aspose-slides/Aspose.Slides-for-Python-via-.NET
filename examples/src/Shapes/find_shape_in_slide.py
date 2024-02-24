import aspose.slides as slides


def find_shape(slide, alt_text):
    # Iterating through all shapes inside the slide
    for shape in slide.shapes:
        # If the alternative text of the slide matches with the required one then
        # Return the shape
        if shape.alternative_text == alt_text:
            return shape
    return None


def find_shape_in_slide(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "shapes_find_shape.pptx") as p:
        slide = p.slides[0]
        # Alternative text of the shape to be found
        shape = find_shape(slide, "Shape1")
        if shape is not None:
            print("Shape Name: " + shape.name)
