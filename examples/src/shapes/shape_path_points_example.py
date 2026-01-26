import aspose.slides as slides


def shape_path_points_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresetGeometry.pptx") as pres:
        shape = pres.slides[0].shapes[0]
        elements = shape.create_shape_elements()
        for element in elements:
            print("Start element")

            types = element.path_types
            points = element.path_points

            for t, p in zip(types, points):
                if t == 0:
                    print("Start point", p)
                elif t == 1:
                    print("LineTo point", p)
                elif t == 3:
                    print("Bezier spline point", p)
                elif t == 128:
                    print("Close subpath point", p)
                elif t == 129:
                    print("End point", p)
