# encoding:utf-8
import csv
import os
from time import sleep
import time


class App(object):
    def __init__(self):
        self.result = ""
        self.startTime = 0

    # 启动app
    def luanchApp(self):
        cmd = "adb shell am start -W -n com.yida.cloud.client.party/.SplashActivity"
        self.result = os.popen(cmd)

    # 关闭app
    def stopApp(self):
        cmd = "adb shell am force-stop com.yida.cloud.client.party"
        os.popen(cmd)

    # 去获取 启动时间
    def getLuanchTime(self):
        for line in self.result.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
        return self.startTime


class Controller(object):
    def __init__(self):
        # 创建对像
        self.app = App()
        # 保存测试结果
        self.allData = [("testTime", "lunchTime")]
        # 总测试次数
        self.testCount = 2

    # 开始测试
    def startProcess(self):
        # 启动app
        self.app.luanchApp()
        # 启动耗时
        cultTime = self.app.getLuanchTime()
        # 当前时间
        currentTime = self.getCurrentTime()
        # 保存时间
        self.allData.append((currentTime, cultTime))
        # 睡眠一下
        sleep(5)
        # 停止app
        self.app.stopApp()
        sleep(5)

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime("%Y-%m-%d %H:%M%S", time.localtime())

    # 开始运行
    def run(self):
        while self.testCount > 0:
            self.startProcess()
            self.testCount -= 1
        self.saveTestResult()

    def saveTestResult(self):
        csvFile = file("startTimeResult.csv", "wb")
        writer = csv.writer(csvFile)
        writer.writerows(self.allData)
        csvFile.close()


if __name__ == "__main__":
    controller = Controller()
    controller.run()
