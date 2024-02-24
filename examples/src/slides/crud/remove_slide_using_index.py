import aspose.slides as slides


def remove_slide_using_index(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Removing a slide using its slide index
        pres.slides.remove_at(0)

        # Writing the presentation file
        pres.save(global_opts.out_dir + "crud_remove_at_out.pptx", slides.export.SaveFormat.PPTX)
