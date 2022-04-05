using System.IO
import aspose.slides as slides
using System

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FindShapeInSlide
    {
        #ExStart:FindShapeInSlide
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate a Presentation class that represents the presentation file
            using (Presentation p = new Presentation(dataDir + "FindingShapeInSlide.pptx"))
            {

                slide = p.slides[0]
                # Alternative text of the shape to be found
                shape = FindShape(slide, "Shape1")
                if (shape != None)
                {
                    print("Shape Name: " + shape.name)
                }
            }
        }
        
        # Method implementation to find a shape in a slide using its alternative text
        public static IShape FindShape(slide, alttext)
        {
            # Iterating through all shapes inside the slide
            for (i = 0 i < slide.shapes.Count i++)
            {
                # If the alternative text of the slide matches with the required one then
                # Return the shape
                if (slide.shapes[i].alternative_text.CompareTo(alttext) == 0)
                    return slide.shapes[i]
            }
            return None
        }
        #ExEnd:FindShapeInSlide
    }
}

