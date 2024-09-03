#!/bin/bash
relative_path=$1
archive_name="exec.gz"
find "$relative_path" -type f -name "*.txt.gz" -print0 | tar -czvf "$archive_name" --null -T -
echo "所有 .txt.gz 文件已被压缩到 $archive_name"
