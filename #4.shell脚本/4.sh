#!/bin/bash

# 检查参数数量是否正确
if [ $# -ne 3 ]; then
    echo "用法: $0 <搜索内容> <源文件> <目标文件>"
    exit 1
fi

# 获取参数
search_content="$1"
source_file="$2"
target_file="$3"

# 检查源文件是否存在
if [ ! -f "$source_file" ]; then
    echo "源文件 $source_file 不存在。"
    exit 1
fi

# 使用 grep 命令搜索指定内容，并显示行号
grep -n "$search_content" "$source_file" | tee "$target_file"

# 检查是否有搜索结果
if [ $? -eq 0 ]; then
    echo "搜索结果已保存到 $target_file 文件中。"
else
    echo "未找到指定内容。"
fi