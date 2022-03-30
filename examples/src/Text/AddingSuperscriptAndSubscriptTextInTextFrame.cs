using Aspose.slides.Export
using Aspose.slides.Charts
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class AddingSuperscriptAndSubscriptTextInTextFrame
    {
        public static void Run()
        {
           
             #ExStart:AddingSuperscriptAndSubscriptTextInTextFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            with slides.Presentation() as presentation:
            {
                # Get slide
                slide = presentation.slides[0]

                # Create text box
                shape = slide.shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 200, 100)
                ITextFrame textFrame = shape.text_frame
                textFrame.Paragraphs.clear()

                # Create paragraph for superscript text
                superPar = new Paragraph()

                # Create portion with usual text
                portion1 = slides.Portion()
                portion1.text = "SlideTitle"
                superPar.portions.add(portion1)

                # Create portion with superscript text
                superPortion = slides.Portion()
                superPortion.portion_format.Escapement = 30
                superPortion.text = "TM"
                superPar.portions.add(superPortion)

                # Create paragraph for subscript text
                paragraph2 = new Paragraph()

                # Create portion with usual text
                portion2 = slides.Portion()
                portion2.text = "a"
                paragraph2.portions.add(portion2)

                # Create portion with subscript text
                subPortion = slides.Portion()
                subPortion.portion_format.Escapement = -25
                subPortion.text = "i"
                paragraph2.portions.add(subPortion)

                # Add paragraphs to text box
                textFrame.Paragraphs.add(superPar)
                textFrame.Paragraphs.add(paragraph2)

                presentation.save(RunExamples.OutPath + "TestOut.pptx", slides.export.SaveFormat.PPTX)
                System.Diagnostics.Process.Start(RunExamples.OutPath + "TestOut.pptx")
             } 
            #ExEnd:AddingSuperscriptAndSubscriptTextInTextFrame
        }
    }
}