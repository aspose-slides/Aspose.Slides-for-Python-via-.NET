import aspose.slides as slides

def shapes_add_audio_frame():
    #ExStart:AddAudioFrame
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with open(dataDir + "audio.wav", "rb") as in_file:

        # Instantiate Prseetation class that represents the PPTX
        with slides.Presentation() as pres:
            # Get the first slide
            sld = pres.slides[0]

            # Add Audio Frame
            audioFrame = sld.shapes.add_audio_frame_embedded(50, 150, 100, 100, in_file)

            # Set Audio to play across the slides
            audioFrame.play_across_slides = True

            # Set Audio to automatically rewind to start after playing
            audioFrame.rewind_audio = True
            
            # Set Play Mode and Volume of the Audio
            audioFrame.play_mode = slides.AudioPlayModePreset.AUTO
            audioFrame.volume = slides.AudioVolumeMode.LOUD

            #Write the PPTX file to disk
            pres.save(outDir + "shapes_add_audio_frame_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AddAudioFrame