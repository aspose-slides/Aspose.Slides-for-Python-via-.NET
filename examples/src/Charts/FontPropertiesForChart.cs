import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
    class FontPropertiesForChart
    {
        public static void Run() {

            #ExStart:FontPropertiesForChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            {               

                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 400)
                chart.text_format.portion_format.font_height = 20
                chart.chart_data.series[0].labels.default_data_label_format.show_value = True
                pres.save(dataDir + "FontPropertiesForChart.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:FontPropertiesForChart

        }
    }
}
