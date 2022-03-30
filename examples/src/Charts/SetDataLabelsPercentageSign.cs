import aspose.pydrawing as drawing
using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class SetDataLabelsPercentageSign
    {
        public static void Run()
        {
            #ExStart:SetDataLabelsPercentageSign
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            # Get reference of the slide
            slide = presentation.slides[0]

            # Add PercentsStackedColumn chart on a slide
            chart = slide.shapes.add_chart(slides.charts.ChartType.PercentsStackedColumn, 20, 20, 500, 400)

            # Set NumberFormatLinkedToSource to False
            chart.axes.vertical_axis.is_number_format_linked_to_source = False
            chart.axes.vertical_axis.number_format = "0.00%"

            chart.chart_data.series.clear()
            defaultWorksheetIndex = 0

            # Getting the chart data worksheet
            workbook = chart.chart_data.chart_data_workbook

            # Add new series
            series = chart.chart_data.series.add(workbook.get_cell(defaultWorksheetIndex, 0, 1, "Reds"), chart.type)
            series.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 1, 1, 0.30))
            series.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 2, 1, 0.50))
            series.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 3, 1, 0.80))
            series.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 4, 1, 0.65))

            # Setting the fill color of series
            series.format.fill.fill_type = slides.FillType.SOLID
            series.format.fill.solid_fill_color.color = drawing.Color.red

            # Setting LabelFormat properties
            series.labels.default_data_label_format.show_value = True
            series.labels.default_data_label_format.is_number_format_linked_to_source = False
            series.labels.default_data_label_format.number_format = "0.0%"
            series.labels.default_data_label_format.text_format.portion_format.font_height = 10
            series.labels.default_data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
            series.labels.default_data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = Color.white
            series.labels.default_data_label_format.show_value = True

            # Add new series
            series2 = chart.chart_data.series.add(workbook.get_cell(defaultWorksheetIndex, 0, 2, "Blues"), chart.type)
            series2.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 1, 2, 0.70))
            series2.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 2, 2, 0.50))
            series2.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 3, 2, 0.20))
            series2.data_points.add_data_point_for_bar_series(workbook.get_cell(defaultWorksheetIndex, 4, 2, 0.35))

            # Setting Fill type and color
            series2.format.fill.fill_type = slides.FillType.SOLID
            series2.format.fill.solid_fill_color.color = drawing.Color.blue
            series2.labels.default_data_label_format.show_value = True
            series2.labels.default_data_label_format.is_number_format_linked_to_source = False
            series2.labels.default_data_label_format.number_format = "0.0%"
            series2.labels.default_data_label_format.text_format.portion_format.font_height = 10
            series2.labels.default_data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
            series2.labels.default_data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = Color.white

            # Write presentation to disk
            presentation.save(dataDir + "SetDataLabelsPercentageSign_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetDataLabelsPercentageSign
        }
    }
}