import argparse
import sys
import os
import io
import json
import pandas as pd

#!/usr/bin/env python3
"""
analise_segmento.py

Simple exploratory script to load a leads CSV and show basic diagnostics.
Usage:
    python analise_segmento.py [--file PATH] [--preview N] [--save-report PATH]
"""


def load_csv(path):
        if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")
        try:
                return pd.read_csv(path)
        except Exception:
                # fallback to a more permissive encoding
                return pd.read_csv(path, encoding="latin1")


def summary_report(df):
        rep = {}
        rep["shape"] = {"rows": int(df.shape[0]), "cols": int(df.shape[1])}
        rep["dtypes"] = {col: str(dtype) for col, dtype in df.dtypes.items()}
        rep["missing"] = {col: int(df[col].isna().sum()) for col in df.columns}
        rep["missing_pct"] = {
                col: float(df[col].isna().mean() * 100) for col in df.columns
        }
        rep["numeric_describe"] = df.select_dtypes(include="number").describe().to_dict()
        rep["object_top_values"] = {}
        for col in df.select_dtypes(include="object").columns:
                rep["object_top_values"][col] = df[col].value_counts(dropna=False).head(10).to_dict()
        return rep


def print_summary(rep, preview_df=None):
        print("Shape:", rep["shape"])
        print("\nDtypes:")
        for col, dtype in rep["dtypes"].items():
                print(f"  {col}: {dtype}")
        print("\nMissing (count, %):")
        for col in rep["missing"]:
                print(f"  {col}: {rep['missing'][col]} ({rep['missing_pct'][col]:.2f}%)")
        print("\nNumeric summary (sample):")
        numeric = rep.get("numeric_describe", {})
        for col, stats in numeric.items():
                print(f"  {col}: count={stats.get('count')}, mean={stats.get('mean')}, std={stats.get('std')}")
        print("\nTop values for object columns:")
        for col, vals in rep.get("object_top_values", {}).items():
                print(f"  {col}: {list(vals.items())[:5]}")
        if preview_df is not None:
                print(f"\nPreview (first {len(preview_df)} rows):")
                print(preview_df.to_string(index=False))


def main():
        p = argparse.ArgumentParser(description="Analyze leads CSV")
        p.add_argument("--file", "-f", default="leads.csv", help="Path to CSV file")
        p.add_argument("--preview", "-n", type=int, default=5, help="Number of preview rows")
        p.add_argument("--save-report", "-s", help="Path to save JSON report")
        args = p.parse_args()

        try:
                df = load_csv(args.file)
        except Exception as e:
                print("Error loading CSV:", e, file=sys.stderr)
                sys.exit(1)

        # basic outputs
        preview = df.head(args.preview)
        rep = summary_report(df)
        print_summary(rep, preview_df=preview)

        if args.save_report:
                try:
                        with open(args.save_report, "w", encoding="utf-8") as fh:
                                json.dump(rep, fh, ensure_ascii=False, indent=2)
                        print(f"\nReport saved to {args.save_report}")
                except Exception as e:
                        print("Could not save report:", e, file=sys.stderr)


if __name__ == "__main__":
        main()