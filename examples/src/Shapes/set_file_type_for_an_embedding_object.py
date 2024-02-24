import aspose.slides as slides


def set_file_type_for_an_embedding_object(global_opts):
    with slides.Presentation() as pres:
        # Add known Ole objects
        with open(global_opts.data_dir + "test.zip", "rb") as file:
            file_bytes = file.read()

            # Create Ole embedded file info
            data_info = slides.dom.ole.OleEmbeddedDataInfo(file_bytes, "zip")

            # Create OLE object
            ole_frame = pres.slides[0].shapes.add_ole_object_frame(150, 20, 50, 50, data_info)
            ole_frame.is_object_icon = True

        pres.save(global_opts.out_dir + "shapes_set_ole_object_out.pptx", slides.export.SaveFormat.PPTX)
