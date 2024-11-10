import aspose.slides as slides


def guides_properties(global_opts):
    with slides.Presentation() as pres:
        # Getting slide size
        slide_size = pres.slide_size.size

        # Getting the collection of the drawing guides
        guides = pres.view_properties.slide_view_properties.drawing_guides
        # Adding the new vertical drawing guide to the right of the slide center
        guides.add(slides.Orientation.VERTICAL, slide_size.width / 2 + 12.5)
        # Adding the new horizontal drawing guide below the slide center
        guides.add(slides.Orientation.HORIZONTAL, slide_size.height / 2 + 12.5)

        # Save presentation
        pres.save(global_opts.out_dir + "GuidesProperties-out.pptx", slides.export.SaveFormat.PPTX)
