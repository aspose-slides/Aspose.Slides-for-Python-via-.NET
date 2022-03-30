using System.IO

import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class ScatteredChart
    {
        public static void Run()
        {
            #ExStart:ScatteredChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            with slides.Presentation() as pres:

            slide = pres.slides[0]

            # Creating the default chart
            chart = slide.shapes.add_chart(slides.charts.ChartType.ScatterWithSmoothLines, 0, 0, 400, 400)

            # Getting the default chart data worksheet index
            defaultWorksheetIndex = 0

            # Getting the chart data worksheet
            fact = chart.chart_data.chart_data_workbook

            # Delete demo series
            chart.chart_data.series.clear()

            # Add new series
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 1, 1, "Series 1"), chart.type)
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 1, 3, "Series 2"), chart.type)

            # Take first chart series
            series = chart.chart_data.series[0]

            # Add new point (1:3) there.
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 2, 1, 1), fact.get_cell(defaultWorksheetIndex, 2, 2, 3))

            # Add new point (2:10)
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 3, 1, 2), fact.get_cell(defaultWorksheetIndex, 3, 2, 10))

            # Edit the type of series
            series.type = ChartType.ScatterWithStraightLinesAndMarkers

            # Changing the chart series marker
            series.marker.size = 10
            series.marker.Symbol = MarkerStyleType.Star

            # Take second chart series
            series = chart.chart_data.series[1]

            # Add new point (5:2) there.
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 2, 3, 5), fact.get_cell(defaultWorksheetIndex, 2, 4, 2))

            # Add new point (3:1)
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 3, 3, 3), fact.get_cell(defaultWorksheetIndex, 3, 4, 1))

            # Add new point (2:2)
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 4, 3, 2), fact.get_cell(defaultWorksheetIndex, 4, 4, 2))

            # Add new point (5:1)
            series.data_points.AddDataPointForScatterSeries(fact.get_cell(defaultWorksheetIndex, 5, 3, 5), fact.get_cell(defaultWorksheetIndex, 5, 4, 1))

            # Changing the chart series marker
            series.marker.size = 10
            series.marker.Symbol = MarkerStyleType.Circle

            pres.save(dataDir + "AsposeChart_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ScatteredChart
        }
    }
}