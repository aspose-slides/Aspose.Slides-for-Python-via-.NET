import aspose.slides as slides
import aspose.pydrawing as drawing

#ExStart:AnimationsOnShapes
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    sld = pres.slides[0]

    # Now create effect "PATH_FOOTBALL" for existing shape from scratch.
    ashp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 150, 250, 25)

    ashp.add_text_frame("Animated TextBox")

    # Add PATH_FOOTBALL animation effect
    pres.slides[0].timeline.main_sequence.add_effect(ashp, slides.animation.EffectType.PATH_FOOTBALL,
                            slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

    # Create some kind of "button".
    shapeTrigger = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.BEVEL, 10, 10, 20, 20)

    # Create sequence of effects for this button.
    seqInter = pres.slides[0].timeline.interactive_sequences.add(shapeTrigger)

    # Create custom user path. Our object will be moved only after "button" click.
    fxUserPath = seqInter.add_effect(ashp, slides.animation.EffectType.PATH_USER, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.ON_CLICK)

    # Created path is empty so we should add commands for moving.
    motionBhv = fxUserPath.behaviors[0]

    pts = [ drawing.PointF(0.076, 0.59)]
    motionBhv.path.add(slides.animation.MotionCommandPathType.LINE_TO, pts, slides.animation.MotionPathPointsType.AUTO, True)
    pts = [ drawing.PointF(0.076, 0.59)]
    motionBhv.path.add(slides.animation.MotionCommandPathType.LINE_TO, pts, slides.animation.MotionPathPointsType.AUTO, False)
    motionBhv.path.add(slides.animation.MotionCommandPathType.END, None, slides.animation.MotionPathPointsType.AUTO, False)

    #Write the presentation as PPTX to disk
    pres.save(outDir + "shapes_animations_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AnimationsOnShapes