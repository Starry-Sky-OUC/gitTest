#!/bin/bash
relative_path=$1
find "$relative_path" -type f -exec ls -ltu {} +
