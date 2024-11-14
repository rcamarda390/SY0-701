@echo off
setlocal enabledelayedexpansion

:: Define the source file and the file to be renamed

set TOOL_PATH=C:\projects\SY0-701

if not exist %TOOL_PATH%\parsed_path.TXT (
    ECHO parsed_path.TXT not set. Exiting.
exit /b
)

::for /F "tokens=1" %%i in (%TOOL_PATH%\parsed_path.TXT) do echo This is the PARSED PATH: "%%i"  & SET QUESTION_OR_ANSWER=%%i


::set file_path=E:\OneDrive\EMPLOYMENT\000 SY0-701\Parsed Questions
set file_path=E:\OneDrive\EMPLOYMENT\000 SY0-701\Parsed Answers
set content_file=ch-q.txt
set file_to_rename=%file_path%\fixedname.jpg

:: Check if content file exists
if not exist "%content_file%" (
    echo The file %content_file% does not exist.
    exit /b
)

:: Read the content of the content_file (assuming the content is in the first line)
set /p new_name=<%content_file%

:: Remove any unwanted spaces or newlines
set new_name=%new_name: =%

:: Check if fixedname.txt exists
if not exist "%file_to_rename%" (
    echo The file %file_to_rename% does not exist.
    exit /b
)

:: Rename the file
ren "%file_to_rename%" "%new_name%.jpg"

:: Notify the user
echo Renamed "%file_to_rename%" to "%new_name%.txt"
