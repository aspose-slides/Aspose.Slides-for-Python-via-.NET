import aspose.slides as slides


def shape_visual_bounds_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "Shapes.pptx") as pres:
        shape = pres.slides[0].shapes[0]
        visual_bounds = shape.get_visual_bounds()
        print(f"Visual bounds: X={visual_bounds.x}, Y={visual_bounds.y}, ", end="")
        print(f"Width={visual_bounds.width}, Height={visual_bounds.height}")
