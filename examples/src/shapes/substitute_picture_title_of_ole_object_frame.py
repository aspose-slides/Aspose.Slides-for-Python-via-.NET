﻿import aspose.slides as slides


def substitute_picture_title_of_ole_object_frame(global_opts):
    with slides.Presentation() as pres:
        slide = pres.slides[0]

        # Add Ole objects
        with open(global_opts.data_dir + "book.xlsx", "rb") as file:
            all_bytes = file.read()

        data_info = slides.dom.ole.OleEmbeddedDataInfo(all_bytes, "xlsx")

        oof = slide.shapes.add_ole_object_frame(20, 20, 50, 50, data_info)
        oof.is_object_icon = True

        # Add image object
        img = slides.Images.from_file(global_opts.data_dir + "image1.jpg")
        imgx = pres.images.add_image(img)
        oof.substitute_picture_format.picture.image = imgx

        # Set caption to OLE icon
        oof.substitute_picture_title = "Caption example"
