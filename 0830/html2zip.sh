#!/bin/bash
relative_path=$1
zip_name="htmlFiles.zip"
find "$relative_path" -type f -name "*.html" -print0 | xargs -0 zip "$zip_name"
echo "所有 .html 文件已被压缩到 $zip_name"
