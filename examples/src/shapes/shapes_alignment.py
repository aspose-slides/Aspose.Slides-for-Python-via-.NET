import aspose.slides as slides


def shapes_alignment(global_opts):
    """This example demonstrates of using SlideUtil.align_shapes method."""
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
        group_shape = slide.shapes.add_group_shape()
        # Create some shapes to the group shape
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 350, 50, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 450, 150, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 550, 250, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 650, 350, 50, 50)
        # Aligning all shapes within IGroupShape.
        slides.util.SlideUtil.align_shapes(slides.ShapesAlignmentType.ALIGN_LEFT, False, group_shape)

        slide = pres.slides.add_empty_slide(slide.layout_slide)
        # Add group shape
        group_shape = slide.shapes.add_group_shape()
        # Create some shapes to the group shape
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 350, 50, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 450, 150, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 550, 250, 50, 50)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 650, 350, 50, 50)
        # Aligning shapes with specified indexes within IGroupShape.
        slides.util.SlideUtil.align_shapes(slides.ShapesAlignmentType.ALIGN_LEFT, False, group_shape, [0, 2])

        # Save presentation
        pres.save(global_opts.out_dir + "shapes_align_out.pptx", slides.export.SaveFormat.PPTX)
