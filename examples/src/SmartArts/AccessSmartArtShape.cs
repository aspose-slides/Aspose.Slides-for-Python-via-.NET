using System.IO

import aspose.slides as slides
using Aspose.slides.SmartArt

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AccessSmartArtShape
    {
        public static void Run()
        {
            #ExStart:AccessSmartArtShape
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation
            using (Presentation pres = new Presentation(dataDir + "AccessSmartArtShape.pptx"))
            {

                # Traverse through every shape inside first slide
                foreach (IShape shape in pres.slides[0].shapes)
                {
                    # Check if shape is of SmartArt type
                    if (shape is ISmartArt)
                    {
                        # Typecast shape to SmartArtEx
                        ISmartArt smart = (ISmartArt)shape
                        print("Shape Name:" + smart.Name)

                    }
                }
            }
            #ExEnd:AccessSmartArtShape
        }
    }
}