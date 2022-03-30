using System.Collections.Generic
using System.IO
using System.text
using Aspose.slides.Export
using Aspose.slides.Export.Xaml

/*
This example demonstrates how to export a Presentation to a set of XAML files.
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    public class ConvertToXaml
    {
        public static void Run()
        {
            # Path to source presentation
            presentationFileName = Path.Combine(RunExamples.GetDataDir_Conversion(), "XamlEtalon.pptx")

            using (Presentation pres = new Presentation(presentationFileName))
            {
                # Create convertion options
                XamlOptions xamlOptions = new XamlOptions()
                xamlOptions.ExportHiddenSlides = True

                # Define your own output-saving service
                NewXamlSaver newXamlSaver = new NewXamlSaver()
                xamlOptions.OutputSaver = newXamlSaver

                # Convert slides
                pres.save(xamlOptions)

                # Save XAML files to an output directory
                foreach (pair in newXamlSaver.Results)
                {
                    File.AppendAllText(Path.Combine(RunExamples.OutPath, pair.Key), pair.value)
                }
            }
        }

        #/ <summary>
        #/ Represents an output saver implementation for transfer data to the external storage.
        #/ </summary>
        class NewXamlSaver : IXamlOutputSaver
        {
            private Dictionary<string, string> m_result =  new Dictionary<string, string>()
            
            public Dictionary<string, string> Results
            {
                get { return m_result }
            }

            public void Save(path, byte[] data)
            {
                name = Path.GetFileName(path)
                Results[name] = Encoding.UTF8.GetString(data)
            }
        }
    }
}