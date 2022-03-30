import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Transitions
{
    class SupportOfMorphTransition
    {
        public static void Run()
        {
            #ExStart:SupportOfMorphTransition
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            with slides.Presentation() as presentation:
            {
                AutoShape autoshape = (AutoShape)presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 400, 100)
                autoshape.text_frame.text = "Test text"

                presentation.slides.AddClone(presentation.slides[0])

                presentation.slides[1].shapes[0].x += 100
                presentation.slides[1].shapes[0].y += 50
                presentation.slides[1].shapes[0].width -= 200
                presentation.slides[1].shapes[0].height -= 10

                presentation.slides[1].SlideShowTransition.type = Aspose.slides.SlideShow.TransitionType.Morph

                presentation.save(dataDir+"presentation-out.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SupportOfMorphTransition
        }
    }
}
