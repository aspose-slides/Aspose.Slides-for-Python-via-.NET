import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
    class HideInformationFromChart
    {
        public static void Run() {

            #ExStart:HideInformationFromChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            {
                slide = pres.slides[0]
                chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 140, 118, 320, 370)

                #Hiding chart Title
                chart.has_title = False

                #/Hiding Values axis
                chart.axes.vertical_axis.is_visible = False

                #Category Axis visibility
                chart.axes.horizontal_axis.is_visible = False

                #Hiding Legend
                chart.has_legend = False

                #Hiding MajorGridLines
                chart.axes.horizontal_axis.major_grid_lines_format.line.FillFormat.fill_type = FillType.NoFill

                for (i = 0 i < chart.chart_data.series.Count i++)
                {
                    chart.chart_data.series.remove_at(i)
                }

                series = chart.chart_data.series[0]

                series.marker.Symbol = MarkerStyleType.Circle
                series.labels.default_data_label_format.show_value = True
                series.labels.default_data_label_format.Position = LegendDataLabelPosition.Top
                series.marker.size = 15

                #Setting series line color
                series.format.line.fill_format.fill_type = slides.FillType.SOLID
                series.format.line.fill_format.solid_fill_color.color = Color.Purple
                series.format.line.dash_style = LineDashStyle.Solid

                pres.save(dataDir + "HideInformationFromChart.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:HideInformationFromChart
        }
    }
}
