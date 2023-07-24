import json

import aiohttp
import requests


headers = {
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': '',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'fromTokenAddress': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
    'fromTokenDecimals': '6',
    'toTokenAddress': '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
    'toTokenDecimals': '18',
    'fromAmount': '100000000',
    'userAddr': '0x0000000000000000000000000000000000000000',
    'chainId': '137',
    'slippage': '3',
    'estimateGas': 'false',
    'blockNumber': '999999999999',
    'deadLine': '1690138622',
    'source': 'dodoSwap',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxMzgzOTM4MzQzMDMwNjUzNTY2MzIzMTMxNjMzNTJkMzAzODMzMzA2NjM0NjY2NDY1NjY2MzMzMzUyZDMyMzYzMDMzMzE2NDM1MzEyZDMxNjY2MTM0MzAzMDJkMzEzODM5MzgzNDMwMzA2NTM1NjYzMzMxMzMzMDYzIiwicyI6NDAsImlhdCI6MTY5MDEzNjc5OSwiZXhwIjoxNjkwMjIzMTk5fQ.G8gRX5GRtAIBvPKm9cYCyc4PrCzn1reLIMiW7E5n2mU',
}


def dodo_resp():
    resp = requests.get('https://api.dodoex.io/route-service/frontend-v2/getdodoroute', params=params, headers=headers)
    dodo_data = json.loads(resp.content)
    print(dodo_data)
    return dodo_data['data']['resAmount'], dodo_data['data']['additionalFeeAmount']


# async def dodo_resp():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.dodoex.io/route-service/frontend-v2/getdodoroute', params=params, headers=headers) as resp:
#             dodo_data = json.loads(await resp.text())
#             return dodo_data['data']['resAmount'], dodo_data['data']['additionalFeeAmount']
