import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.SmartArt
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.SmartArts
{
	class CustomChildNodesInSmartArt
	{
		public static void Run()
		{
			#ExStart:CustomChildNodesInSmartArt
			dataDir = RunExamples.GetDataDir_SmartArts()

			# Load the desired the presentation
			Presentation pres = new Presentation(dataDir + "AccessChildNodes.pptx")

			{
				ISmartArt smart = pres.slides[0].shapes.AddSmartArt(20, 20, 600, 500, SmartArtLayoutType.OrganizationChart)

				# Move SmartArt shape to new position
				ISmartArtNode node = smart.AllNodes[1]
				ISmartArtShape shape = node.shapes[1]
				shape.x += (shape.width * 2)
				shape.y -= (shape.height / 2)

				# Change SmartArt shape's widths
				node = smart.AllNodes[2]
				shape = node.shapes[1]
				shape.width += (shape.width / 2)

				# Change SmartArt shape's height
				node = smart.AllNodes[3]
				shape = node.shapes[1]
				shape.height += (shape.height / 2)

				# Change SmartArt shape's rotation
				node = smart.AllNodes[4]
				shape = node.shapes[1]
				shape.rotation = 90

				pres.save(dataDir + "SmartArt.pptx", slides.export.SaveFormat.PPTX)
			}
			#ExEnd:CustomChildNodesInSmartArt
		}
	}
}