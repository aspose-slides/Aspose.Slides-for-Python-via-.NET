import aspose.slides as slides


#ExStart:ResizeSlideWithTable
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "tables.pptx") as presentation:

    #Old slide size
    currentHeight = presentation.slide_size.size.height
    currentWidth = presentation.slide_size.size.width

    #Changing slide size
    presentation.slide_size.set_size(slides.SlideSizeType.A4_PAPER, slides.SlideSizeScaleType.DO_NOT_SCALE)
    #presentation.slide_size.Orientation = SlideOrienation.Portrait

    #New slide size
    newHeight = presentation.slide_size.size.height
    newWidth = presentation.slide_size.size.width


    ratioHeight = newHeight / currentHeight
    ratioWidth = newWidth / currentWidth

    for master in presentation.masters:
        for shape in master.shapes:
            #Resize position
            shape.height = shape.height * ratioHeight
            shape.width = shape.width * ratioWidth

            #Resize shape size if required 
            shape.y = shape.y * ratioHeight
            shape.x = shape.x * ratioWidth

        for layoutslide in master.layout_slides:
            for shape in layoutslide.shapes:
                #Resize position
                shape.height = shape.height * ratioHeight
                shape.width = shape.width * ratioWidth

                #Resize shape size if required 
                shape.y = shape.y * ratioHeight
                shape.x = shape.x * ratioWidth

    for slide in presentation.slides:
        for shape in slide.shapes:
            #Resize position
            shape.height = shape.height * ratioHeight
            shape.width = shape.width * ratioWidth

            #Resize shape size if required 
            shape.y = shape.y * ratioHeight
            shape.x = shape.x * ratioWidth
            if type(shape) is slides.Table:
                table = shape
                for row in table.rows:
                    row.minimal_height = row.minimal_height * ratioHeight
                    #   row.height = row.height * ratioHeight
                for col in table.columns:
                    col.width = col.width * ratioWidth

    presentation.save(outDir + "tables_resize_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ResizeSlideWithTable
