using System.IO

import aspose.slides as slides
using System
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class MutilevelBullets
    {
        public static void Run()
        {
            #ExStart:MutilevelBullets
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
                ITextFrame text = aShp.AddTextFrame("")
                
                #clearing default paragraph
                text.Paragraphs.clear()

                #Adding first paragraph
                para1 = new Paragraph()
                para1.text = "Content"
                para1.ParagraphFormat.Bullet.type = BulletType.Symbol
                para1.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
                para1.ParagraphFormat.DefaultPortionFormat.fill_format.fill_type = slides.FillType.SOLID
                para1.ParagraphFormat.DefaultPortionFormat.fill_format.solid_fill_color.color = Color.Black
                #Setting bullet level
                para1.ParagraphFormat.Depth = 0

                #Adding second paragraph
                para2 = new Paragraph()
                para2.text = "Second Level"
                para2.ParagraphFormat.Bullet.type = BulletType.Symbol
                para2.ParagraphFormat.Bullet.Char = '-'
                para2.ParagraphFormat.DefaultPortionFormat.fill_format.fill_type = slides.FillType.SOLID
                para2.ParagraphFormat.DefaultPortionFormat.fill_format.solid_fill_color.color = Color.Black
                #Setting bullet level
                para2.ParagraphFormat.Depth = 1

                #Adding third paragraph
                para3 = new Paragraph()
                para3.text = "Third Level"
                para3.ParagraphFormat.Bullet.type = BulletType.Symbol
                para3.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
                para3.ParagraphFormat.DefaultPortionFormat.fill_format.fill_type = slides.FillType.SOLID
                para3.ParagraphFormat.DefaultPortionFormat.fill_format.solid_fill_color.color = Color.Black
                #Setting bullet level
                para3.ParagraphFormat.Depth = 2

                #Adding fourth paragraph
                para4 = new Paragraph()
                para4.text = "Fourth Level"
                para4.ParagraphFormat.Bullet.type = BulletType.Symbol
                para4.ParagraphFormat.Bullet.Char = '-'
                para4.ParagraphFormat.DefaultPortionFormat.fill_format.fill_type = slides.FillType.SOLID
                para4.ParagraphFormat.DefaultPortionFormat.fill_format.solid_fill_color.color = Color.Black
                #Setting bullet level
                para4.ParagraphFormat.Depth = 3

                #Adding paragraphs to collection
                text.Paragraphs.add(para1)
                text.Paragraphs.add(para2)
                text.Paragraphs.add(para3)
                text.Paragraphs.add(para4)

                #Writing the presentation as a PPTX file
                pres.save(dataDir + "MultilevelBullet.pptx", slides.export.SaveFormat.PPTX)

            
            }
            #ExEnd:MutilevelBullets
        }
    }
}