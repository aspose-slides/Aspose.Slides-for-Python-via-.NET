import aspose.slides as slides

def charts_set_layout_mode():
    #ExStart:SetLayoutMode
    outDir = "./examples/out/"

    with slides.Presentation() as presentation:
        slide = presentation.slides[0]
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 100, 600, 400)
        chart.plot_area.as_ilayoutable.x = 0.2
        chart.plot_area.as_ilayoutable.y = 0.2
        chart.plot_area.as_ilayoutable.width = 0.7
        chart.plot_area.as_ilayoutable.height = 0.7
        chart.plot_area.layout_target_type = slides.charts.LayoutTargetType.INNER

        presentation.save(outDir + "charts_set_layout_mode_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SetLayoutMode
