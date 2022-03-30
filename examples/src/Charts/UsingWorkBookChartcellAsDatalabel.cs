using Aspose.slides.Charts
using Aspose.slides.Export
using Aspose.slides.Animation
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
    public class UsingWorkBookChartcellAsDatalabel
    {
        public static void Run()
        {
            #ExStart:UsingWorkBookChartcellAsDatalabel
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()



            lbl0 = "Label 0 cell value"
            lbl1 = "Label 1 cell value"
            lbl2 = "Label 2 cell value"

            # Instantiate Presentation class that represents a presentation file 

            using (Presentation pres = new Presentation(dataDir + "chart2.pptx"))
            {
                slide = pres.slides[0]


                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 600, 400, True)

                IChartSeriesCollection series = chart.chart_data.series

                series[0].labels.default_data_label_format.ShowLabelValueFromCell = True

                wb = chart.chart_data.chart_data_workbook

                series[0].labels[0].ValueFromCell = wb.get_cell(0, "A10", lbl0)
                series[0].labels[1].ValueFromCell = wb.get_cell(0, "A11", lbl1)
                series[0].labels[2].ValueFromCell = wb.get_cell(0, "A12", lbl2)

                pres.save(dataDir + "resultchart.pptx", slides.export.SaveFormat.PPTX)

            }
       #ExEnd:UsingWorkBookChartcellAsDatalabel
        
        
        }
    }
}