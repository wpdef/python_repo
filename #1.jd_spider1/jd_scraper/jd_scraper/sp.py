#!/usr/bin/python3
## -*- coding: utf-8 -*-
import requests,re,urllib3
import lxml.etree as etree
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import random
import os
import collections


class Detail:
    """"""
    def __init__(self,heads=None,m_heads=None):
        self.heads = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Cookie': '__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1739453919140; mba_muid=1739453919139976805723; mba_sid=17394539191432925787127657646.1; 3AB9D23F7A4B3CSS=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; _gia_d=1; wlfstk_smdl=1xb7enofhq9sqf13z9xjotv6hf00xlbz; __jdu=1739453919139976805723; TrackID=1Zzd-GkfUlyDqjmcZWjHjgczRoC9L60NsRJ6-ZlvEgm68MP3qJshzfu5z8HyE3yRuAq_Jan_ErezF4CWTr65ZRzQQnsy1rMQ6v5330enR6C0; thor=FFC264252E62EA92743718F58BA29C5390A41E9E586F68CAE937C2C9B05C2CDDBC280325E77EA703138256622A7A183B15F1D5850F96B8F51E4C47D623B57DF866D71D0B6DFEB0A61E9A7D76B2FF155D9CD7507AE856F1EC66F7030317B1BBF09707BB45FC9E2975F5968EA5FE0FB50AC7407B872427BBDD845AC0AF50EDF41E0705071AE5664C56F4BE53F4E3411E61; light_key=AASBKE7rOxgWQziEhC_QY6ya54jGyyTei2jv23F8b42VWqH08p-doi172z1ZCfVEqW2u24jM; pinId=jsSpVomLMkB4-qPS9PNQiQ; pin=18500425520_p; unick=jd185004lts; ceshi3.com=000; _tp=bQoH%2FMqFIumGj5jZ0Q0qXg%3D%3D; _pst=18500425520_p; ipLoc-djd=13-1000-0-0; __jda=29846306.1739453919139976805723.1739453919.1739453919.1739453919.1; __jdc=29846306; jsavif=1; jsavif=1; xapieid=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; __jdb=29846306.4.1739453919139976805723|1.1739453919; flash=3_jrLxBytlxd7Thers8YtUAL1ocpdtHYZjh5viSWCAmYG-jm4xGQahDmGqMaHma2Wd-a6bj5edTvUV2H6hGUnxeoSznWpnHRH-3KKF87XbdauRwbFF6uBsjzyisaHhdy-npBbhnfdA0jE6QWwXm7rnh_jgEx4Wgok37sOFCXl3ZiZijcCKRq**; shshshfpa=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; shshshfpx=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; areaId=13; shshshfpb=BApXSWGWA_PFAJ_JvOXyU27PmrMe8mnRbBnsEPn5o9xJ1Mr3NsIG2; 3AB9D23F7A4B3C9B=H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4U',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
        }

        self.prices_url="https://api.m.jd.com/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&h5st=20231101105016293%3Bmz5int6gzmmmzz06%3Bfb5df%3Btk03wd6db1d0a18nnce9jvRqnKTiubw4lF_pg9mKgG8JX6txc0V7zKjfS0HfTzB4kJJ1yFVShA4RflzavcHGmR_sfcDH%3B893d0425e9bf8e3c806f71ce0a6d0208%3B4.1%3B1698807016293%3Bee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980b96c3953b1ab788029ae792b39e1131e375f9c8031d24338c00a6fe1fcfd4cd432b01360ceb18967e74ff3397ef481855ad96c1e570ffd9c695d8d8240b967ec5675759122318026b316938f7dcf59ca154ec8e6df06f5772321584b0cb23b5f57aab84eb0e0042b13512aa09c13d556be8b115a7732366e8f12ab611ddd4d745eaeb035ddcf8dea974cf41f4fa6c64bc884949559d1e9d8657456401f43b692cccc4b08aa0f441eca6d4cb48ec465a4408d503bcd263e757f498482bbe5bf9fc59c431485b1dfbdf15205ad9bf46807d8686630402cb4c07db6972ba0462a&t={}228&body=%7B%22skuId%22%3A{}%2C%22area%22%3A%221_72_55653_0%22%2C%22num%22%3A1%7D"
        self.goods_url = "https://item.jd.com/{}.html"
        self.detail_url = "https://cd.jd.com/description/channel?skuId={}&mainSkuId={}&charset=utf-8&cdn=2&callback=showdesc"
        self.d_url="https://api.m.jd.com/description/channel?appid=item-v3&functionId=pc_description_channel&skuId={}&mainSkuId={}&charset=utf-8&cdn=2"
        # 代理配置
        self.tunnel = "p249.kdltps.com:15818"
        username = "t19094506387534"
        password = "cgbbgcym"
        self.proxies1 = self.proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": self.tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": self.tunnel}
        }
        self.proxies=None


    def downloadimg(self,img_url):
        """图片资源下载"""
        img_url=re.sub(r'(.*).360buyimg.com/(.*)/(.*)jfs/', "http://img10.360buyimg.com/sku/jfs/", img_url)
        img_url=re.sub(r'(.*).360buyimg.com', "http://img10.360buyimg.com", img_url)
        if "/jfs/t" not in img_url or "43be1ddda653909e" in img_url or "9c41048fa27fe51b" in img_url or "7fe0b65a239d3adc" in img_url or "77dde360806a1a49" in img_url or "c5a090bec8b20830" in img_url or "14779af55b43ae93" in img_url or "cbb2df46c9cdf20d" in img_url or "33a40a1a92171f82" in img_url or "0b6713542f4c0434" in img_url or "03ec9112206b5341" in img_url or "de7cfed7c36247b1" in img_url  or "12ce4877587a7806" in img_url:
            return ""
        else:
            return img_url.replace(".avif","").replace("/n5/","/sku/")

    def spider(self,sku):
        """数据获取"""
        if "http" in sku:
            filename = os.path.basename(sku)
            sku=filename.split(".")[0]
        goods = dict()
        #商品页html代码
        res = requests.get(self.goods_url.format(sku),headers=self.heads,verify=False, proxies=self.proxies)
        html = res.text
        tree = etree.HTML(html)
        # 商品标题
        title = tree.xpath("/html/body/div[6]/div/div[2]/div[1]//text()")
        if not title:
            title = tree.xpath("//div[@class='sku-name']//text()")
        for item in title:
            if item.strip():
                title = item.strip()
        goods['title'] = title
        imgs = tree.xpath("//*[@id='spec-list']/ul/li/img/@src")
        ware = tree.xpath("//*[@id='detail']/div[2]/div[2]/div[2]/p//text()")
        # 商品包装
        goods['ware'] = ware[0] if ware else ""

        #获取品牌
        brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-5']//text()")
        if not brand:
            brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-4']//text()")
        elif not brand:
            brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-3']//text()")
        elif not brand:
            brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-2']//text()")
        elif not brand:
            brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-1']//text()")
        elif not brand:
            brand = tree.xpath("//*[@clstag='shangpin|keycount|product|mbNav-0']//text()")
        if brand:
            brand = brand[0].replace(" ","")
        #获取型号
        model=""
        model1 = tree.xpath("//*[@id='crumb-wrap']/div/div[1]/div[9]//text()")
        brand1=brand
        goods["p_link"] = "https://item.jd.com/%s.html"%sku
        goods["jd_sn"] = sku
        goods['en_brand'] =""
        if "（" in brand:
            brand1 = brand.split("（")
            if len(brand1)>1:
                zh_brand = brand1[1].replace("）","")
                goods['zh_brand'] = zh_brand.replace(" ","")
            zh_brand = brand1[0]
        else:
            zh_brand = brand1
        try:
            if zh_brand and isinstance(zh_brand,list):
                goods['zh_brand'] = zh_brand[0].replace(" ","")
            else:
                goods['zh_brand'] = zh_brand.replace(" ","")
        except Exception as e:
            goods['zh_brand']=""
        try:
            if not model:
                model = model1[0].replace(goods['zh_brand'],"").replace(goods['en_brand'],"")
            goods["model"] = model.replace(" ","").replace("\r","").replace("\n","")
        except Exception as e:
            goods["model"] =""
        try:
            if not goods["model"]:
                model = tree.xpath('//*[@id="crumb-wrap"]/div/div[1]/div[@class="item ellipsis"]//text()')
                model = model[0].replace(goods['zh_brand'],"").replace(goods['zh_brand'],"")
            goods["model"] = model.replace(" ","").replace("\r","").replace("\n","").replace("（","").replace("）","")
        except Exception as e:
            goods["model"]=""
        parameter_list = tree.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[@class="parameter2 p-parameter-list"]/li//text()')
        attrs_dict = collections.OrderedDict()
        for parameter in parameter_list:
            param = parameter.split("：")
            if ("商品编号" not in param[0]) and ("店铺" not in param[0]):
                if len(param)>1:
                    attrs_dict[param[0]]=param[1]
        attrs = tree.xpath("//*[@id='detail']/div/div/div/div[@class='Ptable-item']")
        for item1 in attrs:
            attr = item1.xpath('dl/dl[@class="clearfix"]')
            for item in attr:
                attrname = item.xpath("dt//text()")
                attrvalue = item.xpath("dd//text()")
                attrs_dict[attrname[0].strip()] = attrvalue[-1].strip()
        goods['image_url'] = list()
        #获取相册图片
        for img in imgs:
            rimg = self.downloadimg(img)
            if rimg:
                goods['image_url'].append(rimg)
        mainskuids = re.findall(r'mainSkuId:.\d+', html)[0].split(":'")
        print(mainskuids)
        mainskuid=mainskuids[1]

        # 获取详情
        detail1 = requests.get(self.d_url.format(sku, mainskuid), headers=self.heads)

        datail_imgs = list()
        if "jpg" in detail1.text or "png" in detail1.text or "gif" in detail1.text:
            detail1_json = json.loads(detail1.text)
            s = re.compile(r'(//img.*?(\.jpg|\.png|\.jpeg|\.gif|\.avif))')
            detail_html = detail1_json["content"]
            datail_imgs = re.findall(s, detail_html)
            datail_imgs = [self.downloadimg(img[0]) for img in datail_imgs]
        if not detail1.text:
            detail1 = requests.get("https://sku-market-gw.jd.com/css/pc/%s.css?t=1715582968935"%mainskuid)
            if "jpg" in detail1.text or "png" in detail1.text or "gif" in detail1.text:
                s = re.compile(r'(//img.*?(\.jpg|\.png|\.jpeg|\.gif|\.avif))')
                datail_imgs = re.findall(s, detail1.text)
                datail_imgs = [self.downloadimg(img[0]) for img in datail_imgs]
        goods['detail'] = datail_imgs
        goods['attrs'] = attrs_dict
        if not goods["title"] and not goods["en_brand"] and not goods["zh_brand"] and not goods["model"]:
            detail = requests.get("https://i-item.jd.com/%s.html" % sku, verify=False,
                                  proxies=self.proxies)
            html = detail.text
            s = re.compile(r'name: \'(.*\'),')
            name = re.findall(s, html)
            if name:
                goods["title"] = name[0].replace("\'","")
                tree = etree.HTML(html)
                brand = tree.xpath("/html/body/div[5]/div/div[1]/div[7]/a//text()")
                # image_url=tree.xpath("[@class='spec-list']//@src")
                image_url = [self.downloadimg(img) for img in tree.xpath("//*[@id='spec-list']//img/@src") if self.downloadimg(img)]
                goods["image_url"] = image_url
                if brand:
                    goods['en_brand']=brand[0]
        return goods

if __name__ == '__main__':
    jd_spider = Detail()
    # jd = JD()
    goods = jd_spider.spider("https://item.jd.com/100108291797.html#crumb-wrap")
    print(json.dumps(goods))