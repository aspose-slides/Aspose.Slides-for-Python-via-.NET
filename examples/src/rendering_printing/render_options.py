import aspose.slides as slides


def rendering_options(global_opts):
    with slides.Presentation(global_opts.data_dir + "rendering_options.pptx") as pres:
        rendering_opts = slides.export.RenderingOptions()
        slides_layout_options = slides.export.NotesCommentsLayoutingOptions()
        slides_layout_options.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED
        rendering_opts.slides_layout_options = slides_layout_options

        pres.slides[0].get_image(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-Original.png", slides.ImageFormat.PNG)

        rendering_opts.slides_layout_options.notes_position = slides.export.NotesPositions.NONE
        rendering_opts.default_regular_font = "Arial Black"
        pres.slides[0].get_image(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-ArialBlackDefault.png", slides.ImageFormat.PNG)

        rendering_opts.default_regular_font = "Arial Narrow"
        pres.slides[0].get_image(rendering_opts, 4 / 3, 4 / 3).save(
            global_opts.out_dir + "rendering_options-ArialNarrowDefault.png", slides.ImageFormat.PNG)
