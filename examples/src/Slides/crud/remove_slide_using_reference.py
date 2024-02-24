import aspose.slides as slides


def remove_slides_using_reference(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Accessing a slide using its index in the slides collection
        slide = pres.slides[0]

        # Removing a slide using its reference
        pres.slides.remove(slide)

        # Writing the presentation file
        pres.save(global_opts.out_dir + "crud_remove_slide_out.pptx", slides.export.SaveFormat.PPTX)
