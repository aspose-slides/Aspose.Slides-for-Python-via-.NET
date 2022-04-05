import aspose.slides as slides

#ExStart:ChangeShapeOrder
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation1:
    slide = presentation1.slides[0]
    shp3 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 365, 400, 150)
    shp3.fill_format.fill_type = slides.FillType.NO_FILL
    shp3.add_text_frame(" ")

    txtFrame = shp3.text_frame
    para = txtFrame.paragraphs[0]
    portion = para.portions[0]
    portion.text="Watermark Text Watermark Text Watermark Text"
    shp3 = slide.shapes.add_auto_shape(slides.ShapeType.TRIANGLE, 200, 365, 400, 150)
    slide.shapes.reorder(2, shp3)

    presentation1.save(outDir + "shapes_reorder_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangeShapeOrder


