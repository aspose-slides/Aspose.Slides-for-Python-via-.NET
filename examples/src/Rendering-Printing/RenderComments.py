import aspose.slides as slides
import aspose.pydrawing as drawing

def rendering_comments():
    #ExStart:RenderComments
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "rendering_comments.pptx") as pres:
        bmp = drawing.Bitmap(740, 960)

        renderOptions = slides.export.RenderingOptions()
        renderOptions.notes_comments_layouting.comments_area_color = drawing.Color.red
        renderOptions.notes_comments_layouting.comments_area_width = 200
        renderOptions.notes_comments_layouting.comments_position = slides.export.CommentsPositions.RIGHT
        renderOptions.notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        with drawing.Graphics.from_image(bmp) as graphics:
            pres.slides[0].render_to_graphics(renderOptions, graphics)

        bmp.save(outDir + "rendering_comments_out.png", drawing.imaging.ImageFormat.png)
    #ExEnd:RenderComments
    

