:: =========================================================================
:: In Line 5, @echo off suppresses showing the prompt and commands entered. 
:: Only the actual output of the commands being run
:: =========================================================================
@echo off

:: ==============================================================================================
:: This command adds the dashed line at the beginning of the output to the file. E.g: Youtube.txt
:: ==============================================================================================
echo ---------------------------------------------- >> Youtube.txt
echo ---------------------------------------------- >> Facebook.txt

:: ===========================================================================================
:: In Line 17, this command adds the text "Doing tracert at %date%, %time%"
:: to the .txt file.  %date% is a variable that automatically captures your PCs current date.
:: %time%  is a variable that automatically captures your PCs current time.
:: ===========================================================================================
echo Doing tracert at %date%, %time% >> Youtube.txt
echo Doing tracert at %date%, %time% >> Facebook.txt

:: ===========================================================================================
:: In Line 23, the command runs a traceroute to the website, for example "www.youtube.com"
:: It then saves the output to the .txt file. For example, Youtube.txt
:: ===========================================================================================
tracert www.youtube.com >> Youtube.txt
tracert www.facebook.com >> Facebook.txt

:: ====================================================================================================
:: In Line 28, this command adds the dashed line at the beginning of the output to the file Youtube.txt
:: ====================================================================================================
echo ---------------------------------------------- >> Youtube.txt
echo ---------------------------------------------- >> Facebook.txt