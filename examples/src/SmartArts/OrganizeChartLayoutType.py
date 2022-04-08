import aspose.slides as slides


#ExStart:OrganizeChartLayoutType
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:

    # Add SmartArt BasicProcess 
    smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.ORGANIZATION_CHART)

    # Get or Set the organization chart type 
    smart.nodes[0].organization_chart_layout = slides.smartart.OrganizationChartLayoutType.LEFT_HANGING

    # Saving Presentation
    presentation.save(outDir + "smart_art_organization_chart_layout_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:OrganizeChartLayoutType
