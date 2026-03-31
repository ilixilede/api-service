# utils.py

import json
from typing import Dict, List
from aiohttp import ClientSession

def load_json(file_path: str) -> Dict:
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data: Dict, file_path: str) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def get_api_data(url: str, params: Dict) -> Dict:
    async def fetch_data():
        async with ClientSession() as session:
            async with session.get(url, params=params) as response:
                return await response.json()

    import asyncio
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(fetch_data())

def flatten_dict(data: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    def flatten(x, name=''):
        out = {}
        for k, v in x.items():
            if isinstance(v, dict):
                out.update(flatten(v, name + k + sep))
            else:
                out[name + k] = v
        return out

    return flatten(data)