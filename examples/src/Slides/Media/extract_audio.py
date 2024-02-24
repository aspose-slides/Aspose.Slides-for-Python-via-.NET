import aspose.slides as slides


def extract_audio(global_opts):
    # Instantiate Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "AudioSlide.ppt") as pres:
        # Access the desired slide
        slide = pres.slides[0]

        # Get the slideshow transition effects for slide
        transition = slide.slide_show_transition

        # Extract sound in byte array
        audio = transition.sound.binary_data

        print("Length: " + str(len(audio)))
