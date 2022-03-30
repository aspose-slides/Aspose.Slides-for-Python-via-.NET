import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_entities_formatting():
    #ExStart:ChartEntities
    # The path to the documents directory.

    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiating presentation# Instantiating presentation
    with slides.Presentation() as pres:

        # Accessing the first slide
        slide = pres.slides[0]

        # Adding the sample chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 50, 50, 500, 400)

        # Setting Chart Titile
        chart.has_title = True
        chart.chart_title.add_text_frame_for_overriding("")
        chartTitle = chart.chart_title.text_frame_for_overriding.paragraphs[0].portions[0]
        chartTitle.text = "Sample Chart"
        chartTitle.portion_format.fill_format.fill_type = slides.FillType.SOLID
        chartTitle.portion_format.fill_format.solid_fill_color.color = drawing.Color.gray
        chartTitle.portion_format.font_height = 20
        chartTitle.portion_format.font_bold = 1
        chartTitle.portion_format.font_italic = 1

        # Setting Major grid lines format for value axis
        chart.axes.vertical_axis.major_grid_lines_format.line.fill_format.fill_type = slides.FillType.SOLID
        chart.axes.vertical_axis.major_grid_lines_format.line.fill_format.solid_fill_color.color = drawing.Color.blue
        chart.axes.vertical_axis.major_grid_lines_format.line.width = 5
        chart.axes.vertical_axis.major_grid_lines_format.line.dash_style = slides.LineDashStyle.DASH_DOT

        # Setting Minor grid lines format for value axis
        chart.axes.vertical_axis.minor_grid_lines_format.line.fill_format.fill_type = slides.FillType.SOLID
        chart.axes.vertical_axis.minor_grid_lines_format.line.fill_format.solid_fill_color.color = drawing.Color.red
        chart.axes.vertical_axis.minor_grid_lines_format.line.width = 3

        # Setting value axis number format
        chart.axes.vertical_axis.is_number_format_linked_to_source = False
        chart.axes.vertical_axis.display_unit = slides.charts.DisplayUnitType.THOUSANDS
        chart.axes.vertical_axis.number_format = "0.0%"

        # Setting chart maximum, minimum values
        chart.axes.vertical_axis.is_automatic_major_unit = False
        chart.axes.vertical_axis.is_automatic_max_value = False
        chart.axes.vertical_axis.is_automatic_minor_unit = False
        chart.axes.vertical_axis.is_automatic_min_value = False

        chart.axes.vertical_axis.max_value = 15
        chart.axes.vertical_axis.min_value = -2
        chart.axes.vertical_axis.minor_unit = 0.5
        chart.axes.vertical_axis.major_unit = 2.0

        # Setting Value Axis Text Properties
        txtVal = chart.axes.vertical_axis.text_format.portion_format
        txtVal.font_bold = 1
        txtVal.font_height = 16
        txtVal.font_italic = 1
        txtVal.fill_format.fill_type = slides.FillType.SOLID 
        txtVal.fill_format.solid_fill_color.color = drawing.Color.dark_green
        txtVal.latin_font = slides.FontData("Times New Roman")

        # Setting value axis title
        chart.axes.vertical_axis.has_title = True
        chart.axes.vertical_axis.title.add_text_frame_for_overriding("")
        valtitle = chart.axes.vertical_axis.title.text_frame_for_overriding.paragraphs[0].portions[0]
        valtitle.text = "Primary Axis"
        valtitle.portion_format.fill_format.fill_type = slides.FillType.SOLID
        valtitle.portion_format.fill_format.solid_fill_color.color = drawing.Color.gray
        valtitle.portion_format.font_height = 20
        valtitle.portion_format.font_bold = 1
        valtitle.portion_format.font_italic = 1

        # Setting Major grid lines format for Category axis
        chart.axes.horizontal_axis.major_grid_lines_format.line.fill_format.fill_type = slides.FillType.SOLID
        chart.axes.horizontal_axis.major_grid_lines_format.line.fill_format.solid_fill_color.color = drawing.Color.green
        chart.axes.horizontal_axis.major_grid_lines_format.line.width = 5

        # Setting Minor grid lines format for Category axis
        chart.axes.horizontal_axis.minor_grid_lines_format.line.fill_format.fill_type = slides.FillType.SOLID
        chart.axes.horizontal_axis.minor_grid_lines_format.line.fill_format.solid_fill_color.color = drawing.Color.yellow
        chart.axes.horizontal_axis.minor_grid_lines_format.line.width = 3

        # Setting Category Axis Text Properties
        txtCat = chart.axes.horizontal_axis.text_format.portion_format
        txtCat.font_bold = 1
        txtCat.font_height = 16
        txtCat.font_italic = 1
        txtCat.fill_format.fill_type = slides.FillType.SOLID 
        txtCat.fill_format.solid_fill_color.color = drawing.Color.blue
        txtCat.latin_font = slides.FontData("Arial")

        # Setting Category Titile
        chart.axes.horizontal_axis.has_title = True
        chart.axes.horizontal_axis.title.add_text_frame_for_overriding("")

        catTitle = chart.axes.horizontal_axis.title.text_frame_for_overriding.paragraphs[0].portions[0]
        catTitle.text = "Sample Category"
        catTitle.portion_format.fill_format.fill_type = slides.FillType.SOLID
        catTitle.portion_format.fill_format.solid_fill_color.color = drawing.Color.gray
        catTitle.portion_format.font_height = 20
        catTitle.portion_format.font_bold = 1
        catTitle.portion_format.font_italic = 1

        # Setting category axis lable position
        chart.axes.horizontal_axis.tick_label_position = slides.charts.TickLabelPositionType.LOW

        # Setting category axis lable rotation angle
        chart.axes.horizontal_axis.tick_label_rotation_angle = 45

        # Setting Legends Text Properties
        txtleg = chart.legend.text_format.portion_format
        txtleg.font_bold = 1
        txtleg.font_height = 16
        txtleg.font_italic = 1
        txtleg.fill_format.fill_type = slides.FillType.SOLID 
        txtleg.fill_format.solid_fill_color.color = drawing.Color.dark_red

        # Set show chart legends without overlapping chart

        chart.legend.overlay = True
        
        # Ploting first series on secondary value axis

        # Setting chart back wall color
        chart.back_wall.thickness = 1
        chart.back_wall.format.fill.fill_type = slides.FillType.SOLID
        chart.back_wall.format.fill.solid_fill_color.color = drawing.Color.orange

        chart.floor.format.fill.fill_type = slides.FillType.SOLID
        chart.floor.format.fill.solid_fill_color.color = drawing.Color.red
        # Setting Plot area color
        chart.plot_area.format.fill.fill_type = slides.FillType.SOLID
        chart.plot_area.format.fill.solid_fill_color.color = drawing.Color.light_cyan

        # Save Presentation
        pres.save(outDir + "charts_entities_formatting_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:ChartEntities