import aspose.pydrawing as drawing
import aspose.slides as slides


def create_smart_art_child_note_thumbnail(global_opts):
    # Instantiate Presentation class that represents the PPTX file
    with slides.Presentation() as pres:
        # Add SmartArt
        smart = pres.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_CYCLE)

        # Obtain the reference of a node by using its Index
        node = smart.nodes[1]

        # Get thumbnail
        bmp = node.shapes[0].get_image()

        # Save thumbnail
        bmp.save(global_opts.out_dir + "shapes_create_smartart_thumbnail_out.jpeg", slides.ImageFormat.JPEG)
