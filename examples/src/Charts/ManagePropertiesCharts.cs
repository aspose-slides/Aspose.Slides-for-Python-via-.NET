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
    public class ManagePropertiesCharts
    {
        public static void Run()
        {
            #ExStart:ManagePropertiesCharts
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:
           
            # Access first slide
            slide = presentation.slides[0]

            # Add chart with default data
            chart = slide.shapes.add_chart(slides.charts.ChartType.StackedColumn3D, 0, 0, 500, 500)

            # Setting the index of chart data sheet
            defaultWorksheetIndex = 0

            # Getting the chart data worksheet
            fact = chart.chart_data.chart_data_workbook

            # Add series
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 0, 1, "Series 1"), chart.type)
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 0, 2, "Series 2"), chart.type)

            # Add Catrgories
            chart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 1, 0, "Caetegoty 1"))
            chart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 2, 0, "Caetegoty 2"))
            chart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 3, 0, "Caetegoty 3"))

            # Set Rotation3D properties
            chart.Rotation3D.RightAngleAxes = True
            chart.Rotation3D.RotationX = 40
            chart.Rotation3D.RotationY = 270
            chart.Rotation3D.DepthPercents = 150

            # Take second chart series
            series = chart.chart_data.series[1]

            # Now populating series data
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 1, 1, 20))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 2, 1, 50))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 3, 1, 30))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 1, 2, 30))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 2, 2, 10))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 3, 2, 60))

            # Set OverLap value
            series.parent_series_group.Overlap = 100         

            # Write presentation to disk
            presentation.save(dataDir + "Rotation3D_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ManagePropertiesCharts
        }
    }
}