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
    class SetLayoutMode
    {
        public static void Run() {

            #ExStart:SetLayoutMode
            dataDir = RunExamples.GetDataDir_Charts()
            with slides.Presentation() as presentation:
            {
                slide = presentation.slides[0]
                chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 100, 600, 400)
                chart.plot_area.as_ilayoutable.x = 0.2f
                chart.plot_area.as_ilayoutable.y = 0.2f
                chart.plot_area.as_ilayoutable.width = 0.7f
                chart.plot_area.as_ilayoutable.height = 0.7f
                chart.plot_area.LayoutTargetType = LayoutTargetType.Inner

                presentation.save(dataDir + "SetLayoutMode_outer.pptx", slides.export.SaveFormat.PPTX)
   
}
            #ExEnd:SetLayoutMode
        }
    }
}
