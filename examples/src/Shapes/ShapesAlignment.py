import aspose.slides as slides

"""
This example demonstrates of using SlideUtil.align_shapes method.
"""
#Path for output presentation
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    slide = pres.slides[0]
    # Create some shapes
    slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 100, 100)
    slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 100, 100)
    slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 300, 100, 100)
    # Aligning all shapes within IBaseSlide.
    slides.util.SlideUtil.align_shapes(slides.ShapesAlignmentType.ALIGN_BOTTOM, True, pres.slides[0])

    slide = pres.slides.add_empty_slide(slide.layout_slide)
    # Add group shape
    groupShape = slide.shapes.add_group_shape()
    # Create some shapes to the group shape
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 350, 50, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 450, 150, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 550, 250, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 650, 350, 50, 50)
    # Aligning all shapes within IGroupShape.
    slides.util.SlideUtil.align_shapes(slides.ShapesAlignmentType.ALIGN_LEFT, False, groupShape)

    slide = pres.slides.add_empty_slide(slide.layout_slide)
    # Add group shape
    groupShape = slide.shapes.add_group_shape()
    # Create some shapes to the group shape
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 350, 50, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 450, 150, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 550, 250, 50, 50)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 650, 350, 50, 50)
    # Aligning shapes with specified indexes within IGroupShape.
    slides.util.SlideUtil.align_shapes(slides.ShapesAlignmentType.ALIGN_LEFT, False, groupShape, [ 0, 2 ])

    # Save presentation
    pres.save(outDir + "shapes_align_out.pptx", slides.export.SaveFormat.PPTX)
