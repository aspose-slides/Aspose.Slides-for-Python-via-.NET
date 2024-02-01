import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def get_base_placehorder_example():
    presentation_name = dataDir + "placeholder.pptx"
    
    with slides.Presentation(presentation_name) as presentation:
        slide = presentation.slides[0]
        shape = slide.shapes[0]
        shape_effects = slide.layout_slide.timeline.main_sequence.get_effects_by_shape(shape)
        print("Shape effects count = {0}", len(shape_effects))
        
        layout_shape = shape.get_base_placeholder()
        layout_shape_effects = slide.layout_slide.timeline.main_sequence.get_effects_by_shape(layout_shape)
        print("Layout shape effects count = {0}", len(layout_shape_effects))
        
        master_shape = layout_shape.get_base_placeholder()
        master_shape_effects = slide.layout_slide.master_slide.timeline.main_sequence.get_effects_by_shape(master_shape)
        print("Master shape effects count = {0}", len(master_shape_effects))
