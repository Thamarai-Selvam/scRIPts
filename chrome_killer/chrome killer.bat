@echo off
for /l %%i in (1,1,100) do (
	echo Tab count: %%i
	start chrome.exe "about:blank"
)
