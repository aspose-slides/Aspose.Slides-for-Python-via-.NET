import aspose.slides as slides


def extract_embedded_file_data_from_ole_object(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_ole_objects.pptx") as pres:
        object_num = 0
        for slide in pres.slides:
            for shape in slide.shapes:
                if type(shape) is slides.OleObjectFrame:
                    object_num += 1
                    data = shape.embedded_data.embedded_file_data
                    extension = shape.embedded_data.embedded_file_extension

                    file_name = "shapes_ole_objects{idx}_out{ex}".format(idx=object_num, ex=extension)
                    with open(global_opts.out_dir + file_name, "wb") as fs:
                        fs.write(data)
