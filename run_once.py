"""
run_once.py
- daily.csv と kw.csv を受け取り、レポートを生成する入口（雛形）
"""

import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--daily", required=True, help="path to daily csv")
    p.add_argument("--kw", required=True, help="path to keyword csv")
    p.add_argument("--config", default="config.yaml", help="path to config yaml")
    args = p.parse_args()

    daily = Path(args.daily)
    kw = Path(args.kw)
    config = Path(args.config)

    print("TODO: implement")
    print(f"daily={daily}")
    print(f"kw={kw}")
    print(f"config={config}")

if __name__ == "__main__":
    main()
