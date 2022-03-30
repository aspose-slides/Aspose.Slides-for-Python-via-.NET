using System
using System.Diagnostics
import aspose.pydrawing as drawing
using Aspose.slides.Export
using Aspose.slides.Charts
import aspose.slides as slides
using CSharp.Tables


namespace Aspose.slides.Examples.CSharp.text
{
    class PortionGetRect
    {
        public static void Run()
        {
            outPath = RunExamples.OutPath

            with slides.Presentation() as pres:
            {
                # Create table
                ITable tbl = pres.slides[0].shapes.AddTable(50, 50, new double[] { 50, 70 }, new double[] { 50, 50, 50 })

                # Create paragraths
                paragraph0 = new Paragraph()
                paragraph0.portions.add(new Portion("Text "))
                paragraph0.portions.add(new Portion("in0"))
                paragraph0.portions.add(new Portion(" Cell"))

                paragraph1 = new Paragraph()
                paragraph1.text = "On0"

                paragraph2 = new Paragraph()
                paragraph2.portions.add(new Portion("Hi there "))
                paragraph2.portions.add(new Portion("col0"))

                ICell cell = tbl.Rows[1][1]

                # Add text into the table cell
                cell.text_frame.Paragraphs.clear()
                cell.text_frame.Paragraphs.add(paragraph0)
                cell.text_frame.Paragraphs.add(paragraph1)
                cell.text_frame.Paragraphs.add(paragraph2)

                # Add TextFrame
                autoShape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 400, 100, 60, 120)
                autoShape.text_frame.text = "Text in shape"
                autoShape.text_frame.paragraphs[0].ParagraphFormat.Alignment = TextAlignment.Left

                # Getting coordinates of the left top corner of the table cell.
                x = tbl.x + cell.OffsetX
                y = tbl.y + cell.OffsetY

                # Using IParagrap.get_rect() and IPortion.get_rect() methods in order to add frame to portions and paragraphs.
                foreach (para in cell.text_frame.Paragraphs)
                {
                    if (para.text == "")
                        continue

                    RectangleF rect = para.get_rect()
                    shape =
                        pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle,
                            rect.x + (float)x, rect.y + (float)y, rect.width, rect.height)

                    shape.fill_format.fill_type = slides.FillType.NO_FILL
                    shape.line_format.fill_format.solid_fill_color.color = drawing.Color.yellow
                    shape.line_format.fill_format.fill_type = slides.FillType.SOLID


                    foreach (portion in para.portions)
                    {
                        if (portion.text.Contains("0"))
                        {
                            rect = portion.get_rect()
                            shape =
                                pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle,
                                    rect.x + (float)x, rect.y + (float)y, rect.width, rect.height)

                            shape.fill_format.fill_type = slides.FillType.NO_FILL
                        }
                    }
                }

                # Add frame to AutoShape paragraphs.
                foreach (para in autoShape.text_frame.Paragraphs)
                {
                    RectangleF rect = para.get_rect()
                    shape =
                        pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle,
                            rect.x + autoShape.x, rect.y + autoShape.y, rect.width, rect.height)

                    shape.fill_format.fill_type = slides.FillType.NO_FILL
                    shape.line_format.fill_format.solid_fill_color.color = drawing.Color.yellow
                    shape.line_format.fill_format.fill_type = slides.FillType.SOLID

                }

                pres.save(outPath + "GetRect_Out.pptx", slides.export.SaveFormat.PPTX)
                Process.Start(outPath + "GetRect_Out.pptx")
            }
        }
    }
}
