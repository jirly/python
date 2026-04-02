
import time
from urllib.parse import quote

import requests

# ===================== 【关键】粘贴你的 token =====================
ZP_STOKEN = ""

# 不限制关键词、不限制地区（纯测试）
KEYWORD = "b67agR0fDlsOGxI7DiEo3PVBHM09FTEdHRUNKR0d+M0hEREZOSyLDncOEw6rDucOzb8OWwrvDkEYyRUVQR0dPRUNKIkVRSERHRkRIxYXDhE5ESMKsRjUxw5nDhsOww7fDuWvDlDXCp8OFFCXDhxLCqcOIGB/DhRLDucOENTYeEx8bFB1iZxpwcWMfGCEWFGloE2RvGRQTFhRpG2IhFCQnS2bDhUTDihbDg0jDihTDg33Dj0REE0Y4SETCtk5QS0ZERVBJxYXFh8WHxYnFgsWFxYfDl8OhxIXDscWHxYfFicOFxYXFh8WHxInDpcWFxYfFh8WJxITDhDxFwqDDhMSPxZHEncWDw7XEpsKnwr/Crl/CmMKnwpl9wqtSw4nDgMOIasOAfcKXYlTCvcK3dcKtw4lfw4XDh2pnwotWan3DiMOJw4Zmw4/Dj3tsZn1iGnHCiSBoSB7CocO9w5M="
CITY_CODE = "000000"

# 带登录态的请求头（反爬核心）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Referer": "https://www.zhipin.com/",
    "Accept": "application/json, text/plain, */*",
    "Cookie": f"__zp_stoken__={ZP_STOKEN}"
}

# =================================================================

def test_crawl_login():
    print("🔍 已登录，开始测试爬取 Boss 直聘 全量岗位...\n")

    try:
        url = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?query=&city=000000&page=1&pageSize=10"

        time.sleep(1)
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()

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
