import aspose.pydrawing as drawing
import aspose.slides as slides


def fill_format_smart_art_shape_node(global_opts):
    with slides.Presentation() as presentation:
        # Accessing the slide
        slide = presentation.slides[0]

        # Adding SmartArt shape and nodes
        chevron = slide.shapes.add_smart_art(10, 10, 800, 60, slides.smartart.SmartArtLayoutType.CLOSED_CHEVRON_PROCESS)
        node = chevron.all_nodes.add_node()
        node.text_frame.text = "Some text"

        # Setting node fill color
        for item in node.shapes:
            item.fill_format.fill_type = slides.FillType.SOLID
            item.fill_format.solid_fill_color.color = drawing.Color.red

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_shapes_fill_format_out.pptx", slides.export.SaveFormat.PPTX)
