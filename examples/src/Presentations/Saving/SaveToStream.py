import aspose.slides as slides

def save_to_stream():
    #ExStart:SaveToStream
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as presentation:
        shape = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 200, 200)

        # Add text to shape
        shape.text_frame.text = "This demo shows how to Create PowerPoint file and save it to Stream."

        with open(outDir + "save_to_stream_out.pptx", "xb") as fs:
            presentation.save(fs, slides.export.SaveFormat.PPTX)
    #ExEnd:SaveToStream
