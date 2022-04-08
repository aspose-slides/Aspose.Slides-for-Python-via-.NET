import aspose.slides as slides


#ExStart:ExtractAudio

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the presentation file
with slides.Presentation(dataDir + "AudioSlide.ppt") as pres:
    # Access the desired slide
    slide = pres.slides[0]

    # Get the slideshow transition effects for slide
    transition = slide.slide_show_transition

    #Extract sound in byte array
    audio = transition.sound.binary_data

    print("Length: " + str(len(audio)))
#ExEnd:ExtractAudio
