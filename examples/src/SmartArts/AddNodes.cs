 using System.IO
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
namespace Aspose.slides.Examples.CSharp.SmartArts

{
    public class AddNodes
    {
        public static void Run()
        {
            #ExStart:AddNodes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Load the desired the presentation# Load the desired the presentation
            Presentation pres = new Presentation(dataDir+ "AddNodes.pptx")

            # Traverse through every shape inside first slide
            foreach (IShape shape in pres.slides[0].shapes)
            {

                # Check if shape is of SmartArt type
                if (shape is Aspose.slides.SmartArt.SmartArt)
                {

                    # Typecast shape to SmartArt
                    Aspose.slides.SmartArt.SmartArt smart = (Aspose.slides.SmartArt.SmartArt)shape

                    # Adding a new SmartArt Node
                    Aspose.slides.SmartArt.SmartArtNode TemNode = (Aspose.slides.SmartArt.SmartArtNode)smart.AllNodes.AddNode()

                    # Adding text
                    TemNode.text_frame.text = "Test"

                    # Adding new child node in parent node. It  will be added in the end of collection
                    Aspose.slides.SmartArt.SmartArtNode newNode = (Aspose.slides.SmartArt.SmartArtNode)TemNode.ChildNodes.AddNode()

                    # Adding text
                    newNode.text_frame.text = "New Node Added"

                }
            }

            # Saving Presentation
            pres.save(dataDir + "AddSmartArtNode_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:AddNodes
        }
    }
}