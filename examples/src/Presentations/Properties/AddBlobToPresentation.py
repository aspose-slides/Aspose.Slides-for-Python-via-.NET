import aspose.slides as slides

def props_add_blob_to_presentation():
    #ExStart:AddBlobToPresentation
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # create a new presentation which will contain this video
    with slides.Presentation() as pres:
        with open(dataDir + "video.mp4", "rb") as fileStream:
            # let's add the video to the presentation - we choose KeepLocked behavior, because we not
            # have an intent to access the "veryLargeVideo.avi" file.
            video = pres.videos.add_video(fileStream, slides.LoadingStreamBehavior.KEEP_LOCKED)
            pres.slides[0].shapes.add_video_frame(0, 0, 480, 270, video)

            # save the presentation. Despite that the output presentation will be very large, the memory
            # consumption will be low the whole lifetime of the pres object
            pres.save(outDir + "props_add_blob_to_presentation_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AddBlobToPresentation


