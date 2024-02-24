import aspose.slides as slides


def get_base_placeholder_example(global_opts):
    presentation_name = global_opts.data_dir + "placeholder.pptx"
    
    with slides.Presentation(presentation_name) as presentation:
        slide = presentation.slides[0]
        shape = slide.shapes[0]
        shape_effects = slide.layout_slide.timeline.main_sequence.get_effects_by_shape(shape)
        print("Shape effects count = {0}".format(len(shape_effects)))
        
        layout_shape = shape.get_base_placeholder()
        layout_shape_effects = slide.layout_slide.timeline.main_sequence.get_effects_by_shape(layout_shape)
        print("Layout shape effects count = {0}".format(len(layout_shape_effects)))
        
        master_shape = layout_shape.get_base_placeholder()
        master_shape_effects = slide.layout_slide.master_slide.timeline.main_sequence.get_effects_by_shape(master_shape)
        print("Master shape effects count = {0}".format(len(master_shape_effects)))
