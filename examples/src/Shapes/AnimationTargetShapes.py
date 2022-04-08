import aspose.slides as slides

# Path to source presentation
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "shapes_animation_example.pptx") as pres:
    for slide in pres.slides:
        for effect in slide.timeline.main_sequence:
            print("{0} animation effect is set to shape#{1} on slide#{2}".format( 
                effect.type, effect.target_shape.unique_id, slide.slide_number))