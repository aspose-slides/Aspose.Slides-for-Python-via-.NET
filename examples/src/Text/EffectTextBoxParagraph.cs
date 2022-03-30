import aspose.slides as slides
using Aspose.slides.Animation
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
	class EffectTextBoxParagraph
	{
		public static void Run()
		{
			#ExStart:EffectTextBoxParagraph
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir + "Test.pptx"))
			{
				ISequence sequence = pres.slides[0].timeline.main_sequence
				autoShape = (IAutoShape)pres.slides[0].shapes[1]

				foreach (IParagraph paragraph in autoShape.text_frame.Paragraphs)
				{
					IEffect[] effects = sequence.GetEffectsByParagraph(paragraph)

					if (effects.Length > 0)
						print("Paragraph \"" + paragraph.text + "\" has " + effects[0].type + " effect.")
				}
			}
			#ExEnd:EffectTextBoxParagraph
		}
		}
}
