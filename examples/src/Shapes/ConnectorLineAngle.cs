using System.IO
import aspose.slides as slides
using System

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class ConnectorLineAngle
    {
        #ExStart:ConnectorLineAngle
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            Presentation pres = new Presentation(dataDir + "ConnectorLineAngle.pptx")
            Slide slide = (Slide)pres.slides[0]
            Shape shape
            for (i = 0 i < slide.shapes.Count i++)
            {
                double dir = 0.0
                shape = (Shape)slide.shapes[i]
                if (shape is AutoShape)
                {
                    AutoShape ashp = (AutoShape)shape
                    if (ashp.ShapeType == slides.ShapeType.LINE)
                    {
                        dir = getDirection(ashp.width, ashp.height, Convert.ToBoolean(ashp.frame.flip_h), Convert.ToBoolean(ashp.frame.flip_v))
                    }
                }
                else if (shape is Connector)
                {
                    Connector ashp = (Connector)shape
                    dir = getDirection(ashp.width, ashp.height, Convert.ToBoolean(ashp.frame.flip_h), Convert.ToBoolean(ashp.frame.flip_v))
                }

                print(dir)
            }

        }
        public static double getDirection(float w, float h, bool flipH, bool flipV)
        {
            float endLineX = w * (flipH ? -1 : 1)
            float endLineY = h * (flipV ? -1 : 1)
            float endYAxisX = 0
            float endYAxisY = h
            double angle = (Math.Atan2(endYAxisY, endYAxisX) - Math.Atan2(endLineY, endLineX))
            if (angle < 0) angle += 2 * Math.PI
            return angle * 180.0 / Math.PI
        }
        #ExEnd:ConnectorLineAngle
    }

}