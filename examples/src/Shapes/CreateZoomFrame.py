import aspose.pydrawing as drawing
import aspose.slides as slides


dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    #Add new slides to the presentation
    slide2 = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide3 = pres.slides.add_empty_slide(pres.slides[0].layout_slide)

    # Create a background for the second slide
    slide2.background.type = slides.BackgroundType.OWN_BACKGROUND
    slide2.background.fill_format.fill_type = slides.FillType.SOLID
    slide2.background.fill_format.solid_fill_color.color = drawing.Color.cyan

    # Create a text box for the second slide
    autoshape = slide2.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 200, 500, 200)
    autoshape.text_frame.text = "Second Slide"

    # Create a background for the third slide
    slide3.background.type = slides.BackgroundType.OWN_BACKGROUND
    slide3.background.fill_format.fill_type = slides.FillType.SOLID
    slide3.background.fill_format.solid_fill_color.color = drawing.Color.dark_khaki

    # Create a text box for the third slide
    autoshape = slide3.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 200, 500, 200)
    autoshape.text_frame.text = "Trird Slide"

    # Add ZoomFrame objects with slide preview
    zoomFrame1 = pres.slides[0].shapes.add_zoom_frame(20, 20, 250, 200, slide2)

    # Add ZoomFrame objects with custom image
    # Create a new image for the zoom object
    image = pres.images.add_image(drawing.Image.from_file(dataDir + "image1.jpg"))
    zoomFrame2 = pres.slides[0].shapes.add_zoom_frame(200, 250, 250, 100, slide3, image)

    # Set a zoom frame format for the zoomFrame2 object
    zoomFrame2.line_format.width = 5
    zoomFrame2.line_format.fill_format.fill_type = slides.FillType.SOLID
    zoomFrame2.line_format.fill_format.solid_fill_color.color = drawing.Color.hot_pink
    zoomFrame2.line_format.dash_style = slides.LineDashStyle.DASH_DOT

    # Do not show background for zoomFrame1 object
    zoomFrame1.show_background = False


    # Save the presentation
    pres.save(outDir + "shapes_create_zoom_frame_out.pptx", slides.export.SaveFormat.PPTX)
