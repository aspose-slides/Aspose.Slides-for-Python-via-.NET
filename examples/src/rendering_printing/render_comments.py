import aspose.slides as slides
import aspose.pydrawing as drawing


def rendering_comments(global_opts):
    with slides.Presentation(global_opts.data_dir + "rendering_comments.pptx") as pres:
        bmp = drawing.Bitmap(740, 960)

        render_options = slides.export.RenderingOptions()
        render_options.notes_comments_layouting.comments_area_color = drawing.Color.red
        render_options.notes_comments_layouting.comments_area_width = 200
        render_options.notes_comments_layouting.comments_position = slides.export.CommentsPositions.RIGHT
        render_options.notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        with drawing.Graphics.from_image(bmp) as graphics:
            pres.slides[0].render_to_graphics(render_options, graphics)

        bmp.save(global_opts.out_dir + "rendering_comments_out.png", drawing.imaging.ImageFormat.png)
