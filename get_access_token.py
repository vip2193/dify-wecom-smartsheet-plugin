#!/usr/bin/env python3
"""获取企业微信access_token"""
import requests

# 配置你的企业信息
CORPID = "你的企业ID"  # 在"我的企业"中查看
CORPSECRET = "WiqfTg7yk7n0w5wdzd9YaSZiAKXb6RLBTimLBg3bPpo"  # 在"应用管理"中查看

def get_access_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORPID}&corpsecret={CORPSECRET}"
    
    try:
        response = requests.get(url)
        result = response.json()
        
        if result.get("errcode") == 0:
            access_token = result.get("access_token")
            expires_in = result.get("expires_in")
            print(f"✓ 获取成功!")
            print(f"Access Token: {access_token}")
            print(f"有效期: {expires_in}秒 ({expires_in//3600}小时)")
            return access_token
        else:
            print(f"✗ 获取失败!")
            print(f"错误码: {result.get('errcode')}")
            print(f"错误信息: {result.get('errmsg')}")
            return None
    except Exception as e:
        print(f"✗ 请求异常: {str(e)}")
        return None

if __name__ == "__main__":
    get_access_token()
