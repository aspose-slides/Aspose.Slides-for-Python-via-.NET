using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class MultipleParagraphs
    {
        public static void Run()
        {
            #ExStart:MultipleParagraphs
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate a Presentation class that represents a PPTX file
            with slides.Presentation() as pres:
            {
                # Accessing first slide
                slide = pres.slides[0]

                # Add an AutoShape of Rectangle type
                ashp = slide.shapes.add_auto_shape(ShapeType.Rectangle, 50, 150, 300, 150)

                # Access TextFrame of the AutoShape
                ITextFrame tf = ashp.text_frame

                # Create Paragraphs and Portions with different text formats
                IParagraph para0 = tf.paragraphs[0]
                port01 = new Portion()
                port02 = new Portion()
                para0.portions.add(port01)
                para0.portions.add(port02)

                IParagraph para1 = new Paragraph()
                tf.Paragraphs.add(para1)
                port10 = new Portion()
                port11 = new Portion()
                port12 = new Portion()
                para1.portions.add(port10)
                para1.portions.add(port11)
                para1.portions.add(port12)

                IParagraph para2 = new Paragraph()
                tf.Paragraphs.add(para2)
                port20 = new Portion()
                port21 = new Portion()
                port22 = new Portion()
                para2.portions.add(port20)
                para2.portions.add(port21)
                para2.portions.add(port22)

                for (i = 0 i < 3 i++)
                    for (j = 0 j < 3 j++)
                    {
                        tf.paragraphs[i].portions[j].text = "Portion0" + j.ToString()
                        if (j == 0)
                        {
                            tf.paragraphs[i].portions[j].portion_format.fill_format.fill_type = slides.FillType.SOLID
                            tf.paragraphs[i].portions[j].portion_format.fill_format.solid_fill_color.color = drawing.Color.red
                            tf.paragraphs[i].portions[j].portion_format.font_bold = 1
                            tf.paragraphs[i].portions[j].portion_format.font_height = 15
                        }
                        else if (j == 1)
                        {
                            tf.paragraphs[i].portions[j].portion_format.fill_format.fill_type = slides.FillType.SOLID
                            tf.paragraphs[i].portions[j].portion_format.fill_format.solid_fill_color.color = drawing.Color.blue
                            tf.paragraphs[i].portions[j].portion_format.font_italic = 1
                            tf.paragraphs[i].portions[j].portion_format.font_height = 18
                        }
                    }

                #Write PPTX to Disk
                pres.save(dataDir + "multiParaPort_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:MultipleParagraphs
        }
    }
}