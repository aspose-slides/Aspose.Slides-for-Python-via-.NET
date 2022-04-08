import aspose.slides as slides

def save_add_blob_image():
    #ExStart:AddBlobImageToPresentation

    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # create a new presentation which will contain this image
    with slides.Presentation() as pres:
        with open(dataDir + "large_image.jpg", "br") as fileStream:
            # let's add the image to the presentation - we choose KeepLocked behavior, because we not
            # have an intent to access the "large_image.jpg" file.
            img = pres.images.add_image(fileStream, slides.LoadingStreamBehavior.KEEP_LOCKED)
            pres.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 0, 0, 300, 200, img)

            # save the presentation. Despite that the output presentation will be
            # large, the memory consumption will be low the whole lifetime of the pres object
            pres.save(outDir + "save_add_blob_image_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:AddBlobImageToPresentation

