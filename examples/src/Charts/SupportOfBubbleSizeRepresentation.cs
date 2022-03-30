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
    class SupportOfBubbleSizeRepresentation
    {

        public static void Run() {


            #ExStart:SupportOfBubbleSizeRepresentation
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 600, 400, True)

                chart.chart_data.SeriesGroups[0].BubbleSizeRepresentation = BubbleSizeRepresentationType.width

                pres.save(dataDir+ "Presentation_BubbleSizeRepresentation.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SupportOfBubbleSizeRepresentation

        }
    }
}
