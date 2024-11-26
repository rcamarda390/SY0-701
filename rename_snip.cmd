@echo off
setlocal enabledelayedexpansion

:: Define the source file and the file to be renamed
:: directory where control files exist
set TOOL_PATH=e:\projects\SY0-701
set image_path=Unassigned

if not exist "%TOOL_PATH%\parsed_path.txt" (
    ECHO "parsed_path.TXT not set. >%TOOL_PATH%\parsed_path.TXT< Exiting."
    exit /b
) else (
    echo "parsed_path.txt Exists"
)
set Parsed_Path="%TOOL_PATH%\parsed_path.TXT"

:: get the path where images are located. Parsed_Path.txt has the image path

for /F "usebackq tokens=* delims=" %%i in (%Parsed_Path%) do (
    echo This is the PARSED PATH: "%%i"
    SET image_path=%%i
)


echo ">"%image_path%"<"

set content_file=ch-q.txt
set file_to_rename=fixedname.jpg

:: Check if content file exists
if not exist "%TOOL_PATH%\%content_file%" (
    set "msg=Tool Path Error: ThE file %TOOL_PATH%\%content_file% does not exist.""
    echo %msg%
    echo %msg% >> "%TOOL_PATH%\logs\rename_cmd.log"
    exit /b
) else (
    echo Exist: %content_file%
)

:: Read the content of the content_file (assuming the content is in the first line)
set /p new_name=<%tool_path%\%content_file%

:: Remove any unwanted spaces or newlines
set new_name=%new_name: =%

:: Check if fixedname.jpg exists
echo Checking file: "%image_path%\%file_to_rename%"



if not exist "%image_path%\%file_to_rename%" (
    echo THE file %image_path%\%file_to_rename% does not exist. Exiting
    echo "THe file %image_path%\%file_to_rename% does not exist. Exiting" >> "%TOOL_PATH%\logs\rename_cmd.log"
    exit /b
) else (
    echo file_to_rename is found
)

:: Rename the file
cd %image_path%
echo "Image_path %image_path%" >> "%TOOL_PATH%\logs\rename_cmd.log"
ren %file_to_rename% %new_name%.jpg

:: Notify the user
echo Renamed "%file_to_rename%" to "%new_name%.txt"
