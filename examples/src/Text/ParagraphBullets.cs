using System.IO

import aspose.slides as slides
using System
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class ParagraphBullets
    {
        public static void Run()
        {
            #ExStart:ParagraphBullets
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Creating a presenation instance
            with slides.Presentation() as pres:
            {

                # Accessing the first slide
                slide = pres.slides[0]


                # Adding and accessing Autoshape
                aShp = slide.shapes.add_auto_shape(ShapeType.Rectangle, 200, 200, 400, 200)

                # Accessing the text frame of created autoshape
                ITextFrame txtFrm = aShp.text_frame

                # Removing the default exisiting paragraph
                txtFrm.Paragraphs.remove_at(0)

                # Creating a paragraph
                Paragraph para = new Paragraph()

                # Setting paragraph bullet style and symbol
                para.ParagraphFormat.Bullet.type = BulletType.Symbol
                para.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)

                # Setting paragraph text
                para.text = "Welcome to Aspose.Slides"

                # Setting bullet indent
                para.ParagraphFormat.Indent = 25

                # Setting bullet color
                para.ParagraphFormat.Bullet.Color.ColorType = ColorType.RGB
                para.ParagraphFormat.Bullet.Color.color = Color.Black
                para.ParagraphFormat.Bullet.IsBulletHardColor = 1 # set IsBulletHardColor to True to use own bullet color

                # Setting Bullet Height
                para.ParagraphFormat.Bullet.height = 100

                # Adding Paragraph to text frame
                txtFrm.Paragraphs.add(para)

                # Creating second paragraph
                Paragraph para2 = new Paragraph()

                # Setting paragraph bullet type and style
                para2.ParagraphFormat.Bullet.type = BulletType.Numbered
                para2.ParagraphFormat.Bullet.NumberedBulletStyle = NumberedBulletStyle.BulletCircleNumWDBlackPlain

                # Adding paragraph text
                para2.text = "This is numbered bullet"

                # Setting bullet indent
                para2.ParagraphFormat.Indent = 25

                para2.ParagraphFormat.Bullet.Color.ColorType = ColorType.RGB
                para2.ParagraphFormat.Bullet.Color.color = Color.Black
                para2.ParagraphFormat.Bullet.IsBulletHardColor = 1 # set IsBulletHardColor to True to use own bullet color

                # Setting Bullet Height
                para2.ParagraphFormat.Bullet.height = 100

                # Adding Paragraph to text frame
                txtFrm.Paragraphs.add(para2)


                #Writing the presentation as a PPTX file
                pres.save(dataDir + "Bullet_out.pptx", slides.export.SaveFormat.PPTX)

            }
            #ExEnd:ParagraphBullets
        }
    }
}