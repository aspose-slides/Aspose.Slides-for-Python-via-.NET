import aspose.slides as slides

#ExStart:EmbeddedVideoFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Embedd vide inside presentation
    with open(dataDir + "video.mp4", "rb") as in_file:
        vid = pres.videos.add_video(in_file)

        # Add Video Frame
        vf = sld.shapes.add_video_frame(50, 150, 300, 350, vid)

        # Set video to Video Frame
        vf.embedded_video = vid

        # Set Play Mode and Volume of the Video
        vf.play_mode = slides.VideoPlayModePreset.AUTO
        vf.volume = slides.AudioVolumeMode.LOUD

    # Write the PPTX file to disk
    pres.save(outDir + "shapes_embed_video_frame_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:EmbeddedVideoFrame