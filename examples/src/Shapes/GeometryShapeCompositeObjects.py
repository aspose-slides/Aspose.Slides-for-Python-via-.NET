import aspose.slides as slides

"""
The example demonstrates creation a composite custom shape from two GeometryPath objects.
"""

# Output file name
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create new shape
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)

    # Create first geometry path
    geometryPath0 = slides.GeometryPath()
    geometryPath0.move_to(0, 0)
    geometryPath0.line_to(shape.width, 0)
    geometryPath0.line_to(shape.width, shape.height / 3)
    geometryPath0.line_to(0, shape.height / 3)
    geometryPath0.close_figure()

    # Create second geometry path
    geometryPath1 = slides.GeometryPath()
    geometryPath1.move_to(0, shape.height / 3 * 2)
    geometryPath1.line_to(shape.width, shape.height / 3 * 2)
    geometryPath1.line_to(shape.width, shape.height)
    geometryPath1.line_to(0, shape.height)
    geometryPath1.close_figure()

    # Set shape geometry as composition of two geometry path
    shape.set_geometry_paths( [geometryPath0, geometryPath1] )

    # Save the presentation
    pres.save(outDir + "shapes_create_geometry_path_out.pptx", slides.export.SaveFormat.PPTX)
