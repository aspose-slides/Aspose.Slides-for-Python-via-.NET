import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.CRUD
{
    class CloneSlideIntoSpecifiedSection
    {
        public static void Run() {

            #ExStart:CloneSlideIntoSpecifiedSection

            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            using (IPresentation presentation = new Presentation()) {

                presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 200, 50, 300, 100)
                presentation.Sections.AddSection("Section 1", presentation.slides[0])

                ISection section2 = presentation.Sections.AppendEmptySection("Section 2")

                presentation.slides.AddClone(presentation.slides[0], section2)


                presentation.save(dataDir + "CloneSlideIntoSpecifiedSection.pptx",slides.export.SaveFormat.PPTX)
            }
            #ExEnd:CloneSlideIntoSpecifiedSection

        }


    }
}
