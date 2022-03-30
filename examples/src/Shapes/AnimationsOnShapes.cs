using System.IO

import aspose.slides as slides
using Aspose.slides.Export
using Aspose.slides.Animation
import aspose.pydrawing as drawing

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AnimationsOnShapes
    {
        public static void Run()
        {
            #ExStart:AnimationsOnShapes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PrseetationEx class that represents the PPTX
            with slides.Presentation() as pres:
            {
                sld = pres.slides[0]

                # Now create effect "PathFootball" for existing shape from scratch.
                ashp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 150, 150, 250, 25)

                ashp.AddTextFrame("Animated TextBox")

                # Add PathFootBall animation effect
                pres.slides[0].timeline.main_sequence.add_effect(ashp, slides.animation.EffectType.PathFootball,
                                       slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

                # Create some kind of "button".
                IShape shapeTrigger = pres.slides[0].shapes.add_auto_shape(ShapeType.Bevel, 10, 10, 20, 20)

                # Create sequence of effects for this button.
                ISequence seqInter = pres.slides[0].timeline.InteractiveSequences.add(shapeTrigger)

                # Create custom user path. Our object will be moved only after "button" click.
                IEffect fxUserPath = seqInter.add_effect(ashp, slides.animation.EffectType.PathUser, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.OnClick)

                # Created path is empty so we should add commands for moving.
                IMotionEffect motionBhv = ((IMotionEffect)fxUserPath.Behaviors[0])

                PointF[] pts = new PointF[1]
                pts[0] = new PointF(0.076f, 0.59f)
                motionBhv.Path.add(MotionCommandPathType.LineTo, pts, MotionPathPointsType.Auto, True)
                pts[0] = new PointF(-0.076f, -0.59f)
                motionBhv.Path.add(MotionCommandPathType.LineTo, pts, MotionPathPointsType.Auto, False)
                motionBhv.Path.add(MotionCommandPathType.End, None, MotionPathPointsType.Auto, False)

                #Write the presentation as PPTX to disk
                pres.save(dataDir + "AnimExample_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AnimationsOnShapes
        }
    }
}