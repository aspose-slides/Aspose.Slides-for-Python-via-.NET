import aspose.slides as slides

def activex_linking_video_activex_control():
    #ExStart:LinkingVideoActiveXControl
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(dataDir + "activex_template.pptx") as presentation:

        # Create empty presentation instance
        with slides.Presentation() as newPresentation:
            # Remove default slide
            newPresentation.slides.remove_at(0)

            # Clone slide with Media Player ActiveX Control
            newPresentation.slides.insert_clone(0, presentation.slides[0])

            # Access the Media Player ActiveX control and set the video path
            

            control = newPresentation.slides[0].controls[0]

            control.properties.remove("URL")
            control.properties.add("URL", dataDir + "video.mp4")

            # Save the Presentation
            newPresentation.save(outDir + "activex_linking_video_activex_control_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:LinkingVideoActiveXControl