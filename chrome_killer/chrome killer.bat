@echo off
for %%i in (1,1,100) do (
	start chrome.exe "about:blank"
	echo Tab count: %%i
)
