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
    public class SetInvertFillColorChart
    {
        public static void Run()
        {
            #ExStart:SetInvertFillColorChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            Color inverColor = drawing.Color.red
            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)
                workBook = chart.chart_data.chart_data_workbook

                chart.chart_data.series.clear()
                chart.chart_data.categories.clear()

                # Adding new series and categories
                chart.chart_data.series.add(workBook.get_cell(0, 0, 1, "Series 1"), chart.type)
                chart.chart_data.categories.add(workBook.get_cell(0, 1, 0, "Category 1"))
                chart.chart_data.categories.add(workBook.get_cell(0, 2, 0, "Category 2"))
                chart.chart_data.categories.add(workBook.get_cell(0, 3, 0, "Category 3"))

                # Take first chart series and populating series data.
                series = chart.chart_data.series[0]
                series.data_points.add_data_point_for_bar_series(workBook.get_cell(0, 1, 1, -20))
                series.data_points.add_data_point_for_bar_series(workBook.get_cell(0, 2, 1, 50))
                series.data_points.add_data_point_for_bar_series(workBook.get_cell(0, 3, 1, -30))
                seriesColor = series.GetAutomaticSeriesColor()
                series.InvertIfNegative = True
                series.format.fill.fill_type = slides.FillType.SOLID
                series.format.fill.solid_fill_color.color = seriesColor
                series.InvertedSolidFillColor.color = inverColor
                pres.save(dataDir + "SetInvertFillColorChart_out.pptx", slides.export.SaveFormat.PPTX)               
            }
            #ExEnd:SetInvertFillColorChart
        }
    }
}