Dim $username="D:\PyCharm404\__py\TMall\Files\SaveImg\back.jpg"
ControlFocus("���Ϊ", "","Edit1");ControlFocus("title","text",controlID) Edit1=Edit instance 1
; Wait 10 seconds for the Upload window to appear

  WinWait("[CLASS:#32770]","",5)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("���Ϊ","","Edit1")

  Sleep(500)

; Set the File name text on the Edit field

  ControlSetText("���Ϊ", "", "Edit1", $username)

  Sleep(500)

; Click on the Open button

  ControlClick("���Ϊ", "","Button1");

   ;ok save reeriter

ControlFocus("ȷ�����Ϊ", "","Edit1");

 WinWait("[CLASS:#32770]","",3)

ControlClick("ȷ�����Ϊ", "","Button1");