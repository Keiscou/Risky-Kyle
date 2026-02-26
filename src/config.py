from pathlib import Path

# Project root = folder containing this file's parent folder (src/)
ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

REPORTS_DIR = ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Assets for the MVP
TICKERS = ["SPY", "TLT", "HYG", "LQD", "UUP"]
OPTIONAL_TICKERS = ["GLD"]  # not used by default; easy to add later
