import aspose.slides as slides


def charts_set_legend_custom_options(options):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        # Get reference of the slide
        slide = presentation.slides[0]

        # Add a clustered column chart on the slide
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 500)

        # Set Legend Properties
        chart.legend.x = 50 / chart.width
        chart.legend.y = 50 / chart.height
        chart.legend.width = 100 / chart.width
        chart.legend.height = 100 / chart.height

        # Write presentation to disk
        presentation.save(options.out_dir + "charts_set_legend_custom_options_out.pptx", slides.export.SaveFormat.PPTX)
