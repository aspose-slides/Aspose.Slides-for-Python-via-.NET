using System
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
    public class DisplayPercentageAsLabels
    {
        public static void Run()
        {
            #ExStart:DisplayPercentageAsLabels
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            slide = presentation.slides[0]
            chart = slide.shapes.add_chart(slides.charts.ChartType.StackedColumn, 20, 20, 400, 400)
            series = chart.chart_data.series[0]
            IChartCategory cat
            double[] total_for_Cat = new double[chart.chart_data.categories.Count]
            for (k = 0 k < chart.chart_data.categories.Count k++)
            {
                cat = chart.chart_data.categories[k]

                for (i = 0 i < chart.chart_data.series.Count i++)
                {
                    total_for_Cat[k] = total_for_Cat[k] + Convert.ToDouble(chart.chart_data.series[i].data_points[k].value.Data)
                }
            }

            double dataPontPercent = 0f

            for (x = 0 x < chart.chart_data.series.Count x++)
            {
                series = chart.chart_data.series[x]
                series.labels.default_data_label_format.ShowLegendKey = False

                for (j = 0 j < series.data_points.Count j++)
                {
                    lbl = series.data_points[j].label
                    dataPontPercent = (Convert.ToDouble(series.data_points[j].value.Data) / total_for_Cat[j]) * 100

                    port = new Portion()
                    port.text = String.format("{0:F2} %", dataPontPercent)
                    port.portion_format.font_height = 8f
                    lbl.text_frame_for_overriding.text = ""
                    IParagraph para = lbl.text_frame_for_overriding.paragraphs[0]
                    para.portions.add(port)

                    lbl.data_label_format.show_series_name = False
                    lbl.data_label_format.ShowPercentage = False
                    lbl.data_label_format.ShowLegendKey = False
                    lbl.data_label_format.show_category_name = False
                    lbl.data_label_format.ShowBubbleSize = False

                }

            }

            # Save presentation with chart
            presentation.save(dataDir + "DisplayPercentageAsLabels_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:DisplayPercentageAsLabels
        }
    }
}