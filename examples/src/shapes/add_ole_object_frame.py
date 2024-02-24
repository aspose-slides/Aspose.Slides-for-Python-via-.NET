import aspose.slides as slides


def shapes_add_ole_object_frame(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Access the first slide
        slide = pres.slides[0]

        # Load an excel file to stream
        with open(global_opts.data_dir + "book.xlsx", "rb") as fs:
            bytes_array = fs.read()
        
            # Create a data object for embedding
            data_info = slides.dom.ole.OleEmbeddedDataInfo(bytes_array, "xlsx")

            # Add an Ole Object Frame shape
            ole_object_frame = slide.shapes.add_ole_object_frame(0, 0, pres.slide_size.size.width, pres.slide_size.size.height, data_info)

            # Write the PPTX to disk
            pres.save(global_opts.out_dir + "shapes_add_ole_object_frame_out.pptx", slides.export.SaveFormat.PPTX)
