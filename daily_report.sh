#!/bin/bash
report="build_report_$(date +%Y%m%d).txt"
{
  echo "=== 构建日志日报 ==="
  echo "统计时间: $(date +'%Y-%m-%d %H:%M:%S')"
  echo "总日志行数: $(wc -l < build.log)"
  fail_count=$(grep -c "STATUS:FAIL" build.log)
  total_lines=$(wc -l < build.log)
  echo "失败率: $(( fail_count * 100 / total_lines ))%"
  echo "TOP错误:"
  grep "STATUS:FAIL" build.log | awk '{print $NF}' | sort | uniq -c | sort -nr | head -3
} | tee "$report"
echo "报告已生成: $report"
read -p "按Enter键继续..."  # 保持窗口打开
