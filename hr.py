from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import pexpect
class HeartRate(QObject):
    HRpacketCapture = pyqtSignal(int)
    def __init__(self):
        super(HeartRate, self).__init__()    
        self.batterylevel = 0
        self.retry = True
        
    def captureHR(self):
        self.retry = True        
        self.gt.sendline("char-write-req 0x0011 0100")
        period = 1.
        last_measure = time.time() - period
        hr_expect = "Notification handle = 0x0010 value: ([0-9a-f ]+)"
        while True:
            try:
                self.gt.expect(hr_expect, timeout=10)

            except pexpect.TIMEOUT:
                # If the timer expires, it means that we have lost the
                # connection with the HR monitor
                print("Connection lost with. Reconnecting.")
                self.gt.sendline("quit")
                try:
                    self.gt.wait()
                except:
                    pass
                time.sleep(1)
                break

            except KeyboardInterrupt:
                print("Received keyboard interrupt. Quitting cleanly.")
                retry = False
                break

            # We measure here the time between two measures. As the sensor
            # sometimes sends a small burst, we have a simple low-pass filter
            # to smooth the measure.
            tmeasure = time.time()
            period = period + 1 / 16. * ((tmeasure - last_measure) - period)
            last_measure = tmeasure

            # Get data from gatttool
            datahex = self.gt.match.group(1).strip()
            data = map(lambda x: int(x, 16), datahex.split(b' '))
            res = self.interpret(list(data))
            # print(res)
            self.HRpacketCapture.emit(int(res['hr']))
            QThread.msleep(40)
    def startHR(self):
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.captureHR)
        self.thread.start()
        
        # self.thread = QThread()
        # self.moveToThread(self.thread)
        # self.thread.started.connect(self.readHR)
        # self.thread.start()
    def interpret(self, data):
        """
        data is a list of integers corresponding to readings from the BLE HR monitor
        """

        byte0 = data[0]
        res = {}
        res["hrv_uint8"] = (byte0 & 1) == 0
        sensor_contact = (byte0 >> 1) & 3
        if sensor_contact == 2:
            res["sensor_contact"] = "No contact detected"
        elif sensor_contact == 3:
            res["sensor_contact"] = "Contact detected"
        else:
            res["sensor_contact"] = "Sensor contact not supported"
        res["ee_status"] = ((byte0 >> 3) & 1) == 1
        res["rr_interval"] = ((byte0 >> 4) & 1) == 1

        if res["hrv_uint8"]:
            res["hr"] = data[1]
            i = 2
        else:
            res["hr"] = (data[2] << 8) | data[1]
            i = 3

        if res["ee_status"]:
            res["ee"] = (data[i + 1] << 8) | data[i]
            i += 2

        if res["rr_interval"]:
            res["rr"] = []
            while i < len(data):
                # Note: Need to divide the value by 1024 to get in seconds
                res["rr"].append((data[i + 1] << 8) | data[i])
                i += 2
        return res;        
        

    def stopHR(self):
        self.gt.sendline("quit")
        self.gt.wait()
    def batteryLevel(self):
        self.gt.sendline("char-read-uuid 00002a19-0000-1000-8000-00805f9b34fb")
        try:
            self.gt.expect("value: ([0-9a-f]+)")
            battery_level = self.gt.match.group(1)
            self.battery_level = int(battery_level, 16)
            print("Battery level: " + str(self.battery_level))

        except pexpect.TIMEOUT:
            print("Couldn't read battery level.")

    def connect(self):
        while self.retry:

            self.gt = pexpect.spawn('gatttool -b EE:D3:5A:86:87:65 -t random --interactive')
            self.gt.expect(r"\[LE\]")
            self.gt.sendline("connect")
            try:
                i = self.gt.expect(["Connection successful.", r"\[CON\]"], timeout=100)
                print(i)
                if i == 0:
                    self.gt.expect(r"\[LE\]>", timeout=100)
                    self.retry = False
            except pexpect.TIMEOUT:
                print("Connection timeout. Retrying.")
        
        print('connected')