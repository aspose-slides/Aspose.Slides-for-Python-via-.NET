using System.IO

import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class ExistingChart
    {
        public static void Run()
        {
            #ExStart:ExistingChart
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Instantiate Presentation class that represents PPTX file# Instantiate Presentation class that represents PPTX file
            Presentation pres = new Presentation(dataDir + "ExistingChart.pptx")

            # Access first slideMarker
            sld = pres.slides[0]

            # Add chart with default data
            chart = sld.shapes[0]

            # Setting the index of chart data sheet
            defaultWorksheetIndex = 0

            # Getting the chart data worksheet
            fact = chart.chart_data.chart_data_workbook


            # Changing chart Category Name
            fact.get_cell(defaultWorksheetIndex, 1, 0, "Modified Category 1")
            fact.get_cell(defaultWorksheetIndex, 2, 0, "Modified Category 2")


            # Take first chart series
            series = chart.chart_data.series[0]

            # Now updating series data
            fact.get_cell(defaultWorksheetIndex, 0, 1, "New_Series1")# Modifying series name
            series.data_points[0].value.Data = 90
            series.data_points[1].value.Data = 123
            series.data_points[2].value.Data = 44

            # Take Second chart series
            series = chart.chart_data.series[1]

            # Now updating series data
            fact.get_cell(defaultWorksheetIndex, 0, 2, "New_Series2")# Modifying series name
            series.data_points[0].value.Data = 23
            series.data_points[1].value.Data = 67
            series.data_points[2].value.Data = 99


            # Now, Adding a new series
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 0, 3, "Series 3"), chart.type)

            # Take 3rd chart series
            series = chart.chart_data.series[2]

            # Now populating series data
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 1, 3, 20))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 2, 3, 50))
            series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, 3, 3, 30))

            chart.type = ChartType.ClusteredCylinder

            # Save presentation with chart
            pres.save(dataDir + "AsposeChartModified_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ExistingChart
        }
    }
}