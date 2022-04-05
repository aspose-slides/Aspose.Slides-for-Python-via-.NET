
using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FormatLines
    {
        public static void Run()
        {
            #ExStart:FormatLines
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of rectangle type
                shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 75)

                # Set the fill color of the rectangle shape
                shp.fill_format.fill_type = slides.FillType.SOLID
                shp.fill_format.solid_fill_color.color = drawing.Color.white

                # Apply some formatting on the line of the rectangle
                shp.line_format.style = LineStyle.ThickThin
                shp.line_format.width = 7
                shp.line_format.dash_style = LineDashStyle.Dash

                # Set the color of the line of rectangle
                shp.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp.line_format.fill_format.solid_fill_color.color = drawing.Color.blue

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpLn_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FormatLines
        }
    }
}