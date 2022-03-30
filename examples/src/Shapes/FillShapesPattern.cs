using System.IO
import aspose.slides as slides
using Aspose.slides.Export
import aspose.pydrawing as drawing

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FillShapesPattern
    {
        public static void Run()
        {
            #ExStart:FillShapesPattern
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

                # Add autoshape of rectangle type
                IShape shp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 150, 75, 150)

                # Set the fill type to Pattern
                shp.fill_format.fill_type = FillType.Pattern

                # Set the pattern style
                shp.FillFormat.PatternFormat.PatternStyle = PatternStyle.Trellis

                # Set the pattern back and fore colors
                shp.FillFormat.PatternFormat.BackColor.color = Color.light_gray
                shp.FillFormat.PatternFormat.ForeColor.color = drawing.Color.yellow

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpPatt_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FillShapesPattern
        }
    }
}