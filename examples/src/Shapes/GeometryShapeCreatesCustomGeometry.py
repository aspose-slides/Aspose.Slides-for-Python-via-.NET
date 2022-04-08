
import aspose.pydrawing as drawing
import aspose.slides as slides
import math

"""
The example demonstrates creation a shape with completely custom geometry.
"""

def create_star_geometry(outerRadius, innerRadiusr):
    starPath = slides.GeometryPath()
    points = []

    step = 72

    for angle in range(-90, 270, step):
        radians = angle * (math.pi / 180)
        x = outerRadius * math.cos(radians)
        y = outerRadius * math.sin(radians)
        points.append(drawing.PointF(x + outerRadius, y + outerRadius))

        radians = math.pi * (angle + step / 2) / 180.0
        x = innerRadiusr * math.cos(radians)
        y = innerRadiusr * math.sin(radians)
        points.append(drawing.PointF(x + outerRadius, y + outerRadius))

    starPath.move_to(points[0])

    for point in points:
        starPath.line_to(point)

    starPath.close_figure()

    return starPath

# Output file name
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Outer and inner star radius
R = 100
r = 50 

# Create star geometry path
starPath = create_star_geometry(R, r)

with slides.Presentation() as pres:
    # Create new shape
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, R * 2, R * 2)

    # Set new geometry path to the shape
    shape.set_geometry_path(starPath)

    # Save the presentation
    pres.save(outDir + "shapes_create_custom_geometry_out.pptx", slides.export.SaveFormat.PPTX)
