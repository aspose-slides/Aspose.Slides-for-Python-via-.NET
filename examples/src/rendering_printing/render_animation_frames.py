import os
import aspose.slides as slides

FPS = 25


def rendering_animation_frames(global_opts):
    frames_dir = os.path.join(global_opts.out_dir, "animation_frames")
    os.makedirs(frames_dir, exist_ok=True)

    # Render every frame of the slide animations to PNG files
    with slides.Presentation(global_opts.data_dir + "SimpleAnimations.pptx") as presentation:
        with slides.export.PresentationAnimationsGenerator(presentation) as animations_generator:
            with slides.export.PresentationPlayer(animations_generator, FPS) as player:

                def on_frame_tick(sender, args):
                    frame_path = os.path.join(frames_dir, "frame_{0}.png".format(sender.frame_index))
                    args.get_frame().save(frame_path)

                player.frame_tick += on_frame_tick
                animations_generator.run(presentation.slides)
