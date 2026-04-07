
import time
from urllib.parse import quote

import requests

# ===================== 【关键】粘贴你的 token =====================
ZP_STOKEN = "b67agSETDn8ODxJDDh1E9woJNSDhFSEpIRE9GTEhEdDZGQ0dMS00lP8OPxIshw7Vsw5xBw45JOU9ITkhERUhFTSlPTEZDRExJRsWCw4dESUZ7xIVRODAzw4TEhBzDuHDDlz3CosOFFybDjxfCqcODExfDiBLDssOHPTMeGBwTGR1pZBJtcWgcIBwWF2JwFmRsEhwWFhdiE2chFycvTmbDhkfDghPDg0PDkRzDhkbDjUdMQ0YzQ0zCs05LUE5HRUtCxY3FgsWHxYLFicWNxYLDl8OaxIbDqcWCxYfFgsOGxY3FgsWHxILDpsWNxYLFh8WCxIfDjEFFwqDDh1bFhMKnxYnDtsSuwqLCo8KUU8Krw4HCusOAwqFcxIdYwqVSUsOMwrHDicOMf8K3w43DjMOPw4nCgMK%2BwrTCvm3DhMKFw4FfVVjCucOGZRnDhMKLfB0SbMKJG2NQG2PCqMOT"
ZP_NAME = "2d9713a7"
a = "53032661.1761475655.1773743494.1774964297.82.7.14.24"
c = "1774964297"

# 不限制关键词、不限制地区（纯测试）
KEYWORD = ""
CITY_CODE = "000000"

# 带登录态的请求头（反爬核心）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Referer": "https://www.zhipin.com/",
    "Accept": "application/json, text/plain, */*",
    "Cookie": "ab_guid=56b247c2-73d8-45fa-b7fc-fbb4145e79c4;lastCity=101280600;__g=-;Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1773191392,1773455723,1773743494,1774964298;HMACCOUNT=FB1D3534B01B7993;Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1775121801;__c=1774964297;__a=53032661.1761475655.1773743494.1774964297.82.7.14.24;bst=V2R9siGef_2FtoVtRuyBgRKi-w7DrVwiQ~|R9siGef_2FtoVtRuyBgRKi-w7DrXzSs~;__zp_stoken__=b67agSU7DlsOMxI3DhkM0wo5QSTpMT09JTkZRUUlOfUFDQk1FRFAkw7zDhcSCYMO0ZsOVwpvDi0g7Rk9LSU5MT0hMK0ZDQ0JORk5DxYPDjU1OQ3rEj0g%2FLcKdw43Ei1fDtXHDnTTCrcOIFizDhiDCpMOCIR7DjxfDs8ONNDwbGRYaHiBobhtibGkWGRMTFnBpIWltIBUhExZwGnAcFi0mSRvDhsONw4xEw4fDgsOES8OQw4XDi01FT8ONST5JTMKzSkVKTkdJRUjFjcWCxYPFjMWDxY3FgsOTw5TEhMOpxYLFg8WMw4TFjcWCxYPEjMOkxY3FgsWDxYzEhcOMQUnCl8OFwpfFisKixY%2FDtMSuwqLDjcO6wqjDvFvEhWnCmFXCpsK8wrx6wrXCssKmwoHCpcKAwpZWVMONw4nCgMK6wrrCvG3DhMKJwrddVVjCtcOQZxnDhMKPch8SbMKFFWlQG0PCpsOT",
}

# =================================================================

def test_crawl_login():
    print("已登录，开始测试爬取 Boss 直聘 全量岗位...\n")

    try:
        url = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?query=&city=000000&page=1&pageSize=10"

        time.sleep(1)
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("resonsp = ",data)

        job_list = data.get("zpData", {}).get("jobList", [])

        if not job_list:
            print("❌ 还是没数据 → token 复制错了，重新复制！")
            return

        # 成功输出
        print(f"✅ 成功爬到数据！共 {len(job_list)} 条\n")
        for i, job in enumerate(job_list[:5]):
            print(f"【岗位{i+1}】{job.get('jobName')} | {job.get('brandName')} | {job.get('salaryDesc')}")

    except Exception as e:
        print(f"❌ 爬取失败：{str(e)}")

if __name__ == "__main__":
    test_crawl_login()
