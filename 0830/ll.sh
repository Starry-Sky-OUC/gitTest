#!/bin/bash

relative_path=$1

if [ -z "$relative_path" ]; then
  echo "路径不能为空"
  exit 1
fi

ls -lah --time=atime --sort=time --color=auto "$relative_path"
