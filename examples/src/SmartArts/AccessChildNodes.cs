using System.IO
import aspose.slides as slides
using System

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AccessChildNodes
    {
        public static void Run()
        {
            #ExStart:AccessChildNodes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation
            Presentation pres = new Presentation(dataDir+ "AccessChildNodes.pptx")

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
                        Aspose.slides.SmartArt.SmartArtNode node0 = (Aspose.slides.SmartArt.SmartArtNode)smart.AllNodes[i]

                        # Traversing through the child nodes in SmartArt node at index i
                        for (j = 0 j < node0.ChildNodes.Count j++)
                        {
                            # Accessing the child node in SmartArt node
                            Aspose.slides.SmartArt.SmartArtNode node = (Aspose.slides.SmartArt.SmartArtNode)node0.ChildNodes[j]

                            # Printing the SmartArt child node parameters
                            outString = string.format("j = {0}, Text = {1},  Level = {2}, Position = {3}", j, node.text_frame.text, node.Level, node.Position)
                            print(outString)
                        }
                    }
                }
            }
            #ExEnd:AccessChildNodes
        }
    }
}