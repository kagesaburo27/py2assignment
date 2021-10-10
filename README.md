# py2assignment
# Web Scrapping


### Installation
PyPI
```bash
pip install beautifulsoup4
```

### Usage

```python
from bs4 import BeautifulSoup
import requests
scrapper = Scrapper()
```

 ### Examples

Usage examples:
```python
>>>  page = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + coin_name + ", headers=headers")
Enter the coin's name
bitcoin
Latest information in market 2021-10-10 20:24:00.550001: 

Block Header | Alexandria - CoinMarketCapcoinmarketcap.com › alexandria › glossary › block-hea...A block header is a unique identifier for a block on a blockchain that is hashed on ... Block headers are frequently used in Bitcoin developer documentation ...
Today's Top 100 Crypto Coins Prices And Data | CoinMarketCapcoinmarketcap.com › coinsCryptocurrency coins listed by market capitalization. Today's prices for the top 100 crypto coins including BTC, ETH, XRP, BCH. LTC and many more.
Today's Top 100 Crypto Tokens Prices And Data | CoinMarketCapcoinmarketcap.com › tokensCrypto and blockchain tokens. Today's prices for the top 100 
blockchain tokens including stablecoins like Tether, listed by market capitalization.
CoinMarketCap API Documentationcoinmarketcap.com › api › documentation/exchange/*, Endpoints that return data around cryptocurrency exchanges such as ... Each HTTP request must contain the header Accept: application/json .
Crypto Glossary | CoinMarketCap | Alexandriacoinmarketcap.com › alexandria › glossaryFind out the meaning of cryptocurrency and blockchain's hidden 
language with ... A block header is a unique identifier for a block on a blockchain that is ...
Timestamp | Alexandria - CoinMarketCapcoinmarketcap.com › alexandria › glossary › timestampWhen a BTC block is generated, two timestamps are usually involved. One is the block header which is imputed by the miner. The second is the actual at which ...
Light Node | Alexandria - CoinMarketCapcoinmarketcap.com › alexandria › glossary › light-nodeThe block header is this detailed summary of a specific block which includes information ... A physical unit of Bitcoin that comes in the form of brass, ...
Floating Table Headers and Full-Screen Charts - CoinMarketCap Blogblog.coinmarketcap.com › 2018/04/10 › coinmarketcap...2018 ж. 10 сәу. · We will share often as we explore cryptocurrency and blockchain around the world with you. Get updates direct in your inbox by entering your ...
Hedera Hashgraph price today, HBAR to USD live ... - CoinMarketCapcoinmarketcap.com › currencies › hedera-hashgraphGet the latest Hedera Hashgraph price, HBAR market cap, trading pairs, charts and data today from the world's number one cryptocurrency price-tracking ...
Blockchain Explorer Guide | CoinMarketCapcoinmarketcap.com › guides › blockexplorerCoinMarketCap's block explorer currently has indices for Bitcoin, Ethereum and ... On the left side of the header, you'll see the CoinMarketCap logo, ...
```
