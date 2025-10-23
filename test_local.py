#!/usr/bin/env python3
"""本地测试脚本 - 测试所有工具"""
import sys
sys.path.insert(0, '.')

from tools.create_sheet import CreateSheetTool
from tools.add_rows import AddRowsTool
from tools.get_rows import GetRowsTool
from tools.update_rows import UpdateRowsTool

# 模拟runtime凭证
class MockRuntime:
    def __init__(self, corpid, corpsecret):
        self.credentials = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

# 配置你的企业信息
CORPID = "你的企业ID"
CORPSECRET = "你的应用Secret"
SHEET_ID = "你的表格ID"  # 如果测试创建表格,会自动生成
SHEET_NAME = "Sheet1"

def test_create_sheet():
    """测试创建表格"""
    print("\n" + "="*50)
    print("测试0: 创建表格")
    print("="*50)
    
    tool = CreateSheetTool()
    tool.runtime = MockRuntime(CORPID, CORPSECRET)
    
    params = {
        "sheet_name": "测试表格_" + str(int(time.time()))
    }
    
    for message in tool._invoke(params):
        print(f"结果: {message.message}")
        # 如果成功,可以获取docid用于后续测试

def test_add_rows():
    """测试添加行"""
    print("\n" + "="*50)
    print("测试1: 添加行")
    print("="*50)
    
    tool = AddRowsTool()
    tool.runtime = MockRuntime(CORPID, CORPSECRET)
    
    params = {
        "sheet_id": SHEET_ID,
        "sheet_name": SHEET_NAME,
        "rows_data": '[["张三", "25", "工程师"], ["李四", "30", "设计师"]]'
    }
    
    for message in tool._invoke(params):
        print(f"结果: {message.message}")

def test_get_rows():
    """测试查询行"""
    print("\n" + "="*50)
    print("测试2: 查询行")
    print("="*50)
    
    tool = GetRowsTool()
    tool.runtime = MockRuntime(CORPID, CORPSECRET)
    
    params = {
        "sheet_id": SHEET_ID,
        "sheet_name": SHEET_NAME,
        "row_start": 0,
        "row_count": 10
    }
    
    for message in tool._invoke(params):
        print(f"结果: {message.message}")

def test_update_rows():
    """测试更新行"""
    print("\n" + "="*50)
    print("测试3: 更新行")
    print("="*50)
    print("注意: 需要先运行test_get_rows获取row_id")
    
    tool = UpdateRowsTool()
    tool.runtime = MockRuntime(CORPID, CORPSECRET)
    
    params = {
        "sheet_id": SHEET_ID,
        "sheet_name": SHEET_NAME,
        "row_id": "从get_rows获取的row_id",
        "row_data": '["王五", "35", "经理"]'
    }
    
    for message in tool._invoke(params):
        print(f"结果: {message.message}")

if __name__ == "__main__":
    import time
    
    print("企业微信在线表格插件 - 本地测试")
    print("请先在脚本中配置: CORPID, CORPSECRET")
    
    # 运行测试
    # test_create_sheet()  # 创建新表格
    test_add_rows()
    test_get_rows()
    # test_update_rows()  # 需要先获取row_id
    
    print("\n" + "="*50)
    print("测试完成!")
    print("="*50)


