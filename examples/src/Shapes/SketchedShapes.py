import aspose.slides as slides
import aspose.pydrawing as drawing

"""
The example below demonstrates how to set sketchy type for a shape.
Please pay attention that not all versions of PowerPoint can display sketched shapes.
"""
#Path for output presentation
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 20, 20, 300, 150)
    shape.fill_format.fill_type = slides.FillType.NO_FILL

    # Transform shape to sketch of a freehand style
    shape.line_format.sketch_format.sketch_type = slides.LineSketchType.SCRIBBLE

    pres.slides[0].get_thumbnail(4/3, 4/3).save(outDir + "shapes_sketch_format_out.png", drawing.imaging.ImageFormat.png)
    pres.save(outDir + "shapes_sketch_format_out.pptx", slides.export.SaveFormat.PPTX)
