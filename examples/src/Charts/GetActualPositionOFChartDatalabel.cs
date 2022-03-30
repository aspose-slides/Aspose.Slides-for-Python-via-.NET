using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.slides as slides
import aspose.pydrawing as drawing

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class GetActualPositionOFChartDatalabel
    {
        public static void Run()
        {
            #ExStart:GetActualPositionOFChartDatalabel
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 400)
                foreach (series in chart.chart_data.series)
                {
                    series.labels.default_data_label_format.Position = LegendDataLabelPosition.OutsideEnd
                    series.labels.default_data_label_format.show_value = True
                }

                chart.validate_chart_layout()

                foreach (series in chart.chart_data.series)
                {
                    foreach (point in series.data_points)
                    {
                        if (point.value.ToDouble() > 4)
                        {
                            float x = point.label.ActualX
                            float y = point.label.ActualY
                            float w = point.label.ActualWidth
                            float h = point.label.ActualHeight

                            shape = chart.user_shapes.shapes.add_auto_shape(ShapeType.Ellipse, x, y, w, h)
                            shape.fill_format.fill_type = slides.FillType.SOLID
                            shape.fill_format.solid_fill_color.color = drawing.Color.from_argb(100, 0, 255, 0)
                        }
                    }
                }

                pres.save(dataDir + "GetActualPositionOFChartDatalabel", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:GetActualPositionOFChartDatalabel
        }
    }
}