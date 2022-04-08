import aspose.slides as slides

"""
This code example demonstrates how the set_macro_hyperlink_click method is used to set a macro hyperlink click on a shape:
"""


macroName = "TestMacro"
with slides.Presentation() as presentation:
    shape = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.BLANK_BUTTON, 20, 20, 80, 30)
    shape.hyperlink_manager.set_macro_hyperlink_click(macroName)

    print("External URL is {0}".format(shape.hyperlink_click.external_url))
    print("Shape action type is {0}".format(shape.hyperlink_click.action_type))
