import aspose.slides as slides


#ExStart:AddLayoutSlides
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    # Try to search by layout slide type
    layoutSlides = presentation.masters[0].layout_slides
    layoutSlide = layoutSlides.get_by_type(slides.SlideLayoutType.TITLE_AND_OBJECT) and layoutSlides.get_by_type(slides.SlideLayoutType.TITLE)

    if layoutSlide is None:
        # The situation when a presentation doesn't contain some type of layouts.
        # presentation File only contains Blank and Custom layout types.
        # But layout slides with Custom types has different slide names,
        # like "Title", "Title and Content", etc. And it is possible to use these
        # names for layout slide selection.
        # Also it is possible to use the set of placeholder shape types. For example,
        # Title slide should have only Title pleceholder type, etc.
        for titleAndObjectLayoutSlide in layoutSlides:
            if titleAndObjectLayoutSlide.name == "Title and Object":
                layoutSlide = titleAndObjectLayoutSlide
                break
        if layoutSlide is None:
            for titleLayoutSlide in layoutSlides:
                if titleLayoutSlide.name == "Title":
                    layoutSlide = titleLayoutSlide
                    break

            if layoutSlide is None:
                layoutSlide = layoutSlides.get_by_type(slides.SlideLayoutType.BLANK)
                if layoutSlide is None:
                    layoutSlide = layoutSlides.add(slides.SlideLayoutType.TITLE_AND_OBJECT, "Title and Object")

    # Adding empty slide with added layout slide 
    presentation.slides.insert_empty_slide(0, layoutSlide)

    # Save presentation    
    presentation.save(outDir + "layout_add_layout_slides_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddLayoutSlides