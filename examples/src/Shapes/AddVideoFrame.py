import aspose.slides as slides

#ExStart:AddVideoFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add Video Frame
    vf = sld.shapes.add_video_frame(50, 150, 300, 150, dataDir + "video.mp4")

    # Set Play Mode and Volume of the Video
    vf.play_mode = slides.VideoPlayModePreset.AUTO
    vf.volume = slides.AudioVolumeMode.LOUD

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_add_video_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddVideoFrame