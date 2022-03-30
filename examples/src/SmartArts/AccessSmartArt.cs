using System.IO
import aspose.slides as slides
using System

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AccessSmartArt
    {
        public static void Run()
        {
            #ExStart:AccessSmartArt
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation
             Presentation pres = new Presentation(dataDir + "AccessSmartArt.pptx")

            # Traverse through every shape inside first slide
            foreach (IShape shape in pres.slides[0].shapes)
            {
                # Check if shape is of SmartArt type
                if (shape is Aspose.slides.SmartArt.SmartArt)
                {

                    # Typecast shape to SmartArt
                    Aspose.slides.SmartArt.SmartArt smart = (Aspose.slides.SmartArt.SmartArt)shape

                    # Traverse through all nodes inside SmartArt
                    for (i = 0 i < smart.AllNodes.Count i++)
                    {
                        # Accessing SmartArt node at index i
                        Aspose.slides.SmartArt.SmartArtNode node = (Aspose.slides.SmartArt.SmartArtNode)smart.AllNodes[i]

                        # Printing the SmartArt node parameters
                        outString = string.format("i = {0}, Text = {1},  Level = {2}, Position = {3}", i, node.text_frame.text, node.Level, node.Position)
                        print(outString)
                    }
                }
            }
            #ExEnd:AccessSmartArt
        }
    }
}