using System.IO
import aspose.slides as slides
using System

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AssistantNode
    {
        public static void Run()
        {
            #ExStart:AssistantNode
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Creating a presentation instance
            using (Presentation pres = new Presentation(dataDir+ "AssistantNode.pptx"))
            {
                # Traverse through every shape inside first slide
                foreach (IShape shape in pres.slides[0].shapes)
                {
                    # Check if shape is of SmartArt type
                    if (shape is Aspose.slides.SmartArt.ISmartArt)
                    {
                        # Typecast shape to SmartArtEx
                        Aspose.slides.SmartArt.ISmartArt smart = (Aspose.slides.SmartArt.SmartArt)shape
                        # Traversing through all nodes of SmartArt shape

                        foreach (Aspose.slides.SmartArt.ISmartArtNode node in smart.AllNodes)
                        {
                            tc = node.text_frame.text
                            # Check if node is Assitant node
                            if (node.IsAssistant)
                            {
                                # Setting Assitant node to False and making it normal node
                                node.IsAssistant = False
                            }
                        }
                    }
                }
                # Save Presentation
                pres.save(dataDir + "ChangeAssitantNode_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AssistantNode
        }
    }
}