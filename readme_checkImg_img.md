"识别验证码,使用cookie登录系统"
1、安装模块selenium、PIL、pytesseract、requests
2、Tesseract-OCR

实现方法：
1、将页面截图保存，将验证码放大
2、通过pytesseract模块和OCR工具识别验证码，等到页面的cookie
3、更新cookie使得页面能够保持登录状态
4、进行后续的接口操作