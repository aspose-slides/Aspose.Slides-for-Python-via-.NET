using System.IO
import aspose.slides as slides
import aspose.slides as slides
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
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of rectangle type
                shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

                # Set the fill type to Pattern
                shp.fill_format.fill_type = FillType.Pattern

                # Set the pattern style
                shp.fill_format.PatternFormat.PatternStyle = PatternStyle.Trellis

                # Set the pattern back and fore colors
                shp.fill_format.PatternFormat.BackColor.color = drawing.Color.light_gray
                shp.fill_format.PatternFormat.ForeColor.color = drawing.Color.yellow

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpPatt_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FillShapesPattern
        }
    }
}