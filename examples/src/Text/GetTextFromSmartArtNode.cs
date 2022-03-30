using System.IO

import aspose.slides as slides
using Aspose.slides.SmartArt
using System

namespace Aspose.slides.Examples.CSharp.text
{
    public class GetTextFromSmartArtNode
    {
        public static void Run()
        {
            # ExStart:GetTextFromSmartArtNode
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

          using (Presentation presentation = new Presentation("Presentation.pptx"))
{
            slide = presentation.slides[0]
            ISmartArt smartArt = (ISmartArt)slide.shapes[0]

            ISmartArtNodeCollection smartArtNodes = smartArt.AllNodes
            foreach (ISmartArtNode smartArtNode in smartArtNodes)
            {
                foreach (ISmartArtShape nodeShape in smartArtNode.shapes)
                {
                    if (nodeShape.text_frame != None)
                        print(nodeShape.text_frame.text)
                }
            }
            }
            }
        # ExEnd:GetTextFromSmartArtNode
        }
    }
