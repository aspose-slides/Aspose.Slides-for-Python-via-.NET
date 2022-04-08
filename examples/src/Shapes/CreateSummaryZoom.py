import aspose.pydrawing as drawing
import aspose.slides as slides

"""
This sample demonstrates how to create a summary zoom using Aspose.Slides for .NET
"""

# Output file name
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    #Adds a new slide to the presentation
    slide = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide.background.fill_format.fill_type = slides.FillType.SOLID
    slide.background.fill_format.solid_fill_color.color = drawing.Color.brown
    slide.background.type = slides.BackgroundType.OWN_BACKGROUND

    # Adds a new section to the presentation
    pres.sections.add_section("Section 1", slide)

    #Adds a new slide to the presentation
    slide = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide.background.fill_format.fill_type = slides.FillType.SOLID
    slide.background.fill_format.solid_fill_color.color = drawing.Color.aqua
    slide.background.type = slides.BackgroundType.OWN_BACKGROUND

    # Adds a new section to the presentation
    pres.sections.add_section("Section 2", slide)

    #Adds a new slide to the presentation
    slide = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide.background.fill_format.fill_type = slides.FillType.SOLID
    slide.background.fill_format.solid_fill_color.color = drawing.Color.chartreuse
    slide.background.type = slides.BackgroundType.OWN_BACKGROUND

    # Adds a new section to the presentation
    pres.sections.add_section("Section 3", slide)

    #Adds a new slide to the presentation
    slide = pres.slides.add_empty_slide(pres.slides[0].layout_slide)
    slide.background.fill_format.fill_type = slides.FillType.SOLID
    slide.background.fill_format.solid_fill_color.color = drawing.Color.dark_green
    slide.background.type = slides.BackgroundType.OWN_BACKGROUND

    # Adds a new section to the presentation
    pres.sections.add_section("Section 4", slide)

    # Adds a SummaryZoomFrame object
    summaryZoomFrame = pres.slides[0].shapes.add_summary_zoom_frame(150, 50, 300, 200)

    # Saves the presentation
    pres.save(outDir + "shapes_create_summary_zoom_out.pptx", slides.export.SaveFormat.PPTX)

