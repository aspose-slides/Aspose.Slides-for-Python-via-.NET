import aspose.slides as slides
import aspose.pydrawing as drawing


def bullet_fill_format_example(global_opts):
    with slides.Presentation() as presentation:
        smart = presentation.slides[0].shapes.add_smart_art(10, 10, 500, 400, slides.smartart.SmartArtLayoutType.VERTICAL_PICTURE_LIST)
        node = smart.all_nodes[0]

        if node.bullet_fill_format is not None:
            img = drawing.Bitmap(global_opts.data_dir + "image1.jpg")
            image = presentation.images.add_image(img)
            node.bullet_fill_format.fill_type = slides.FillType.PICTURE
            node.bullet_fill_format.picture_fill_format.picture.image = image
            node.bullet_fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

        presentation.save(global_opts.out_dir +"smart_art_bullet_fill_format_out.pptx", slides.export.SaveFormat.PPTX)
