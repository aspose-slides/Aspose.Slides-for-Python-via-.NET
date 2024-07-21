import aspose.slides as slides


def get_ole_object_frame_count(slides_collection):
    ole_frames_count, empty_ole_frames_count = 0, 0

    for slide in slides_collection:
        for shape in slide.shapes:
            if type(shape) is slides.OleObjectFrame:
                ole_frames_count += 1
                embedded_data = shape.embedded_data.embedded_file_data
                if embedded_data is None or len(embedded_data) == 0:
                    empty_ole_frames_count += 1

    return ole_frames_count, empty_ole_frames_count


def delete_embedded_binary_objects(global_opts):
    # Create loading options.
    load_options = slides.LoadOptions()
    load_options.delete_embedded_binary_objects = True

    with slides.Presentation(global_opts.data_dir + "OlePptx.pptx", load_options) as pres:
        ole_frames_count, empty_ole_frames_count = get_ole_object_frame_count(pres.slides)
        print("Number of OLE frames in source presentation = {}".format(ole_frames_count))
        print("Number of empty OLE frames in source presentation = {}".format(empty_ole_frames_count))

        pres.save(global_opts.out_dir + "OlePptx-out.pptx", slides.export.SaveFormat.PPTX)

        with slides.Presentation(global_opts.out_dir + "OlePptx-out.pptx") as out_pres:
            (ole_frames_count, empty_ole_frames_count) = get_ole_object_frame_count(out_pres.slides)
            print("Number of OLE frames in resulting presentation = {}".format(ole_frames_count))
            print("Number of empty OLE frames in resulting presentation = {}".format(empty_ole_frames_count))
