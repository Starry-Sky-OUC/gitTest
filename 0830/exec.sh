#!/bin/bash
relative_path=$1
find "$relative_path" -type f -name "*.txt" -exec gzip {} \;
echo "所有 .txt 文件已被压缩"
