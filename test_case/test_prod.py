from tools.api import request_tool
from tools.security.md5_tool import md5_passwd


def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '增加商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'token': pub_data['token']}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
 {
  "brand": "耐克",
  "colors": [
    "白","蓝","黄"
  ],
  "price": 2699,
  "productCode": "自动生成 字符串 3,10 数字字母",
  "productName": "r145",
  "sizes": [
    "22","33","44"
  ],
  "type": "服装"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
    pub_data["productCode"]=r.json()["data"][0]["productCode"]

def test_get_params(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改商品用户'  # allure报告中二级分类
    title = "修改商品用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU": pub_data["skuCode"],"price": 6800}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(data=data,method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "修改模块"  # allure报告中一级分类
    story = '根据产品编码批量修改商品价格'  # allure报告中二级分类
    title = "根据产品编码批量修改商品价格_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode": pub_data["skuCode"], "price": 6800}
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "修改模块"  # allure报告中一级分类
    story = ':产品改为下架后,其下商品全部成为下架'  # allure报告中二级分类
    title = ":产品改为下架后,其下商品全部成为下架_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode": pub_data["skuCode"]}
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
def test_post_data1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '产品改为预售后,其下商品全部成为预售'  # allure报告中二级分类
    title = "产品改为预售后,其下商品全部成为预售_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":pub_data["productCode"]}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_data(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '调整商品库存'  # allure报告中二级分类
    title = "调整商品库存_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":pub_data["skuCode"],"qty":999}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_recharge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类
    title = "用户充值_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
     "accountName": "string888",
    "changeMoney": 7000
}
     '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_add_order(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '增加订单'  # allure报告中二级分类
    title = "增加订单_全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token":"${token}"}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "ordeerPrice": 7000,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "${skuCode}"
    }
  ],
  "receiver": "lst",
  "receiverPhone": "188888888888",
  "receivingAddress": "上海市，闵行区",
  "sign": "",
  "userName": "string888"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title)
def test_post_json66(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '数字签字'  # allure报告中二级分类
    title = "数字签字_全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    headers = {"token": "${token}"}
    s = "receiver=lst&ordeerPrice=7000&receiverPhone=18888888888&key=guoya"
    sign = md5_passwd(s,"")
    pub_data["sign"] = sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "ordeerPrice": 7000,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "${skuCode}"
    }
  ],
  "receiver": "lst",
  "receiverPhone": "188888888888",
  "receivingAddress": "上海市，闵行区",
  "sign": "${sign}",
  "userName": "string888"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,sign=sign,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
