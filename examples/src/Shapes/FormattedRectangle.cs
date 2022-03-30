using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FormattedRectangle
    {
        public static void Run()
        {
            #ExStart:FormattedRectangle
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
                IShape shp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 150, 150, 50)

                # Apply some formatting to rectangle shape
                shp.fill_format.fill_type = slides.FillType.SOLID
                shp.fill_format.solid_fill_color.color = Color.Chocolate

                # Apply some formatting to the line of rectangle
                shp.line_format.fill_format.fill_type = slides.FillType.SOLID
                shp.line_format.fill_format.solid_fill_color.color = Color.Black
                shp.line_format.width = 5

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShp2_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FormattedRectangle
        }
    }
}