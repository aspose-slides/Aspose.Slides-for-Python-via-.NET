using System
using System.Collections.Generic
using System.Data
import aspose.pydrawing as drawing
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using DataTable = System.Data.DataTable

namespace CSharp.Presentations.Conversion
{
    # This example demonstrates creating 3D shape and appliing 3D effects to the text in it.

    public class WordArt
    {
        public static void Run()
        {
            resultPath = Path.Combine(RunExamples.OutPath, "WordArt_out.pptx")

            with slides.Presentation() as pres:
            {
                # Create shape and text frame
                shape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 314, 122, 400, 215.433f)

                ITextFrame textFrame = shape.text_frame

                Portion portion = (Portion)textFrame.paragraphs[0].portions[0]
                portion.text = "Aspose.Slides"
                FontData fontData = slides.FontData("Arial Black")
                portion.portion_format.latin_font = fontData
                portion.portion_format.font_height = 36

                # Set format of the text
                portion.portion_format.fill_format.fill_type = FillType.Pattern
                portion.portion_format.FillFormat.PatternFormat.ForeColor.color = Color.DarkOrange
                portion.portion_format.FillFormat.PatternFormat.BackColor.color = Color.white
                portion.portion_format.FillFormat.PatternFormat.PatternStyle = PatternStyle.SmallGrid

                portion.portion_format.line_format.fill_format.fill_type = slides.FillType.SOLID
                portion.portion_format.line_format.fill_format.solid_fill_color.color = Color.Black

                # Add a shadow effect for the text
                portion.portion_format.EffectFormat.EnableOuterShadowEffect()
                portion.portion_format.EffectFormat.OuterShadowEffect.ShadowColor.color = Color.Black
                portion.portion_format.EffectFormat.OuterShadowEffect.ScaleHorizontal = 100
                portion.portion_format.EffectFormat.OuterShadowEffect.ScaleVertical = 65
                portion.portion_format.EffectFormat.OuterShadowEffect.BlurRadius = 4.73
                portion.portion_format.EffectFormat.OuterShadowEffect.Direction = 230
                portion.portion_format.EffectFormat.OuterShadowEffect.Distance = 2
                portion.portion_format.EffectFormat.OuterShadowEffect.SkewHorizontal = 30
                portion.portion_format.EffectFormat.OuterShadowEffect.SkewVertical = 0
                portion.portion_format.EffectFormat.OuterShadowEffect.ShadowColor.ColorTransform.add(ColorTransformOperation.SetAlpha, 0.32f)

                # Add reflection
                portion.portion_format.EffectFormat.EnableReflectionEffect()
                portion.portion_format.EffectFormat.ReflectionEffect.BlurRadius = 0.5
                portion.portion_format.EffectFormat.ReflectionEffect.Distance = 4.72
                portion.portion_format.EffectFormat.ReflectionEffect.StartPosAlpha = 0f
                portion.portion_format.EffectFormat.ReflectionEffect.EndPosAlpha = 60f
                portion.portion_format.EffectFormat.ReflectionEffect.Direction = 90
                portion.portion_format.EffectFormat.ReflectionEffect.ScaleHorizontal = 100
                portion.portion_format.EffectFormat.ReflectionEffect.ScaleVertical = -100
                portion.portion_format.EffectFormat.ReflectionEffect.StartReflectionOpacity = 60f
                portion.portion_format.EffectFormat.ReflectionEffect.EndReflectionOpacity = 0.9f
                portion.portion_format.EffectFormat.ReflectionEffect.RectangleAlign = RectangleAlignment.BottomLeft

                # Add glow effect
                portion.portion_format.EffectFormat.EnableGlowEffect()
                portion.portion_format.EffectFormat.GlowEffect.Color.R = 255
                portion.portion_format.EffectFormat.GlowEffect.Color.ColorTransform.add(ColorTransformOperation.SetAlpha, 0.54f)
                portion.portion_format.EffectFormat.GlowEffect.Radius = 7

                # Add transformation
                textFrame.TextFrameFormat.Transform = TextShapeType.ArchUpPour

                # Add 3D effects to the shape
                shape.ThreeDFormat.BevelBottom.BevelType = BevelPresetType.Circle
                shape.ThreeDFormat.BevelBottom.height = 10.5
                shape.ThreeDFormat.BevelBottom.width = 10.5

                shape.ThreeDFormat.BevelTop.BevelType = BevelPresetType.Circle
                shape.ThreeDFormat.BevelTop.height = 12.5
                shape.ThreeDFormat.BevelTop.width = 11

                shape.ThreeDFormat.ExtrusionColor.color = drawing.Color.orange
                shape.ThreeDFormat.ExtrusionHeight = 6

                shape.ThreeDFormat.ContourColor.color = drawing.Color.dark_red
                shape.ThreeDFormat.ContourWidth = 1.5

                shape.ThreeDFormat.Depth = 3

                shape.ThreeDFormat.Material = MaterialPresetType.Plastic

                shape.ThreeDFormat.LightRig.Direction = LightingDirection.Top
                shape.ThreeDFormat.LightRig.LightType = LightRigPresetType.Balanced
                shape.ThreeDFormat.LightRig.SetRotation(0, 0, 40)

                shape.ThreeDFormat.Camera.CameraType = CameraPresetType.PerspectiveContrastingRightFacing

                # Add 3D effects to the text
                textFrame = shape.text_frame

                textFrame.TextFrameFormat.ThreeDFormat.BevelBottom.BevelType = BevelPresetType.Circle
                textFrame.TextFrameFormat.ThreeDFormat.BevelBottom.height = 3.5
                textFrame.TextFrameFormat.ThreeDFormat.BevelBottom.width = 3.5

                textFrame.TextFrameFormat.ThreeDFormat.BevelTop.BevelType = BevelPresetType.Circle
                textFrame.TextFrameFormat.ThreeDFormat.BevelTop.height = 12.5
                textFrame.TextFrameFormat.ThreeDFormat.BevelTop.width = 11

                textFrame.TextFrameFormat.ThreeDFormat.ExtrusionColor.color = drawing.Color.orange
                textFrame.TextFrameFormat.ThreeDFormat.ExtrusionHeight = 6

                textFrame.TextFrameFormat.ThreeDFormat.ContourColor.color = drawing.Color.dark_red
                textFrame.TextFrameFormat.ThreeDFormat.ContourWidth = 1.5

                textFrame.TextFrameFormat.ThreeDFormat.Depth = 3

                textFrame.TextFrameFormat.ThreeDFormat.Material = MaterialPresetType.Plastic

                textFrame.TextFrameFormat.ThreeDFormat.LightRig.Direction = LightingDirection.Top
                textFrame.TextFrameFormat.ThreeDFormat.LightRig.LightType = LightRigPresetType.Balanced
                textFrame.TextFrameFormat.ThreeDFormat.LightRig.SetRotation(0, 0, 40)

                textFrame.TextFrameFormat.ThreeDFormat.Camera.CameraType = CameraPresetType.PerspectiveContrastingRightFacing

                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
