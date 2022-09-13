set TARGET= '%cd%\bin\TwilioSmsApp.exe'
set START= '%cd%\bin'
set SHORTCUT='TwilioSmsApp.lnk'
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile  

%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.TargetPath = %TARGET%;$S.WorkingDirectory = %START%; $S.Save()"