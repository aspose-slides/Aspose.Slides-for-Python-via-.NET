using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
This example demonstrates how to use the spreadsheet options for a chart formulas.
*/
namespace CSharp.Charts
{
    class SpreadsheetFormulasOptions
    {
        public static void Run()
        {
            loadOptions = slides.LoadOptions()

            # Set preferred culture information for calculating some functions intended for use with languages 
            # that use the double-byte character set (DBCS).
            loadOptions.spreadsheet_options.PreferredCulture = new System.Globalization.CultureInfo("ja-JP")

            using (Presentation presentation = new Presentation(loadOptions))
            {
                chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 150, 150, 500, 300)
                workbook = chart.chart_data.chart_data_workbook

                cell = workbook.get_cell(0, "B2")
                
                # Use the Formula property of the IChartDataCell interface to write a formula in a cell.
                cell.formula = "FINDB(\"ス\", \"テキスト\")"
                workbook.calculate_formulas()

                #Check calculation.
                if (Int32.Parse(cell.value.ToString()) == 5)
                {
                    print("Calculated value = 5.")
                }
                else
                {
                    print("Wrong calculation!")
                }
            }
        }
    }
}
