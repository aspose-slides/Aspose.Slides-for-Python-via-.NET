using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AddArrowShapedLineToSlide
    {
        public static void Run()
        {
            #ExStart:AddArrowShapedLineToSlide
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PresentationEx class that represents the PPTX file
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add an autoshape of type line
                shp = sld.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

                # Apply some formatting on the line
                shp.line_format.style = LineStyle.ThickBetweenThin
                shp.line_format.width = 10

                shp.line_format.dash_style = slides.LineDashStyle.DASH_DOT

                shp.line_format.BeginArrowheadLength = LineArrowheadLength.Short
                shp.line_format.BeginArrowheadStyle = LineArrowheadStyle.Oval

                shp.line_format.EndArrowheadLength = LineArrowheadLength.Long
                shp.line_format.EndArrowheadStyle = LineArrowheadStyle.Triangle

                shp.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp.line_format.fill_format.solid_fill_color.color = Color.Maroon

                #Write the PPTX to Disk
                pres.save(dataDir + "LineShape2_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddArrowShapedLineToSlide
        }
    }
}