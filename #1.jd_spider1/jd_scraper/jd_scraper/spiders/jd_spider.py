import re

import requests
import scrapy
from ..sp import Detail
import os
import json

class JDSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = [
        "https://list.jd.com/list.html?cat=1318,12099,9756",
    ]
    goods={"title":"","price":"","color":"", "size":"", "sku":"","details":str(),"img_urls":list(),"attr_str":""}
    def start_requests(self):
        cookies={
            "__jda":"29846306.173943151511689615987.1739431515.1739431515.1739449397.2",
            "__jdc":"29846306",
            "__jdu":"173943151511689615987",
            "__jdv":"122270672|direct|-|none|-|1739431515118",
            "_pst":"18500425520_p",
            "_tp":"bQoH/MqFIumGj5jZ0Q0qXg==",
            "3AB9D23F7A4B3C9B":"AR2CNQYELQGHXYVNNVNEIWZS7UYFSJMJ63F5CLPYGMXI3YVHE5Y22SJB5UXLCNDBCSASCKIUOIW7NJPOGKU76OVBCU",
            "3AB9D23F7A4B3CSS":"jdd03AR2CNQYELQGHXYVNNVNEIWZS7UYFSJMJ63F5CLPYGMXI3YVHE5Y22SJB5UXLCNDBCSASCKIUOIW7NJPOGKU76OVBCUAAAAMU75BZEJAAAAAACV2GHHYPHK26DIX",
            "areaId":"13",
            "avif":"1",
            "flash":"3_ufXeIAY7rFCrOWV25yf43TtpJ06bASQbnEBt_s-PXAHSgF3hIFtRJDFNvsKJnSXLxoxCVBWIlWYHjrGmTDr6L74TAEGX0CRCG1mMeaKFH4TVa5_D3EyrFSN_3saDAMzKH9e7bHgbauUrZAsF9aSP6ky6HgKQZ3zJfIsrYv5Lk7B9gNfZhq**",
            "ipLoc-djd":"13-1000-0-0",
            "jsavif":"1",
            "light_key":"AASBKE7rOxgWQziEhC_QY6yaxzHQdBmQdomhpoiRuec01s7Oafz_4Rlld3Y8SWPbzrU-TrbT",
            "mba_muid":"173943151511689615987",
            "pin":"18500425520_p",
            "pinId":"jsSpVomLMkB4-qPS9PNQiQ",
            "shshshfpa":"cca54cc2-2aa9-aae7-70aa-e6fdd6f24b5f-1739431516",
            "shshshfpb":"BApXS7fpM_PFAU-LS2O5EU8Jjj4ptNPqFBnsCEjlo9xJ1MuClsIG2",
            "shshshfpx":"cca54cc2-2aa9-aae7-70aa-e6fdd6f24b5f-1739431516",
            "thor":"FFC264252E62EA92743718F58BA29C5390A41E9E586F68CAE937C2C9B05C2CDDA515333A83039EDC390C4E81EDF5D367876F6BC49E1F20D56C3FF1D23B7D0F7D8F36CDC2B36AD0039184B5E84F815654353BF554678400AE0651255D42BF9AA326D2356D29809324B710AFC5FD690D630237A2D05C71A4162ACEF4BB796974ABC6F3E57ED8EBA5C4952363DE2F8F8FBE",
            "TrackID":"1P7Ns7vHS8Q5iYqaN9tY_uUXEETL9qFCP7MO2H3E4r0zEqEV_3VCcqqAXLDHVmiAppPLbDQ-ALH6pWTcRrm1EMykpOqJ_6KjQzRYIP7M4CAOWCrtdmx0REdJfn4YNchKC",
            "unick":"jd185004lts",
            "x-rp-evtoken":"mGW9U4qbzsaBdCMe70m9pBL_IXbAkPPIV0x-vgZ91X5EqemFEBcAQAVyH8NCDtieR3jKgNWPK5ERVkamfroW2w==",
            "xapieid":"jdd03AR2CNQYELQGHXYVNNVNEIWZS7UYFSJMJ63F5CLPYGMXI3YVHE5Y22SJB5UXLCNDBCSASCKIUOIW7NJPOGKU76OVBCUAAAAMU75BZEJAAAAAACV2GHHYPHK26DIX"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.get_headers(), cookies=cookies, callback=self.parse)

    def get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://www.jd.com/",
            "Upgrade-Insecure-Requests": "1",
            'Cookie': '__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1739453919140; mba_muid=1739453919139976805723; mba_sid=17394539191432925787127657646.1; 3AB9D23F7A4B3CSS=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; _gia_d=1; wlfstk_smdl=1xb7enofhq9sqf13z9xjotv6hf00xlbz; __jdu=1739453919139976805723; TrackID=1Zzd-GkfUlyDqjmcZWjHjgczRoC9L60NsRJ6-ZlvEgm68MP3qJshzfu5z8HyE3yRuAq_Jan_ErezF4CWTr65ZRzQQnsy1rMQ6v5330enR6C0; thor=FFC264252E62EA92743718F58BA29C5390A41E9E586F68CAE937C2C9B05C2CDDBC280325E77EA703138256622A7A183B15F1D5850F96B8F51E4C47D623B57DF866D71D0B6DFEB0A61E9A7D76B2FF155D9CD7507AE856F1EC66F7030317B1BBF09707BB45FC9E2975F5968EA5FE0FB50AC7407B872427BBDD845AC0AF50EDF41E0705071AE5664C56F4BE53F4E3411E61; light_key=AASBKE7rOxgWQziEhC_QY6ya54jGyyTei2jv23F8b42VWqH08p-doi172z1ZCfVEqW2u24jM; pinId=jsSpVomLMkB4-qPS9PNQiQ; pin=18500425520_p; unick=jd185004lts; ceshi3.com=000; _tp=bQoH%2FMqFIumGj5jZ0Q0qXg%3D%3D; _pst=18500425520_p; ipLoc-djd=13-1000-0-0; __jda=29846306.1739453919139976805723.1739453919.1739453919.1739453919.1; __jdc=29846306; jsavif=1; jsavif=1; xapieid=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; __jdb=29846306.4.1739453919139976805723|1.1739453919; flash=3_jrLxBytlxd7Thers8YtUAL1ocpdtHYZjh5viSWCAmYG-jm4xGQahDmGqMaHma2Wd-a6bj5edTvUV2H6hGUnxeoSznWpnHRH-3KKF87XbdauRwbFF6uBsjzyisaHhdy-npBbhnfdA0jE6QWwXm7rnh_jgEx4Wgok37sOFCXl3ZiZijcCKRq**; shshshfpa=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; shshshfpx=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; areaId=13; shshshfpb=BApXSWGWA_PFAJ_JvOXyU27PmrMe8mnRbBnsEPn5o9xJ1Mr3NsIG2; 3AB9D23F7A4B3C9B=H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4U',

        }
    # def filter

    def parse(self, response):
        # print(response.text)
        # 解析商品列表
        for product in response.css('li.gl-item'):
            try:

                link=product.css('div.p-name a::attr(href)').get().strip()
                self.goods["sku"]=link.split("/")[-1].split(".")[-2]
                self.goods=Detail(heads=self.get_headers).spider(self.goods["sku"])
                self.goods["price"] = product.css('div.p-price i::text').get().strip()
                with open("goods_list.json","a+") as f:
                    f.write(json.dumps(self.goods)+"\n")
                yield self.goods
            except Exception as e:
                pass