import aspose.pydrawing as drawing
import aspose.slides as slides
import math


def create_star_geometry(outer_radius, inner_radius):
    star_path = slides.GeometryPath()
    points = []

    step = 72

    for angle in range(-90, 270, step):
        radians = angle * (math.pi / 180)
        x = outer_radius * math.cos(radians)
        y = outer_radius * math.sin(radians)
        points.append(drawing.PointF(x + outer_radius, y + outer_radius))

        radians = math.pi * (angle + step / 2) / 180.0
        x = inner_radius * math.cos(radians)
        y = inner_radius * math.sin(radians)
        points.append(drawing.PointF(x + outer_radius, y + outer_radius))

    star_path.move_to(points[0])

    for point in points:
        star_path.line_to(point)

    star_path.close_figure()

    return star_path


def geometry_shape_creates_custom_geometry(global_opts):
    """The example demonstrates creation a shape with completely custom geometry."""
    outer_radius = 100
    inner_radius = 50

    # Create star geometry path
    star_path = create_star_geometry(outer_radius, inner_radius)

    with slides.Presentation() as pres:
        # Create new shape
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, outer_radius * 2,
                                                     outer_radius * 2)

        # Set new geometry path to the shape
        shape.set_geometry_path(star_path)

        # Save the presentation
        pres.save(global_opts.out_dir + "shapes_create_custom_geometry_out.pptx", slides.export.SaveFormat.PPTX)
