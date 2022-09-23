"""
@Time : 2022/9/21 15:10 
@Author : ls
@DES: 
"""
from fastapi import APIRouter

router = APIRouter(prefix='/login')


@router.get("/")
async def login(name: str):
    if name == 'tom':
        return "登录成功"
    else:
        return "用户名错误"
