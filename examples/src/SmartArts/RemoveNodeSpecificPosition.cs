using System.IO
import aspose.slides as slides
using Aspose.slides.Examples.CSharp

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class RemoveNodeSpecificPosition
    {
        public static void Run()
        {
            #ExStart:RemoveNodeSpecificPosition
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation             
            Presentation pres = new Presentation(dataDir + "RemoveNodeSpecificPosition.pptx")

            # Traverse through every shape inside first slide
            foreach (IShape shape in pres.slides[0].shapes)
            {
                # Check if shape is of SmartArt type
                if (shape is Aspose.slides.SmartArt.SmartArt)
                {
                    # Typecast shape to SmartArt
                    Aspose.slides.SmartArt.SmartArt smart = (Aspose.slides.SmartArt.SmartArt)shape

                    if (smart.AllNodes.Count > 0)
                    {
                        # Accessing SmartArt node at index 0
                        Aspose.slides.SmartArt.ISmartArtNode node = smart.AllNodes[0]

                        if (node.ChildNodes.Count >= 2)
                        {
                            # Removing the child node at position 1
                            ((Aspose.slides.SmartArt.SmartArtNodeCollection)node.ChildNodes).RemoveNode(1)
                        }

                    }
                }
            }

            # Save Presentation
            pres.save(dataDir + "RemoveSmartArtNodeByPosition_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:RemoveNodeSpecificPosition
        }
    }
}