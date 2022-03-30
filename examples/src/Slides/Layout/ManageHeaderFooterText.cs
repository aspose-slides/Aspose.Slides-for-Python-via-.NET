import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Layout
{
    class ManageHeaderFooterText
    {
        public static void Run() {

            #ExStart:ManageHeaderFooterText

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()

            # Load Presentation
            Presentation pres = new Presentation(dataDir + "headerTest.pptx")

            # Setting Footer
            pres.HeaderFooterManager.SetAllFootersText("My Footer text")
            pres.HeaderFooterManager.SetAllFootersVisibility(True)

            # Access and Update Header
            IMasterNotesSlide masterNotesSlide = pres.MasterNotesSlideManager.MasterNotesSlide
            if (None != masterNotesSlide)
            {
                UpdateHeaderFooterText(masterNotesSlide)
            }

            # Save presentation
            pres.save(dataDir + "HeaderFooterJava.pptx", slides.export.SaveFormat.PPTX)

            #ExEnd:ManageHeaderFooterText

        }

        #ExStart:UpdateHeaderFooterText
        # Method to set Header/Footer Text
        public static void UpdateHeaderFooterText(IBaseSlide master)
        {
            foreach (IShape shape in master.shapes)
            {
                if (shape.Placeholder != None)
                {
                    if (shape.Placeholder.type == PlaceholderType.Header)
                    {
                        ((IAutoShape)shape).text_frame.text = "HI there new header"
                    }
                }
            }
        }
        #ExEnd:UpdateHeaderFooterText
    }
}
