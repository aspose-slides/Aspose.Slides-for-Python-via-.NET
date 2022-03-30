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
    public class SettingAutomicPieChartSliceColors
    {
        public static void Run()
        {
            #ExStart:SettingAutomicPieChartSliceColors
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            # Instantiate Presentation class that represents PPTX file
            with slides.Presentation() as presentation:
            {
              
             # Access first slide
             slides = presentation.slides[0]

             # Add chart with default data
             chart = slides.shapes.add_chart(slides.charts.ChartType.PIE, 100, 100, 400, 400)

             # Setting chart Title
             chart.chart_title.add_text_frame_for_overriding("Sample Title")
             chart.chart_title.text_frame_for_overriding.TextFrameFormat.CenterText = 1
             chart.chart_title.height = 20
             chart.has_title = True

             # Set first series to Show Values
             chart.chart_data.series[0].labels.default_data_label_format.show_value = True

             # Setting the index of chart data sheet
             defaultWorksheetIndex = 0

             # Getting the chart data worksheet
             fact = chart.chart_data.chart_data_workbook

             # Delete default generated series and categories
             chart.chart_data.series.clear()
             chart.chart_data.categories.clear()

             # Adding new categories
             chart.chart_data.categories.add(fact.get_cell(0, 1, 0, "First Qtr"))
             chart.chart_data.categories.add(fact.get_cell(0, 2, 0, "2nd Qtr"))
             chart.chart_data.categories.add(fact.get_cell(0, 3, 0, "3rd Qtr"))

             # Adding new series
             series = chart.chart_data.series.add(fact.get_cell(0, 0, 1, "Series 1"), chart.type)

             # Now populating series data
             series.data_points.AddDataPointForPieSeries(fact.get_cell(defaultWorksheetIndex, 1, 1, 20))
             series.data_points.AddDataPointForPieSeries(fact.get_cell(defaultWorksheetIndex, 2, 1, 50))
             series.data_points.AddDataPointForPieSeries(fact.get_cell(defaultWorksheetIndex, 3, 1, 30))
            
             series.parent_series_group.IsColorVaried = True
             presentation.save(dataDir + "Pie.pptx", slides.export.SaveFormat.PPTX)
         }
            }
            #ExEnd:SettingAutomicPieChartSliceColors
        }
    }
