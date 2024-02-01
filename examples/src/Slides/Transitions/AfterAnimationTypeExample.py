import aspose.slides as slides
import aspose.pydrawing as drawing

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def after_animation_type_example():
    # The path to the documents directory.
    out_path = outDir + "AnimationAfterEffect-out.pptx"
    
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(dataDir + "AnimationAfterEffect.pptx") as pres:
        # Add new slide to the presentation
        slide1 = pres.slides.add_clone(pres.slides[0])
        # Get the first effect of the first slide
        seq = slide1.timeline.main_sequence
        # Change the After animation effect to "Hide on Next Mouse Click" 
        for effect in seq:
            effect.after_animation_type = slides.animation.AfterAnimationType.HIDE_ON_NEXT_MOUSE_CLICK
        
        # Add new slide to the presentation
        slide2 = pres.slides.add_clone(pres.slides[0])
        # Get the first effect of the first slide
        seq = slide2.timeline.main_sequence
        # Change the After animation effect type to "Color"
        for effect in seq:
            effect.after_animation_type = slides.animation.AfterAnimationType.COLOR
            effect.after_animation_color.color = drawing.Color.green
        
        # Add new slide to the presentation
        slide3 = pres.slides.add_clone(pres.slides[0])
        # Get the first effect of the first slide
        seq = slide3.timeline.main_sequence
        # Change the After animation effect to "Hide After Animation" 
        for effect in seq:
            effect.after_animation_type = slides.animation.AfterAnimationType.HIDE_AFTER_ANIMATION
        
        pres.save(out_path, slides.export.SaveFormat.PPTX)
