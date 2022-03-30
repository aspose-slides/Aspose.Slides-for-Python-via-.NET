using System.IO
import aspose.slides as slides
using Aspose.slides.SmartArt
using System

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AccessChildNodeSpecificPosition
    {
        public static void Run()
        {
            #ExStart:AccessChildNodeSpecificPosition
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate the presentation
            with slides.Presentation() as pres:

            # Accessing the first slide
            slide = pres.slides[0]

            # Adding the SmartArt shape in first slide
            ISmartArt smart = slide.shapes.AddSmartArt(0, 0, 400, 400, SmartArtLayoutType.StackedList)

            # Accessing the SmartArt  node at index 0
            ISmartArtNode node = smart.AllNodes[0]

            # Accessing the child node at position 1 in parent node
            position = 1
            SmartArtNode chNode = (SmartArtNode)node.ChildNodes[position] 

            # Printing the SmartArt child node parameters
            outString = string.format("j = {0}, Text = {1},  Level = {2}, Position = {3}", position, chNode.text_frame.text, chNode.Level, chNode.Position)
            print(outString)
            #ExEnd:AccessChildNodeSpecificPosition
        }
    }
}