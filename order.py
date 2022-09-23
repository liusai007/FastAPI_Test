"""
@Time : 2022/9/21 16:39 
@Author : ls
@DES: 
"""
from fastapi import APIRouter

router = APIRouter(prefix='/order')


@router.get("/")
async def order(good: str):
    if good == 'car':
        return "买车成功"
    else:
        return "买车错误"
