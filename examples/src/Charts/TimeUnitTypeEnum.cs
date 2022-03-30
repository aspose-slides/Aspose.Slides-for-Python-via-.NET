using System
import aspose.pydrawing as drawing
using System.IO

import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
This sample demonstrates using  TimeUnitType enumeration
*/

namespace CSharp.Charts
{
    public class TimeUnitTypeEnum
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "TimeUnitTypeEnum.pptx")

            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 10, 10, 400, 300, True)
                chart.axes.horizontal_axis.major_unit_scale = TimeUnitType.NONE
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
