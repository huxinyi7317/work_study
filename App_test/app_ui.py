from appium import webdriver
from appiumtools import find_element,is_element_cunzai
from time import sleep

#雷电模拟器
desired_caps = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "LIO-AN00",
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.TBMainActivity",
  "unicodeKeyboard": True,
  "resetKeyboard": True,
  "noReset": True
}
#iQOO
desired_caps1 = {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "4710a707",
  "appPackage": "com.taobao.taobao",
  "unicodeKeyboard": True,
  "resetKeyboard": True,
  "noReset": True,
  "appActivity": "com.taobao.tao.TBMainActivity"
}
# desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
# desired_caps['platformVersion'] = '5.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
# desired_caps['deviceName'] = 'MI 4LTE'                      # 手机/模拟器的型号：adb shell getprop ro.product.model
# desired_caps['appPackage'] = 'com.tencent.mobileqq'               # app的名字：
#                                                         # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
#                                                         # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
# desired_caps['appActivity'] = '.activity.SplashActivity'              # 同上↑
# desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
# desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# desired_caps['noReset'] = True                        # 使用app缓存
def wan_cheng_ren_wu(driver,locator,timeout):
    ''' 
        外部提供需要执行滑动动作的入口信息
        滑动屏幕，driver == '手机驱动
        locator == ('xpath','xpath定位脚本')
        timeout == '定位入口元素的等待时间'
    '''
    asser,elem = is_element_cunzai(driver,locator,timeout)
    if asser:
        elem.click()
        #获取屏幕的高
        i = 0
        while i < 16:
            sleep(2)
            x = driver.get_window_size()['width']
            # 获取屏幕宽
            y = driver.get_window_size()['height']
            #滑动屏幕
            driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/4*y, 2000)
            sleep(1)
            i += 1
            driver.back()
    return

def taobao_12(config_caps):
    #参数是链接手机的配置，这是淘宝自动做任务领取币脚本，请先登录淘宝账号
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config_caps)
    #进入双十二红包活动
    # asser,elem = is_element_cunzai(driver,('xpath','//android.widget.FrameLayout[@content-desc="互动城"]/android.widget.FrameLayout[1]/android.widget.ImageView'),10)
    sleep(3)
    if True:
        #固定坐标点击进入
        driver.tap([(770,1090)])
        # elem.click()
    else:
        print('元素没有找到')
    #签到领红包
    sleep(5)
    asser,elem = is_element_cunzai(driver,('xpath','//android.webkit.WebView[@content-desc="金币小镇双12欢乐造红包"]/android.app.Dialog/android.widget.Button[4]'),10)
    if asser:
        elem.click()
    print('已签到')
    try:
        find_element(driver,locator=('aid','立即领取欢乐币')).click()
        find_element(driver,locator=('aid','领欢乐币')).click()
    except:
        print('元素定位失败')
    #检查是否可点击
    asser,elem = is_element_cunzai(driver,('aid','去打卡'),3)

    if asser:
        elem.click()
    print('已打卡')
    asser,elem = is_element_cunzai(driver,('content-desc','去完成'),2)
    #查找是否有任务需要去完成
    while asser:
        if asser:
            elem.click()
            driver.implicitly_wait(10)
            #页面停留时间
            sleep(18)
            driver.back()

    #领取任务奖励
    asser,elem = is_element_cunzai(driver,('aid','立即领取'),2)
    #存在就领取
    while asser:
        elem.click()
        print('领取红包')
    driver.back()
    #升级
    while True:
        asser,elem = is_element_cunzai(driver,('text','升级领红包'),2)
        if asser:
            elem.click()
        else:
            break
    print('今日任务已完成')
    driver.close_app()   


if __name__ == "__main__":
    taobao_12(desired_caps)