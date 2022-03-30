import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class SetCustomBulletsNumber
    {
        public static void Run() {

            #ExStart:SetCustomBulletsNumber

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            using (presentation = new Presentation())
            {
                shape = presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 200, 200, 400, 200)

                # Accessing the text frame of created autoshape
                ITextFrame textFrame = shape.text_frame

                # Removing the default exisiting paragraph
                textFrame.Paragraphs.remove_at(0)

                # First list
                paragraph1 = new Paragraph { Text = "bullet 2" }
                paragraph1.ParagraphFormat.Depth = 4 
                paragraph1.ParagraphFormat.Bullet.NumberedBulletStartWith = 2
                paragraph1.ParagraphFormat.Bullet.type = BulletType.Numbered
                textFrame.Paragraphs.add(paragraph1)

                paragraph2 = new Paragraph { Text = "bullet 3" }
                paragraph2.ParagraphFormat.Depth = 4
                paragraph2.ParagraphFormat.Bullet.NumberedBulletStartWith = 3 
                paragraph2.ParagraphFormat.Bullet.type = BulletType.Numbered  
                textFrame.Paragraphs.add(paragraph2)

                
                paragraph5 = new Paragraph { Text = "bullet 7" }
                paragraph5.ParagraphFormat.Depth = 4
                paragraph5.ParagraphFormat.Bullet.NumberedBulletStartWith = 7
                paragraph5.ParagraphFormat.Bullet.type = BulletType.Numbered
                textFrame.Paragraphs.add(paragraph5)

                presentation.save(dataDir + "SetCustomBulletsNumber-slides.pptx", slides.export.SaveFormat.PPTX)
            }


            #ExEnd:SetCustomBulletsNumber

        }
    }
}
