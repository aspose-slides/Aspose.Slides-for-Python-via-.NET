import aspose.slides as slides
import aspose.pydrawing as drawing

def rendering_options():
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "rendering_options.pptx") as pres:
        renderingOpts = slides.export.RenderingOptions()
        renderingOpts.notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        pres.slides[0].get_thumbnail(renderingOpts, 4 / 3, 4 / 3).save(outDir + "rendering_options-Original.png", drawing.imaging.ImageFormat.png)

        renderingOpts.notes_comments_layouting.notes_position = slides.export.NotesPositions.NONE
        renderingOpts.default_regular_font = "Arial Black"
        pres.slides[0].get_thumbnail(renderingOpts, 4 / 3, 4 / 3).save(outDir + "rendering_options-ArialBlackDefault.png", drawing.imaging.ImageFormat.png)

        renderingOpts.default_regular_font = "Arial Narrow"
        pres.slides[0].get_thumbnail(renderingOpts, 4 / 3, 4 / 3).save(outDir + "rendering_options-ArialNarrowDefault.png", drawing.imaging.ImageFormat.png)



