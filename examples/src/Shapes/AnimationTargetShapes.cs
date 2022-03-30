using System
using System.IO
import aspose.slides as slides
using Aspose.slides.Animation
using Aspose.slides.DOM.Ole
using Aspose.slides.Export

/*
This sample demonstrates the output of information for all animated shapes in the main sequence for all slides in a presentation.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AnimationTargetShapes
    {
        public static void Run()
        {
            # Path to source presentation
            presentationFileName = Path.Combine(RunExamples.GetDataDir_Shapes(), "AnimationShapesExample.pptx")

            using (Presentation pres = new Presentation(presentationFileName))
            {
                foreach (slide in pres.Slides)
                {
                    foreach (IEffect effect in slide.timeline.main_sequence)
                    {
                        print(effect.type + " animation effect is set to shape#" +
                                          effect.TargetShape.UniqueId +
                                          " on slide#" + slide.SlideNumber)
                    }
                }
            }
        }
    }
}