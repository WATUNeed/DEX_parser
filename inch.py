import json
from pprint import pprint

import aiohttp
import requests


# def inch_resp(amount: float):
#     amount = str(int(round(amount * 1000000000000000000)))
#     headers = {
#         'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#         'Accept': 'application/json, text/plain, */*',
#         'Referer': 'https://app.1inch.io/',
#         'DNT': '1',
#         'sec-ch-ua-mobile': '?0',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#         'sec-ch-ua-platform': '"Windows"',
#     }
#
#     params = {
#         'walletAddress': '0x0000000000000000000000000000000000000000',
#         'fromTokenAddress': '0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270',
#         'toTokenAddress': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
#         'amount': amount,
#         'enableEstimate': 'false',
#     }
#     resp = requests.get('https://fusion.1inch.io/quoter/v1.0/137/quote/receive', params=params, headers=headers)
#     data = json.loads(resp.content)
#     print(data)
#     return data['volume']['usd']['fromToken'], data['presets']['medium']['auctionStartAmount']


async def inch_resp(amount: float):
    amount = str(int(round(amount * 1000000000000000000)))
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://app.1inch.io/',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'walletAddress': '0x0000000000000000000000000000000000000000',
        'fromTokenAddress': '0x5fe2b58c013d7601147dcdd68c143a77499f5531',
        'toTokenAddress': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
        'amount': amount,
        'enableEstimate': 'false',
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://fusion.1inch.io/quoter/v1.0/137/quote/receive', params=params) as resp:

            data = json.loads(await resp.text())
            return data['volume']['usd']['fromToken'], data['presets']['medium']['auctionStartAmount']

