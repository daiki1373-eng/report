"""
watch_folder.py
- inbox フォルダを監視して、daily/kw の組が揃ったら run_once 相当の処理を呼ぶ入口（雛形）
"""

import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--inbox", default="./inbox")
    p.add_argument("--out", default="./out")
    p.add_argument("--processed", default="./processed")
    p.add_argument("--failed", default="./failed")
    args = p.parse_args()

    print("TODO: implement watcher")
    print(args)

if __name__ == "__main__":
    main()
