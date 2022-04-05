import aspose.pydrawing as drawing
import aspose.slides as slides

"""
This sample demonstrates how to create a section zoom using Aspose.Slides for .NET
"""

# Output file name
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    #Adds a new slide to the presentation
    slide = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide.background.fill_format.fill_type = slides.FillType.SOLID
    slide.background.fill_format.solid_fill_color.color = drawing.Color.yellow_green
    slide.background.type = slides.BackgroundType.OWN_BACKGROUND

    # Adds a new Section to the presentation
    pres.sections.add_section("Section 1", slide)

    # Adds a SectionZoomFrame object
    sectionZoomFrame = pres.slides[0].shapes.add_section_zoom_frame(20, 20, 300, 200, pres.sections[1])

    # Saves the presentation
    pres.save(outDir + "shapes_section_zoom_out.pptx", slides.export.SaveFormat.PPTX)