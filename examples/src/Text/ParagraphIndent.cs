using System.IO

import aspose.slides as slides
using System
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class ParagraphIndent
    {
        public static void Run()
        {
            #ExStart:ParagraphIndent

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Presentation Class
            with slides.Presentation() as pres:

            # Get first slide
            sld = pres.slides[0]

            # Add a Rectangle Shape
            rect = sld.shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 500, 150)

            # Add TextFrame to the Rectangle
            ITextFrame tf = rect.AddTextFrame("This is first line \rThis is second line \rThis is third line")

            # Set the text to fit the shape
            tf.TextFrameFormat.autofit_type = TextAutofitType.Shape

            # Hide the lines of the Rectangle
            rect.line_format.fill_format.fill_type = slides.FillType.SOLID

            # Get first Paragraph in the TextFrame and set its Indent
            IParagraph para1 = tf.paragraphs[0]
            # Setting paragraph bullet style and symbol
            para1.ParagraphFormat.Bullet.type = BulletType.Symbol
            para1.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
            para1.ParagraphFormat.Alignment = TextAlignment.Left

            para1.ParagraphFormat.Depth = 2
            para1.ParagraphFormat.Indent = 30

            # Get second Paragraph in the TextFrame and set its Indent
            IParagraph para2 = tf.paragraphs[1]
            para2.ParagraphFormat.Bullet.type = BulletType.Symbol
            para2.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
            para2.ParagraphFormat.Alignment = TextAlignment.Left
            para2.ParagraphFormat.Depth = 2
            para2.ParagraphFormat.Indent = 40

            # Get third Paragraph in the TextFrame and set its Indent
            IParagraph para3 = tf.paragraphs[2]
            para3.ParagraphFormat.Bullet.type = BulletType.Symbol
            para3.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
            para3.ParagraphFormat.Alignment = TextAlignment.Left
            para3.ParagraphFormat.Depth = 2
            para3.ParagraphFormat.Indent = 50

            #Write the Presentation to disk
            pres.save(dataDir + "InOutDent_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ParagraphIndent            
        }
    }
}