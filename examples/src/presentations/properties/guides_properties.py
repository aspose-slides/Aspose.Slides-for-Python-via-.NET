import os
import aspose.pydrawing as drawing
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

        # Getting the collection of the drawing guides for first master slide
        guides = pres.masters[0].drawing_guides
        # Adding the new vertical drawing guide to the right of the slide center
        guides.add(slides.Orientation.VERTICAL, slide_size.width / 2 + 20)
        # Print the drawing guides of the first master slide
        print(os.linesep.join(f"{g.orientation} {g.position} {g.color}" for g in guides))

        # Change the color of the first drawing guide of the master slide
        guides[0].color = drawing.Color.forest_green

        # Print the drawing guides of the first master slide
        print(os.linesep.join(f"{g.orientation} {g.position} {g.color}" for g in guides))

        # Save presentation
        pres.save(global_opts.out_dir + "GuidesProperties-out.pptx", slides.export.SaveFormat.PPTX)
