import aspose.slides as slides


def adjust_value_type_example(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation(global_opts.data_dir + "PresetGeometry.pptx") as pres:
        shape = pres.slides[0].shapes[0]

        # Show all adjustment point and its types for a RoundRectangle
        print("Adjustment types for a Rectangle:")
        for i in range(len(shape.adjustments)):
            print("\tType for point", i, "is", shape.adjustments[i].type.name)

        # Change value of an adjustment point
        if shape.adjustments[0].type == slides.ShapeAdjustmentType.CORNER_SIZE:
            shape.adjustments[0].angle_value *= 2

        # Show all adjustment point and its types for an RightArrow
        shape1 = pres.slides[0].shapes[1]
        print("Adjustment types for an Arrow:")
        for i in range(len(shape1.adjustments)):
            print("\tType for point", i, "is", shape1.adjustments[i].type.name)

        # Change value of adjustment points
        if shape1.adjustments[0].type == slides.ShapeAdjustmentType.ARROW_TAIL_THICKNESS:
            shape1.adjustments[0].angle_value /= 3

        if shape1.adjustments[1].type == slides.ShapeAdjustmentType.ARROWHEAD_LENGTH:
            shape1.adjustments[1].angle_value /= 2

        # Save the presentation
        pres.save(global_opts.out_dir + "PresetGeometry_out.pptx", slides.export.SaveFormat.PPTX)
