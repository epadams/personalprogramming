#!/bin/bash

yt-dlp -F $1

read uFormat

#yt-dlp --add-metadata --embed-thumbnail --split-chapters -o "chapter:%(title)s - %(section_number)03d %(section_title)s [%(id)s].%(ext)s" -f $uFormat $1
#yt-dlp --add-metadata --write-thumbnail --split-chapters -f $uFormat $1
#yt-dlp --split-chapters --parse-metadata 'chapter:title' -f $uFormat $1 --exec rm
#yt-dlp --split-chapters --embed-thumbnail -o "title:%(section_title)s" -f $uFormat $1 --exec rm
yt-dlp --split-chapters -o "title:%(section_title)s" -f $uFormat $1 --exec rm

exit
