using System
import aspose.pydrawing as drawing
using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class SetMarkerOptions
    {
        public static void Run()
        {
            #ExStart:SetMarkerOptions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            slide = presentation.slides[0]

            # Creating the default chart
            chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 0, 0, 400, 400)

            # Getting the default chart data worksheet index
            defaultWorksheetIndex = 0

            # Getting the chart data worksheet
            fact = chart.chart_data.chart_data_workbook

            # Delete demo series
            chart.chart_data.series.clear()

            # Add new series
            chart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 1, 1, "Series 1"), chart.type)
            
            # Set the picture
            image1 = drawing.Bitmap(dataDir + "aspose-logo.jpg")
            imgx1 = presentation.images.add_image(image1)

            # Set the picture
            image2 = drawing.Bitmap(dataDir + "Tulips.jpg")
            imgx2 = presentation.images.add_image(image2)

            # Take first chart series
            series = chart.chart_data.series[0]

            # Add new point (1:3) there.
            point = series.data_points.add_data_point_for_line_series(fact.get_cell(defaultWorksheetIndex, 1, 1, 4.5))
            point.marker.format.fill.fill_type = slides.FillType.PICTURE
            point.marker.format.fill.picture_fill_format.picture.image = imgx1

            point = series.data_points.add_data_point_for_line_series(fact.get_cell(defaultWorksheetIndex, 2, 1, 2.5))
            point.marker.format.fill.fill_type = slides.FillType.PICTURE
            point.marker.format.fill.picture_fill_format.picture.image = imgx2

            point = series.data_points.add_data_point_for_line_series(fact.get_cell(defaultWorksheetIndex, 3, 1, 3.5))
            point.marker.format.fill.fill_type = slides.FillType.PICTURE
            point.marker.format.fill.picture_fill_format.picture.image = imgx1

            point = series.data_points.add_data_point_for_line_series(fact.get_cell(defaultWorksheetIndex, 4, 1, 4.5))
            point.marker.format.fill.fill_type = slides.FillType.PICTURE
            point.marker.format.fill.picture_fill_format.picture.image = imgx2

            # Changing the chart series marker
            series.marker.size = 15

            # Write presentation to disk
            presentation.save(dataDir + "MarkOptions_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetMarkerOptions
        }
    }
}