import aspose.slides as slides

def charts_bubble_size_representation():
    #ExStart:SupportOfBubbleSizeRepresentation
    # The path to the documents directory.
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 600, 400, True)
        chart.chart_data.series_groups[0].bubble_size_representation = slides.charts.BubbleSizeRepresentationType.WIDTH
        pres.save(outDir + "charts_bubble_size_representation_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:SupportOfBubbleSizeRepresentation
