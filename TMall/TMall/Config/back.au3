Dim $username="D:\PyCharm404\__py\TMall\Files\SaveImg\back.jpg"
ControlFocus("另存为", "","Edit1");ControlFocus("title","text",controlID) Edit1=Edit instance 1
; Wait 10 seconds for the Upload window to appear

  WinWait("[CLASS:#32770]","",5)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("另存为","","Edit1")

  Sleep(500)

; Set the File name text on the Edit field

  ControlSetText("另存为", "", "Edit1", $username)

  Sleep(500)

; Click on the Open button

  ControlClick("另存为", "","Button1");

   ;ok save reeriter

ControlFocus("确认另存为", "","Edit1");

 WinWait("[CLASS:#32770]","",3)

ControlClick("确认另存为", "","Button1");