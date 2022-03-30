using System.IO
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class number_format
    {
        public static void Run()
        {
            #ExStart:number_format
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate the presentation# Instantiate the presentation
            with slides.Presentation() as pres:

            # Access the first presentation slide
            slide = pres.slides[0]

            # Adding a defautlt clustered column chart
            chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 400)

            # Accessing the chart series collection
            IChartSeriesCollection series = chart.chart_data.series

            # Setting the preset number format
            # Traverse through every chart series
            foreach (ChartSeries ser in series)
            {
                # Traverse through every data cell in series
                foreach (cell in ser.data_points)
                {
                    # Setting the number format
                    cell.value.as_cell.PresetNumberFormat = 10 #0.00%
                }
            }

            # Saving presentation
            pres.save(dataDir + "PresetNumberFormat_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:number_format
        }
    }
}