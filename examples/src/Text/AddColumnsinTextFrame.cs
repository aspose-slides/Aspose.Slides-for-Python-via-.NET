import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Microsoft.VisualStudio.TestTools.UnitTesting
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class AddColumnsinTextFrame
    {
        public static void Run()
        {

            #ExStart:AddColumnsinTextFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            outPptxFileName = dataDir + "ColumnsTest.pptx"
            with slides.Presentation() as pres:
            {
                shape1 = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 300, 300)
                TextFrameFormat format = (TextFrameFormat)shape1.text_frame.TextFrameFormat

                format.ColumnCount = 2
                shape1.text_frame.text = "All these columns are limited to be within a single text container -- " +
                                          "you can add or delete text and the new or remaining text automatically adjusts " +
                                          "itself to flow within the container. You cannot have text flow from one container " +
                                          "to other though -- we told you PowerPoint's column options for text are limited!"
                pres.save(outPptxFileName, slides.export.SaveFormat.PPTX)

                using (Presentation test = new Presentation(outPptxFileName))
                {
                    Assert.AreEqual(2, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnCount)
                    Assert.AreEqual(double.NaN, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnSpacing)
                }

                format.ColumnSpacing = 20
                pres.save(outPptxFileName, slides.export.SaveFormat.PPTX)

                using (Presentation test = new Presentation(outPptxFileName))
                {
                    Assert.AreEqual(2, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnCount)
                    Assert.AreEqual(20, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnSpacing)
                }

                format.ColumnCount = 3
                format.ColumnSpacing = 15
                pres.save(outPptxFileName, slides.export.SaveFormat.PPTX)

                using (Presentation test = new Presentation(outPptxFileName))
                {
                    Assert.AreEqual(3, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnCount)
                    Assert.AreEqual(15, ((AutoShape)test.slides[0].shapes[0]).text_frame.TextFrameFormat.ColumnSpacing)
                }

            }

            #ExEnd:AddColumnsinTextFrame
        }
    }
}
