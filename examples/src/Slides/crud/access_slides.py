import aspose.slides as slides


def access_slides(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Accessing a slide using its slide index
        slide = pres.slides[0]
        print("Slide Number: " + str(slide.slide_number))
