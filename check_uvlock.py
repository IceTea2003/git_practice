"""检查 uv.lock 并可选生成 requirements.txt"""

import argparse
import subprocess
import sys
from pathlib import Path

LOCK_FILE = "uv.lock"
OUTPUT_FILE = "requirements.txt"


def main():
    parser = argparse.ArgumentParser(description="检查 uv.lock 并可选生成 requirements.txt")
    parser.add_argument("-y", "--yes", action="store_true", help="跳过确认，直接生成")
    args = parser.parse_args()

    if not Path(LOCK_FILE).exists():
        print(f"未找到 {LOCK_FILE} 文件，当前目录不存在 uv.lock。")
        sys.exit(0)

    print(f"已检测到 {LOCK_FILE} 文件。")

    if not args.yes:
        choice = input("是否根据 uv.lock 生成 requirements.txt？(y/n): ")
        if choice.strip().lower() != "y":
            print("已取消。")
            sys.exit(0)

    print(f"正在生成 {OUTPUT_FILE} ...")
    result = subprocess.run(
        ["uv", "export", "--format", "requirements-txt", "-o", OUTPUT_FILE],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print(f"已成功生成 {OUTPUT_FILE}")
    else:
        print(f"生成 {OUTPUT_FILE} 失败，请检查 uv 是否正确安装。")
        if result.stderr:
            print(result.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
