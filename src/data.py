from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import yfinance as yf


@dataclass(frozen=True)
class DataPullConfig:
    tickers: list[str]
    start: str = "2010-01-01"   # reasonable default horizon
    end: str | None = None     # None = up to latest available
    interval: str = "1d"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def fetch_adj_close(cfg: DataPullConfig) -> pd.DataFrame:
    """
    Download Adjusted Close prices via yfinance.
    Returns a DataFrame indexed by date with columns = tickers.
    """
    df = yf.download(
        tickers=cfg.tickers,
        start=cfg.start,
        end=cfg.end,
        interval=cfg.interval,
        auto_adjust=False,      # we explicitly use Adj Close
        progress=False,
        group_by="column"
    )

    # yfinance returns multi-index columns when multiple tickers; handle both cases
    if isinstance(df.columns, pd.MultiIndex):
        px = df["Adj Close"].copy()
    else:
        # single ticker case
        px = df.rename(columns={"Adj Close": cfg.tickers[0]})[cfg.tickers[0]].to_frame()

    px.index = pd.to_datetime(px.index)
    px = px.sort_index()
    px = px.dropna(how="all")
    return px


def save_prices_csv(prices: pd.DataFrame, out_path: Path) -> None:
    """
    Save prices to CSV with ISO dates.
    """
    prices.to_csv(out_path, index=True)


def load_prices_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
