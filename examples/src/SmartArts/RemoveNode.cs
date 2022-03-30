using System.IO
import aspose.slides as slides
using Aspose.slides.SmartArt

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class RemoveNode
    {
        public static void Run()
        {
            #ExStart:RemoveNode
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation
            using (Presentation pres = new Presentation(dataDir+ "RemoveNode.pptx"))
            {

                # Traverse through every shape inside first slide
                foreach (IShape shape in pres.slides[0].shapes)
                {

                    # Check if shape is of SmartArt type
                    if (shape is ISmartArt)
                    {
                        # Typecast shape to SmartArtEx
                        ISmartArt smart = (ISmartArt)shape

                        if (smart.AllNodes.Count > 0)
                        {
                            # Accessing SmartArt node at index 0
                            ISmartArtNode node = smart.AllNodes[0]

                            # Removing the selected node
                            smart.AllNodes.RemoveNode(node)

                        }
                    }
                }

                # Save Presentation
                pres.save(dataDir + "RemoveSmartArtNode_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:RemoveNode
        }
    }
}