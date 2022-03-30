using System.IO
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{

    # Code below shows how to use ISvgShapeAndTextFormattingController interface for
    # tspan Id attribute manipulation.

    public class SvgFormattingController
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Conversion()
            pptxFileName = Path.Combine(dataDir, "Convert_Svg_Custom.pptx")
            outSvgFileName = Path.Combine(RunExamples.OutPath, "Convert_Svg_Custom.svg")

            using (Presentation pres = new Presentation(pptxFileName))
            {
                using (FileStream stream = new FileStream(outSvgFileName, FileMode.Create))
                {
                    SVGOptions svgOptions = new SVGOptions
                    {
                        ShapeFormattingController = new MySvgShapeFormattingController()
                    }

                    pres.slides[0].WriteAsSvg(stream, svgOptions)
                }
            }
        }
    }

    class MySvgShapeFormattingController : ISvgShapeAndTextFormattingController
    {
        private m_shapeIndex, m_portionIndex, m_tspanIndex

        public MySvgShapeFormattingController(shapeStartIndex = 0)
        {
            m_shapeIndex = shapeStartIndex
            m_portionIndex = 0
        }

        public void FormatShape(Aspose.slides.Export.ISvgShape svgShape, IShape shape)
        {
            svgShape.Id = string.format("shape-{0}", m_shapeIndex++)
            m_portionIndex = m_tspanIndex = 0
        }

        public void FormatText(Aspose.slides.Export.ISvgTSpan svgTSpan, portion, ITextFrame textFrame)
        {
            paragraphIndex = 0 portionIndex = 0
            for (i = 0 i < textFrame.Paragraphs.Count i = i + 1)
            {
                portionIndex = textFrame.paragraphs[i].portions.IndexOf(portion)
                if (portionIndex > -1) { paragraphIndex = i break }
            }
            if (m_portionIndex != portionIndex)
            {
                m_tspanIndex = 0
                m_portionIndex = portionIndex
            }
            svgTSpan.Id = string.format("paragraph-{0}_portion-{1}_{2}", paragraphIndex, m_portionIndex, m_tspanIndex++)
        }

        public ISvgShapeFormattingController AsISvgShapeFormattingController
        {
            get { return this }
        }
    }
}