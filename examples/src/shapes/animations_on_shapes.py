import aspose.slides as slides
import aspose.pydrawing as drawing


def animation_on_shapes(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        slide = pres.slides[0]

        # Now create effect "PATH_FOOTBALL" for existing shape from scratch.
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 150, 250, 25)

        auto_shape.add_text_frame("Animated TextBox")

        # Add PATH_FOOTBALL animation effect
        pres.slides[0].timeline.main_sequence.add_effect(auto_shape, slides.animation.EffectType.PATH_FOOTBALL,
                                                         slides.animation.EffectSubtype.NONE,
                                                         slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        # Create some kind of "button".
        shape_trigger = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.BEVEL, 10, 10, 20, 20)

        # Create sequence of effects for this button.
        seq_inter = pres.slides[0].timeline.interactive_sequences.add(shape_trigger)

        # Create custom user path. Our object will be moved only after "button" click.
        fx_user_path = seq_inter.add_effect(auto_shape, slides.animation.EffectType.PATH_USER,
                                            slides.animation.EffectSubtype.NONE,
                                            slides.animation.EffectTriggerType.ON_CLICK)

        # Created path is empty so we should add commands for moving.
        motion_behavior = fx_user_path.behaviors[0]

        pts = [drawing.PointF(0.076, 0.59)]
        motion_behavior.path.add(slides.animation.MotionCommandPathType.LINE_TO, pts,
                                 slides.animation.MotionPathPointsType.AUTO, True)
        pts = [drawing.PointF(0.076, 0.59)]
        motion_behavior.path.add(slides.animation.MotionCommandPathType.LINE_TO, pts,
                                 slides.animation.MotionPathPointsType.AUTO, False)
        motion_behavior.path.add(slides.animation.MotionCommandPathType.END, None,
                                 slides.animation.MotionPathPointsType.AUTO, False)

        # Write the presentation as PPTX to disk
        pres.save(global_opts.out_dir + "shapes_animations_out.pptx", slides.export.SaveFormat.PPTX)
