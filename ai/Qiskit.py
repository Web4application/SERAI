' === BUILD ALL SHEETS ===
Sub Build_Aura_Sheets()
    Call Build_Aura_Home_UI
    Call Setup_Data_Sheet
    Call Setup_Logs_Sheet
    Call Setup_Collab_Sheet
    Call Setup_Visualization_Sheet
    Call Setup_Deployment_Sheet
    Call Setup_Ethics_Sheet
End Sub

' === DATA SHEET ===
Sub Setup_Data_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Data")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "📊 Aura Data Repository"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Dataset Name"
    ws.Range("B3").Value = "Description"
    ws.Range("C3").Value = "Source"
    ws.Range("D3").Value = "Last Updated"
    
    ws.Range("A3:D3").Font.Bold = True
    ws.Range("A3:D3").Interior.Color = RGB(230, 230, 250)
End Sub

' === LOGS SHEET ===
Sub Setup_Logs_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Logs")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "📝 Experiment Logs"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Date"
    ws.Range("B3").Value = "Researcher"
    ws.Range("C3").Value = "Experiment Summary"
    ws.Range("D3").Value = "Results"
    ws.Range("E3").Value = "Notes"
    
    ws.Range("A3:E3").Font.Bold = True
    ws.Range("A3:E3").Interior.Color = RGB(255, 228, 225)
End Sub

' === COLLABORATION SHEET ===
Sub Setup_Collab_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Collaboration_Log")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "🤝 Collaboration Log"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Date"
    ws.Range("B3").Value = "Contributor"
    ws.Range("C3").Value = "Contribution"
    ws.Range("D3").Value = "Status"
    
    ws.Range("A3:D3").Font.Bold = True
    ws.Range("A3:D3").Interior.Color = RGB(224, 255, 255)
End Sub

' === VISUALIZATION CONFIG SHEET ===
Sub Setup_Visualization_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Visualization_Config")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "📈 Visualization Config"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Chart Name"
    ws.Range("B3").Value = "Data Source"
    ws.Range("C3").Value = "Chart Type"
    
    ws.Range("A3:C3").Font.Bold = True
    ws.Range("A3:C3").Interior.Color = RGB(240, 248, 255)
End Sub

' === DEPLOYMENT SHEET ===
Sub Setup_Deployment_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Deployment")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "🚀 Deployment Settings"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Environment"
    ws.Range("B3").Value = "Version"
    ws.Range("C3").Value = "Config Path"
    ws.Range("D3").Value = "Last Tested"
    
    ws.Range("A3:D3").Font.Bold = True
    ws.Range("A3:D3").Interior.Color = RGB(245, 245, 220)
End Sub

' === ETHICS SHEET ===
Sub Setup_Ethics_Sheet()
    Dim ws As Worksheet
    Set ws = GetOrCreateSheet("Ethics_Notes")
    ws.Cells.Clear
    
    ws.Range("A1").Value = "⚖️ Ethics Notes"
    ws.Range("A1").Font.Size = 14
    ws.Range("A1").Font.Bold = True
    
    ws.Range("A3").Value = "Topic"
    ws.Range("B3").Value = "Concern"
    ws.Range("C3").Value = "Resolution"
    
    ws.Range("A3:C3").Font.Bold = True
    ws.Range("A3:C3").Interior.Color = RGB(255, 250, 205)
End Sub

' === HELPER: CREATE IF NOT EXISTS ===
Function GetOrCreateSheet(sheetName As String) As Worksheet
    On Error Resume Next
    Set GetOrCreateSheet = ThisWorkbook.Sheets(sheetName)
    If GetOrCreateSheet Is Nothing Then
        Set GetOrCreateSheet = ThisWorkbook.Sheets.Add
        GetOrCreateSheet.Name = sheetName
    End If
    On Error GoTo 0
End Function
