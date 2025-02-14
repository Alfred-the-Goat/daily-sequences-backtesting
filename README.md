# daily-sequences-backtesting
A simple bactesting aid to show the probabilty of various 4 sequences of red and green daily candles

Note:
1.  You will need yfinance, matplotlib, and networkx, all of which can be installed via pip and are free.
2.  Note that this data is only the daily candle, not including overnight gaps.  In other words, if markets gapped up overnight and then declined over the next day, that would be considered a red candle, and vice versa.  

1: **install yfinance**:
  ```bash
  pip install yfinance
```
2: **install networx**:
```bash
pip install networkx pygraphviz
```

