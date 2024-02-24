import aspose.slides as slides


def shapes_accessing_ole_object_frame(global_opts):
    # Load the PPTX to Presentation object
    with slides.Presentation(global_opts.data_dir + "shapes_accessing_ole_object_frame.pptx") as pres:
        # Access the first slide
        slide = pres.slides[0]

        # Cast the shape to OleObjectFrame
        ole_object_frame = slide.shapes[0]

        # Read the OLE Object and write it to disk
        if type(ole_object_frame) is slides.OleObjectFrame:
            # Get embedded file data
            data = ole_object_frame.embedded_data.embedded_file_data

            # Get embedded file extention
            file_extention = ole_object_frame.embedded_data.embedded_file_extension

            # Create a path to save the extracted file
            extracted_path = "excelFromOLE_out" + file_extention

            # Save extracted data
            with open(global_opts.out_dir + "shapes_accessing_ole_object_frame_out.xlsx", "wb") as fs:
                fs.write(data)
