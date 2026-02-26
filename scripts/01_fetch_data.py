from pathlib import Path

from src.config import RAW_DIR, TICKERS
from src.data import DataPullConfig, ensure_dir, fetch_adj_close, save_prices_csv


def main() -> None:
    ensure_dir(RAW_DIR)

    cfg = DataPullConfig(
        tickers=TICKERS,
        start="2010-01-01",
        end=None,
        interval="1d",
    )

    prices = fetch_adj_close(cfg)

    out_path = Path(RAW_DIR) / "adj_close.csv"
    save_prices_csv(prices, out_path)

    print(f"Saved: {out_path}")
    print(f"Shape: {prices.shape}")
    print("Head:")
    print(prices.head())


if __name__ == "__main__":
    main()
