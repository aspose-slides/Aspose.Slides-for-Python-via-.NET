using System.IO
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.pydrawing as drawing

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class ValidateChartLayoutAdded
    {
        public static void Run()
        {
            #ExStart:ValidateChartLayoutAdded
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            using (Presentation pres = new Presentation(dataDir+"test.pptx"))
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
                chart.validate_chart_layout()
                x = chart.plot_area.actual_x
                y = chart.plot_area.actual_y
                w = chart.plot_area.actual_width
                h = chart.plot_area.actual_height


                # Saving presentation
                pres.save(dataDir + "Result.pptx", slides.export.SaveFormat.PPTX)
            }
          

            
            #ExEnd:ValidateChartLayoutAdded
        }
    }
}