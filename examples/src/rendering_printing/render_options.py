import aspose.slides as slides
import aspose.pydrawing as drawing


def rendering_options(global_opts):
    with slides.Presentation(global_opts.data_dir + "rendering_options.pptx") as pres:
        rendering_opts = slides.export.RenderingOptions()
        rendering_opts.notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        pres.slides[0].get_thumbnail(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-Original.png", drawing.imaging.ImageFormat.png)

        rendering_opts.notes_comments_layouting.notes_position = slides.export.NotesPositions.NONE
        rendering_opts.default_regular_font = "Arial Black"
        pres.slides[0].get_thumbnail(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-ArialBlackDefault.png", drawing.imaging.ImageFormat.png)

        rendering_opts.default_regular_font = "Arial Narrow"
        pres.slides[0].get_thumbnail(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-ArialNarrowDefault.png", drawing.imaging.ImageFormat.png)
