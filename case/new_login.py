#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from PIL import Image,ImageEnhance
import pytesseract
import requests


def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login.png')  #截取登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgElement = driver.find_element_by_id('checkImg_img')
    imgLocation = imgElement.location #获取验证码元素坐标
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    login = Image.open("login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('authcode.png')
    authcodeImg = Image.open('authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).replace(' ', '')
    return authCodeText

def pandarola_login(account='admin',passwd='Admin123',url="http://120.78.168.211/m4m/admin/index.jsp"):
    '''登录系统'''
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    cookies1=driver.get_cookies()
    print(cookies1)
    imgElement = driver.find_element_by_id('checkImg_img')
    authCodeText = get_auth_code(driver,imgElement)
    driver.find_element_by_xpath("//input[@name='account']").clear()
    driver.find_element_by_xpath("//input[@name='account']").send_keys(account)
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(passwd)
    driver.find_element_by_xpath("//input[@id='checkImg']").send_keys(authCodeText)
    # time.sleep(2)
    driver.find_element_by_id("login-btn").click()
    time.sleep(2)
    cookies2=driver.get_cookies()
    print(cookies2)
    text=driver.title
    driver.quit()
    if text=="M4M云管理平台-云端管理":
    # driver.quit()
        print('登录成功')
        return cookies2
    else:
        print("登录失败")


def add_cookies(s,cookies=pandarola_login()):
    '''往session添加cookies'''
    try:
        # 添加cookies到CookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"], i['value'])
        s.cookies.update(c)  # 更新session里cookies
        print(s.cookies)
    except Exception as msg:
        print(u"添加cookies的时候报错了：%s" % str(msg))

# def aa():
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
#     }
#     url="http://120.78.168.211/m4m/admin/system/userModule.jsp"
#     k=a.get(url=url,headers=headers)
#     print(k.content)



if __name__=="__main__":
    s = requests.session()
    add_cookies(s=s)
    # aa()