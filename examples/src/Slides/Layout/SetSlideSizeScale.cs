using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Export
using Aspose.slides.Examples.CSharp

namespace Aspose.slides.Examples.CSharp.slides.Layout
{
    class SetSlideSizeScale
    {
        public static void Run()
        {

            #ExStart:SetSlideSizeScale
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()

            # ExStart:SettSizeAndType
            # Instantiate a Presentation object that represents a presentation file 
            Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx")
            Presentation auxPresentation = new Presentation()

            slide = presentation.slides[0]

            # Set the slide size of generated presentations to that of source
            presentation.SlideSize.SetSize(540, 720, SlideSizeScaleType.EnsureFit) # Method SetSize is used for set slide size with scale content to ensure fit
            presentation.SlideSize.SetSize(SlideSizeType.A4Paper, SlideSizeScaleType.Maximize) # Method SetSize is used for set slide size with maximize size of content

          
           
            # Save Presentation to disk
            auxPresentation.save(dataDir + "Set_Size&Type_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetSlideSizeScale
            
            
        
            
           
        
        }
    }
}
