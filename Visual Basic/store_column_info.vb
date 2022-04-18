'Written by: Matt Scanlon
'Written on: 2022-04-15 8:30 AM
'Last updated by: Matt Scanlon
'Last Updated: 2022-04-15 8:30 AM

'PURPOSE:
'To dynamically create a stored dictionary of column
'references for use in further calls

'INPUTS:
'Source workbook

'OUTPUTS:
'Stored dictionary of column headers from source workbook

'REQUIREMENTS:
'Enable Microsoft Scripting Runtime Reference Library

    Dim columns As Scripting.Dictionary

Function store_all_columns_fn(header_row As Integer)
    Set OutputWS = ActiveWorksheet
    Set columns = New Scripting.Dictionary
    columns.RemoveAll
    
    count_of_columns = 4
    
    For current_col = 1 To count_of_columns
        current_col_header = OutputWS.Cells(header_row, current_col)
        columns.Add current_col_header & "_Col", current_col_header
    Next
End Function
Sub store_all_columns()
    Dim OutputWS As Worksheet
    
    Set OutputWS = ActiveWorkbook.ActiveSheet
    Set columns = New Scripting.Dictionary
    columns.RemoveAll
    
    header_row = 1
    count_of_columns = 4
    
    For current_col = 1 To count_of_columns
        current_col_header = OutputWS.Cells(header_row, current_col)
        columns.Add current_col_header & "_Col", current_col_header
    Next
End Sub
Sub report_all_columns()
    i = 10
    For Each Key In columns.Keys
        ThisWorkbook.ActiveSheet.Cells(i, 1) = Key
        ThisWorkbook.ActiveSheet.Cells(i, 2) = columns(Key)
        ThisWorkbook.ActiveSheet.Cells(i, 3) = ""
        i = i + 1
    Next
End Sub
Sub store_specified_columns()
    Set OutputWS = ThisWorkbook.Sheets(1)
    Set columns = New Scripting.Dictionary
    
    FindStr = "Dibby"
    StartColumn = 1
    StartRow = 1
    CountRows = 2
    CountColumns = 4

    For StartColumn = 1 To CountColumns
    
        columns.Add CellResult & "_Col", CellResult
    Next

    i = 6
    For Each Key In columns.Keys
        ThisWorkbook.ActiveSheet.Cells(i, 1) = columns(Key)
        i = i + 1
    Next
End Sub