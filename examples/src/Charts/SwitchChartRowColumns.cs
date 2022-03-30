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
    public class SwitchChartRowColumns
    {
        public static void Run()
        {
            #ExStart:SwitchChartRowColumns
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Creating empty presentation
            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)

                #Add data
                IChartSeries[] series = new IChartSeries[chart.chart_data.series.Count]
                chart.chart_data.series.CopyTo(series, 0)

                IChartDataCell[] categoriesCells = new IChartDataCell[chart.chart_data.categories.Count]

                for (i = 0 i < chart.chart_data.categories.Count i++)
                {
                    categoriesCells[i] = chart.chart_data.categories[i].as_cell
                }

                IChartDataCell[] seriesCells = new IChartDataCell[chart.chart_data.series.Count]
                for (i = 0 i < chart.chart_data.series.Count i++)
                {
                    seriesCells[i] = chart.chart_data.series[i].Name.AsCells[0]
                }

                #Switching rows and columns
                chart.chart_data.SwitchRowColumn()
           
                # Saving presentation
                pres.save(RunExamples.OutPath + "SwitchChartRowColumns_out.pptx", slides.export.SaveFormat.PPTX)
                #ExEnd:SwitchChartRowColumns
            }
        }
    }
}
