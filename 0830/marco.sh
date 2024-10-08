#!/bin/bash

#执行 marco 时，当前的工作目录应当以某种形式保存
#当执行 polo 时，无论现在处在什么目录下，都应当 cd 回到当时执行 marco 的目录

saved_dir=""

marco() {
  saved_dir=$(pwd)
}

polo() {
  if [ -z "$saved_dir" ]; then
    echo "空目录"
  else
    cd "$saved_dir" || echo "error"
  fi
}
