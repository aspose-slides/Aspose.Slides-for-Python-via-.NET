﻿import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class GetEffectiveValuesOfTable
    {
        public static void Run() {

            #ExStart:GetEffectiveValuesOfTable

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            using (Presentation pres = new Presentation(dataDir + "pres.pptx"))
            {
                ITable tbl = pres.slides[0].shapes[0] as ITable
                ITableFormatEffectiveData tableFormatEffective = tbl.TableFormat.GetEffective()
                IRowFormatEffectiveData rowFormatEffective = tbl.Rows[0].RowFormat.GetEffective()
                IColumnFormatEffectiveData columnFormatEffective = tbl.Columns[0].ColumnFormat.GetEffective()
                ICellFormatEffectiveData cellFormatEffective = tbl[0, 0].CellFormat.GetEffective()

                IFillFormatEffectiveData tableFillFormatEffective = tableFormatEffective.FillFormat
                IFillFormatEffectiveData rowFillFormatEffective = rowFormatEffective.FillFormat
                IFillFormatEffectiveData columnFillFormatEffective = columnFormatEffective.FillFormat
                IFillFormatEffectiveData cellFillFormatEffective = cellFormatEffective.FillFormat
               
            }
            #ExEnd:GetEffectiveValuesOfTable

        }
    }
}
