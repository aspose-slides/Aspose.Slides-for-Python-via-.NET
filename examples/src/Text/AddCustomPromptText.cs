import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class AddCustomPromptText
    {
        public static void Run() {

            #ExStart:AddCustomPromptText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            using (Presentation pres = new Presentation(dataDir + "Presentation2.pptx"))
            {
                slide = pres.slides[0]
                foreach (IShape shape in slide.Slide.shapes) # iterate through the slide
                {
                    if (shape.Placeholder != None && shape is AutoShape)
                    {
                        text = ""
                        if (shape.Placeholder.type == PlaceholderType.CenteredTitle) # title - the text is empty, PowerPoint displays "Click to add title". 
                        {
                            text = "Click to add custom title"
                        }
                        else if (shape.Placeholder.type == PlaceholderType.Subtitle) # the same for subtitle.
                        {
                            text = "Click to add custom subtitle"
                        }

                        ((IAutoShape)shape).text_frame.text = text

                        print("Placeholder with text: {0}", text)
                    }
                }

                pres.save(dataDir + "Placeholders_PromptText.pptx", slides.export.SaveFormat.PPTX)
            }



            #ExEnd:AddCustomPromptText

        }
    }
}
