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
    public class MultiCategoryChart
    {
        public static void Run()
        {
            #ExStart:MultiCategoryChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            slide = pres.slides[0]

            ch = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 600, 450)
            ch.chart_data.series.clear()
            ch.chart_data.categories.clear()


            fact = ch.chart_data.chart_data_workbook
            fact.clear(0)
            defaultWorksheetIndex = 0

            IChartCategory category = ch.chart_data.categories.add(fact.get_cell(0, "c2", "A"))
            category.GroupingLevels.SetGroupingItem(1, "Group1")
            category = ch.chart_data.categories.add(fact.get_cell(0, "c3", "B"))

            category = ch.chart_data.categories.add(fact.get_cell(0, "c4", "C"))
            category.GroupingLevels.SetGroupingItem(1, "Group2")
            category = ch.chart_data.categories.add(fact.get_cell(0, "c5", "D"))

            category = ch.chart_data.categories.add(fact.get_cell(0, "c6", "E"))
            category.GroupingLevels.SetGroupingItem(1, "Group3")
            category = ch.chart_data.categories.add(fact.get_cell(0, "c7", "F"))

            category = ch.chart_data.categories.add(fact.get_cell(0, "c8", "G"))
            category.GroupingLevels.SetGroupingItem(1, "Group4")
            category = ch.chart_data.categories.add(fact.get_cell(0, "c9", "H"))

            #            Adding Series
            series = ch.chart_data.series.add(fact.get_cell(0, "D1", "Series 1"),
                ChartType.CLUSTERED_COLUMN)

            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D2", 10))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D3", 20))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D4", 30))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D5", 40))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D6", 50))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D7", 60))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D8", 70))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D9", 80))
            # Save presentation with chart
            pres.save(dataDir+"AsposeChart_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:MultiCategoryChart
        }
    }
}