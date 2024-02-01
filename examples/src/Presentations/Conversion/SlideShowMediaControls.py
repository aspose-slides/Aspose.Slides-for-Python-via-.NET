import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def slide_show_media_controls():
    with slides.Presentation() as pres:
        # Еnable media control display in slideshow mode. 
        pres.slide_show_settings.show_media_controls = True
        
        # Save presentation.
        pres.save(outDir + "SlideShowMediaControl.pptx", slides.export.SaveFormat.PPTX)
