@echo off
setlocal enabledelayedexpansion

:: the call will change directory, dont need to do it here too??
:: Define the input and output files
set chapter_file=chapter.txt
set question_file=question.txt
set output_file=ch-q.txt

:: Read the contents of chapter.txt and question.txt into variables
set /p chapter_content=<%chapter_file%
set /p question_content=<%question_file%

:: Combine the contents of chapter.txt and question.txt with " - " in between
set combined_content=%chapter_content%-%question_content%

:: Use > to overwrite and remove newline by using set /p (no newline added)
<nul set /p= %combined_content% > %output_file%
call "increment_question.cmd"
echo Done! The file %output_file% has been created with the content: %combined_content%
