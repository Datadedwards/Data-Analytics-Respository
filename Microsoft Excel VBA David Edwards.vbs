Attribute VB_Name = "Module1"
Sub VBA_Homework_easymode_David()

    For Each ws In Sheets
    
        Dim ticker As String
        Dim volume As LongLong
        volume = 0
        Dim Stock_Table_Row As Integer
        Stock_Table_Row = 2
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Total Stock Volume"
        Last_Row = Range("A" & Rows.Count).End(xlUp).Row
    

    
        For i = 2 To Last_Row
    
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            
                ticker = ws.Cells(i, 1).Value
            
                volume = volume + ws.Cells(i, 7)
            
                ws.Range("I" & Stock_Table_Row).Value = ticker
            
                ws.Range("J" & Stock_Table_Row).Value = volume
            
                Stock_Table_Row = Stock_Table_Row + 1
            
                volume = 0
            
            Else
            
                volume = volume + ws.Cells(i, 7).Value
        
            End If
        
        Next i

    Next ws

End Sub


