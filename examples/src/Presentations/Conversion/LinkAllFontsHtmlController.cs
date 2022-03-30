import aspose.slides as slides
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace Aspose.slides.Examples.CSharp.Conversion
{
    #ExStart:LinkAllFontsHtmlController
    class LinkAllFontsHtmlController : EmbedAllFontsHtmlController
    {
        private readonly m_basePath

        public LinkAllFontsHtmlController(string[] fontNameExcludeList, basePath)
            : base(fontNameExcludeList)
        {
            m_basePath = basePath
        }

        public override void WriteFont(
            IHtmlGenerator generator,
            IFontData originalFont,
            IFontData substitutedFont,
            fontStyle,
            fontWeight,
            byte[] fontData)
        {
            fontName = substitutedFont == None ? originalFont.FontName : substitutedFont.FontName
            path = string.format("{0}.woff", fontName) # some path sanitaze may be needed
            File.WriteAllBytes(Path.Combine(m_basePath, path), fontData)

            generator.AddHtml("<style>")
            generator.AddHtml("@font-face { ")
            generator.AddHtml(string.format("font-family: '{0}' ", fontName))
            generator.AddHtml(string.format("src: url('{0}')", path))

            generator.AddHtml(" }")
            generator.AddHtml("</style>")
        }
    
    }
  #  ExEnd:LinkAllFontsHtmlController
}
