using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FormatJoinStyles
    {
        public static void Run()
        {
            #ExStart:FormatJoinStyles

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add three autoshapes of rectangle type
                IShape shp1 = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 100, 150, 75)
                IShape shp2 = sld.shapes.add_auto_shape(ShapeType.Rectangle, 300, 100, 150, 75)
                IShape shp3 = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 250, 150, 75)

                # Set the fill color of the rectangle shape
                shp1.fill_format.fill_type = slides.FillType.SOLID
                shp1.fill_format.solid_fill_color.color = Color.Black
                shp2.fill_format.fill_type = slides.FillType.SOLID
                shp2.fill_format.solid_fill_color.color = Color.Black
                shp3.fill_format.fill_type = slides.FillType.SOLID
                shp3.fill_format.solid_fill_color.color = Color.Black

                # Set the line width
                shp1.line_format.width = 15
                shp2.line_format.width = 15
                shp3.line_format.width = 15

                # Set the color of the line of rectangle
                shp1.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp1.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
                shp2.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp2.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
                shp3.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp3.line_format.fill_format.solid_fill_color.color = drawing.Color.blue

                # Set the Join Style
                shp1.line_format.JoinStyle = LineJoinStyle.Miter
                shp2.line_format.JoinStyle = LineJoinStyle.Bevel
                shp3.line_format.JoinStyle = LineJoinStyle.Round

                # Add text to each rectangle
                ((IAutoShape)shp1).text_frame.text = "This is Miter Join Style"
                ((IAutoShape)shp2).text_frame.text = "This is Bevel Join Style"
                ((IAutoShape)shp3).text_frame.text = "This is Round Join Style"

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpLnJoin_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FormatJoinStyles
        }
    }
}