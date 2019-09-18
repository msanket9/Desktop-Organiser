#!/bin/sh
cd 
cd Desktop 

echo "Suggest a name for your desktop Folder?"
read name
mkdir $name

cd $name
mkdir Media
mkdir Other 
mkdir Programming
mkdir Text

cd Media 
mkdir Audio
mkdir Images 
mkdir Video
cd ..

cd Other
mkdir Compressed 
mkdir Disc
mkdir Executables
mkdir Fonts
mkdir Internet
mkdir Uncategorized
cd ..

cd Programming
mkdir CnC++
mkdir CSS
mkdir Dart
mkdir Database
mkdir HTML
mkdir Java
mkdir JavaScript
mkdir Python
mkdir Shell 
mkdir Swift
cd ..

cd Text
mkdir Document
mkdir Other
mkdir Presentation
mkdir Spreadsheet
mkdir TextFiles

cd Document
mkdir Microsoft
mkdir PDF
cd ..

cd Other
mkdir System
cd ..

cd Presentation
mkdir Microsoft
cd ..

cd Spreadsheet
mkdir Microsoft
cd ..

cd 

