import aspose.slides as slides


def get_placeholder_text_example():
    with slides.Presentation() as pres:
        # Add new slide based on LayoutSlides[0]
        slide = pres.slides.add_empty_slide(pres.layout_slides[0])

        # Search for specified text in a slide, including its layout (layout template text)
        for _ in slides.util.SlideUtil.get_text_boxes_contains_text(slide, "Click", True):
            # Set text for TextFrame
            print("A text block with the specified text was found.")

        # Find all “Text” placeholders on a slide:
        for _ in slides.util.SlideUtil.find_shapes_by_placeholder_type(slide, slides.PlaceholderType.CENTERED_TITLE):
            print("Placeholder of type PlaceholderType.CenteredTitle was found.")
