import aspose.slides as slides


#ExStart:AddColumnsinTextFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    shape1 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)
    format = shape1.text_frame.text_frame_format

    format.column_count = 2
    shape1.text_frame.text = "All these columns are limited to be within a single text container -- " + \
                                "you can add or delete text and the new or remaining text automatically adjusts " + \
                                "itself to flow within the container. You cannot have text flow from one container " + \
                                "to other though -- we told you PowerPoint's column options for text are limited!"
    pres.save(outDir + "text_add_columns_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:AddColumnsinTextFrame
