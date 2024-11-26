@echo off
setlocal enabledelayedexpansion

set filename=question.txt
:: directory where control files exist
set TOOL_PATH=e:\projects\SY0-701

if not exist %TOOL_PATH%\parsed_path.TXT (
    ECHO parsed_path.TXT not set. Exiting.
exit /b
)

cd %TOOL_PATH%

:: Check if the file exists
if not exist %filename% (
    :: File doesn't exist, create it and insert 1 without a trailing newline
    >%filename% ( 
        <nul set /p =1
    )
    echo File %filename% created with number 1.
    exit /b
)

:: If the file exists, read the number
set /p number=<%filename%

:: Check if the number is valid (an integer)
for /f "delims=0123456789" %%a in ("%number%") do (
    echo Error: Invalid content in %filename%.
    exit /b
)

:: Increment the number by 1
set /a number+=1

:: Write the incremented number back to the file without a newline
>%filename% ( 
    <nul set /p =%number%
)

echo File %filename% updated with number %number%.
