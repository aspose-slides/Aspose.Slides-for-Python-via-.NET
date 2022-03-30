using System.IO

import aspose.slides as slides
using Aspose.slides.Charts
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class GetWidthHeightFromChartPlotArea
    {
        public static void Run()
        {
            #ExStart:GetWidthHeightFromChartPlotArea
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            using (Presentation pres = new Presentation(dataDir+"test.Pptx"))
            {
                Chart chart = (Chart)pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
                chart.validate_chart_layout()

                double x = chart.plot_area.ActualX
                double y = chart.plot_area.ActualY
                double w = chart.plot_area.ActualWidth
                double h = chart.plot_area.ActualHeight

                # Save presentation with chart
                pres.save(dataDir + "Chart_out.pptx", slides.export.SaveFormat.PPTX)
            }
                        
            
            #ExEnd:GetWidthHeightFromChartPlotArea
        }
    }
}