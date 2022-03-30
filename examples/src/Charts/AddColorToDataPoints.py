import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_add_color_to_data_points():
    #ExStart:AddColorToDataPoints

    with slides.Presentation() as pres:
        # The path to the documents directory.
        outDir = "./examples/out/"


        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.SUNBURST, 100, 100, 450, 400)

        dataPoints = chart.chart_data.series[0].data_points
        dataPoints[3].data_point_levels[0].label.data_label_format.show_value = True


    
        branch1Label = dataPoints[0].data_point_levels[2].label
        branch1Label.data_label_format.show_category_name = False
        branch1Label.data_label_format.show_series_name = True

        branch1Label.data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
        branch1Label.data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = drawing.Color.yellow


        steam4Format = dataPoints[9].format
        steam4Format.fill.fill_type = slides.FillType.SOLID
        
        steam4Format.fill.solid_fill_color.color = drawing.Color.from_argb(0, 176, 240, 255)

        pres.save(outDir + "charts_AddColorToDataPoints.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:AddColorToDataPoints

