@echo off
for /1 %%i in (1,1,10) do (
	start chrome.exe "about:blank"
	echo Tab count: %%i
)