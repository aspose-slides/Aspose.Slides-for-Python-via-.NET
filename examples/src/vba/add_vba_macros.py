import aspose.slides as slides


def add_vba_macros(global_opts):
    # Instantiate Presentation
    with slides.Presentation() as presentation:
        # Create new VBA Project
        presentation.vba_project = slides.vba.VbaProject()

        # Add empty module to the VBA project
        module = presentation.vba_project.modules.add_empty_module("Module")
    
        # Set module source code
        module.source_code = 'Sub Test(oShape As Shape) MsgBox "Test" End Sub'

        # Create reference to <stdole>
        stdole_reference = slides.vba.VbaReferenceOleTypeLib("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation")

        # Create reference to Office
        office_reference = slides.vba.VbaReferenceOleTypeLib("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library")

        # Add references to the VBA project
        presentation.vba_project.references.add(stdole_reference)
        presentation.vba_project.references.add(office_reference)

        # Save Presentation
        presentation.save(global_opts.out_dir + "vba_AddVBAMacros_out.pptm", slides.export.SaveFormat.PPTM)
