# encoding:utf-8
# 监测cpu信息
import csv
import os
import time
from time import sleep


class CpuInfoController(object):
    def __init__(self, count, sleetTime):
        # 命令结果
        self.mCmdResult = ""
        self.count = count
        self.sleetTime = sleetTime
        self.mAllResult = [("timeTemp", "cpu result")]

    def startCmd(self):
        print("------------begin execute cmd----------")
        cmd = "adb shell dumpsys cpuinfo | grep com.yida.cloud.client.party"
        self.mCmdResult = os.popen(cmd)
        self.mAllResult.append((self.getCurrentTme(), self.mCmdResult.readlines()))
        print("------------execute cmd end,result:----------")
        print(self.mCmdResult.readlines())

    def getCurrentTme(self):
        return time.strftime("%Y-%m-%d %H:%M%S", time.localtime())

    def startTestProcess(self):
        print("----------start test process------------")
        while self.count > 0:
            print("-----------testing-----------")
            self.startCmd()
            sleep(self.sleetTime)
            self.count -= 1
        self.saveData()

    def saveData(self):
        print("-----------begin save data-----------")
        csvFile = file("cpu_test_result.csv", "wb")
        writer = csv.writer(csvFile)
        writer.writerows(self.mAllResult)
        csvFile.close()
        print("-----------save data success-----------")


if __name__ == "__main__":
    CpuInfoController(10, 1).startTestProcess()
