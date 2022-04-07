import aspose.pydrawing as drawing
import aspose.slides as slides

# This example demonstrates setting keep text out of 3D scene.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_keep_text_flat.pptx") as pres:
    shape1 = pres.slides[0].shapes[0]
    shape2 = pres.slides[0].shapes[1]

    shape1.text_frame.text_frame_format.keep_text_flat = False
    shape2.text_frame.text_frame_format.keep_text_flat = True

    pres.slides[0].get_thumbnail(4 / 3, 4 / 3).save(outDir + "text_keep_text_flat_out.png", drawing.imaging.ImageFormat.png)
