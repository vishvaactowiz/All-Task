import requests as re

def request(url):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': 'akamai_generated_location={"zip":"""","city":"AHMEDABAD","state":"GJ","county":"""","areacode":"""","lat":"23.03","long":"72.62","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=88~id=62751d91f20a387917bf508970e2d9ff; eXr91Jra=Aw4YhqmdAQAA4rQJ1Tz6gQnyxG-7yARZODVa387_XawO-kLQAl65hias4KnfAS1yQYOuco1HwH8AAEB3AAAAAA|1|0|18de1d083359298bb92a88960490fe83350c2bcf; __host_color_scheme=ps9VWIn1-3UZFh-XHgzZDxdsD0v-Segux3ZKtncKd0e38tdO2Ywg; __host_theme_options=1776665631349; usprivacy=1---; algoliaUT=8efd6310-49f8-40b2-b9db-c564af822cc0; check=true; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C49981354674629128521120048296192984817%7CMCAAMLH-1777270434%7C12%7CMCAAMB-1777270434%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776672834s%7CNONE%7CvVersion%7C4.6.0; s_cc=true; mbox=session#407945b5e39547e9a00d29e32127b02b#1776667495|PC#407945b5e39547e9a00d29e32127b02b.41_0#1839910435; _cb=CmHuZCBzo4z5CXpLe2; _chartbeat2=.1776665635309.1776665635309.1.CTBPJgB6tDjeCcsEtIDDQZaUBoBd9t.1; _cb_svref=external; _ALGOLIA=anonymous-6f5accfb-b27a-49b6-a506-f31b973bcbe5; _awl=2.1776665636.5-ed14e1a8698d84e79016aeb022a2ef3f-6763652d617369612d6561737431-0; __gads=ID=317b35f8c9e799da:T=1776665635:RT=1776665635:S=ALNI_MaXeCgoy6-2gN0gZM4deYUvy2qyeg; __gpi=UID=0000126e14c11580:T=1776665635:RT=1776665635:S=ALNI_Mb0IahYURLy6a_LaNly3KvVIdEcnA; __eoi=ID=525773f271e7e384:T=1776665635:RT=1776665635:S=AA-AfjZ2W0F6gHHRJGcD-bHRlZ2f; OptanonAlertBoxClosed=2026-04-20T06:13:57.121Z; OneTrustWPCCPAGoogleOptOut=false; sailthru_pageviews=2; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+11%3A43%3A57+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=ae838ae4-3c51-44de-aaeb-4c7294a3d5ee&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&crTime=1776665637897; cto_bundle=65EtPF9YbVlCZ3hvJTJCYnFoeVg1RU14SUpmb0ZCRmw5NzBwOGR1RmF4eWxqSFl3UUlFN1JUczNwN0x6d0FuRm0lMkY3cUpGNFpPVGFDcjhqTDRqRWN2TSUyQjZSQlZ5ODFPcnZROExVdjdESXVwdGRkaDBXamd1MkFiV0ZBMkEzcURwMmRCSVlDWTBGZTN1T1YlMkZ1aWZERm1jTTFzTE5JdjdUdkhQSmwwZkY1M2R2dzBmQnZTUSUzRA; s_sq=%5B%5BB%5D%5D',
    }
    
    response = re.get(url,headers = headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print("error")