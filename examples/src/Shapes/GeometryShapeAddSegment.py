import aspose.slides as slides

"""
This example demonstrates adding new segment to the existing geometry shape.
"""

# Output file name
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create new shape
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)
    # Get geometry path of the shape
    geometryPath = shape.get_geometry_paths()[0]

    # Add two lines to geometry path
    geometryPath.line_to(100, 50, 1)
    geometryPath.line_to(100, 50, 4)

    # Assign edited geometry path to the shape
    shape.set_geometry_path(geometryPath)

    # Save the presentation
    pres.save(outDir + "shapes_add_segment_to_geometry_path_out.pptx", slides.export.SaveFormat.PPTX)
