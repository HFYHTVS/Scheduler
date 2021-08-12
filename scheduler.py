'''-*-coding:utf-8-*-'''
scheduler_version = "2.1 [release]"
'''
Project 丨 日程规划表
update_date = 2021-3-21   
__author__  = HFYHTVS   [-EMAIL-]: fanyihang051201@163.com
copyright©PTG_STUDIO 2021
'''
try:
    import datetime  # 导入获取系统时间的datetime
    import os
    import random
    import sys
    import threading  # 导入线程库
    import time  # 导入time库
    import webbrowser
    import json
    from PySide2.QtCore import *  # 导入QT运行核心
    from PySide2.QtGui import *  # 导入QT Gui
    from PySide2.QtMultimedia import QSound  # 导入QT音频驱动
    from PySide2.QtWebEngineWidgets import QWebEngineView  # 导入QT(Pyside2) Web 视图引擎
    from PySide2.QtWidgets import *  # 导入QT窗体控件列表
    from ui_scheduler import Ui_Scheduler  # 导入UI文件的ui类，继承它
    from ui_newplan import Ui_Newplan
    from toast import Toast
    # from matplotlib import *
    # from pyecharts.charts import Pie                  # 导入Python echarts model['Pie']
except:
    raise ImportError('- can\'t import package mobels. PLEASE WATCH SOURCE CODE OR ASK FOR HELP...')
""" LOGGER
子窗体弹出实现{
    相应的个性化设置
}
pyecharts报表的生成{
    Pie
    bar
    point
    ...
}
"""




# 新建对象scheduler 继承QT ui显示模块 以及Ui文件的显示类
class scheduler(QMainWindow, Ui_Scheduler):    #MainClass
    def __init__(self):                                 # 初始化对象
        super().__init__()
        self.setupUi(self)                              # 调用Ui文件的setupUi()方法初始化
        self.setup_media = QSound('media/setup.wav')
        self.setup_media.play()
        self.setup()
        self.setupStyle()  # 初始个性化设置[bgc,media]
        self.setup_button_style()
        self.tray = tray()
        self.show()         # show方法显示窗体

    def setup(self):
        self.pbtn_plan.clicked.connect(self.plan)
        with open('data.json','r')as f:
            self.data = json.load(f)
            print(self.data)
        pass
        # main
        # self.pbtn_background.clicked.connect(self.changeBackground)

    def setupStyle(self):
        #window title
        self.setWindowTitle(f'日程规划表 丨Scheduler丨{scheduler_version}')
        #media
        self.click_media = QSound('media/click')
        #icon
        self.icon = QIcon("icon/timerLogo.png")
        self.setWindowIcon(self.icon)  # set window's icon
        # self.setIcon(self.icon)
        title_img = QPixmap('icon/iconTitle.png').scaled(170, 80)
        # self.lb_title.setScaledContents(True)
        self.lb_title.setPixmap(title_img)
        #mouse
        self.set_mouse('icon/iconMouse.png', size=4)
        #bkg
        self.bkg = 'background/Grade Grey.jpg'
        # self.lb_plate.setPixmap(QPixmap('icon/bkg.jpeg'))
        # self.lb_plate.setScaledContents(True)
        self.lb_background.setPixmap(QPixmap(self.bkg))
        # lb_plate
        plt_img = QPixmap('icon/iconPlate3.png')
        self.lb_plate.setPixmap(plt_img)
        #lb_note
        self.lb_note.setText(f'日程规划表\nScheduler\n版本\n{scheduler_version}\nHFYHTVS')

    def setup_button_style(self):
        '''pbtn_plan'''
        self.pbtn_plan.setIcon(QIcon('icon\iconNewplan.png'))
        self.pbtn_plan.setIconSize(QSize(160,80))
        '''pbtn_settings'''
        self.pbtn_settings.setIcon(QIcon('icon\iconSettings.png'))
        self.pbtn_settings.setIconSize(QSize(160, 80))
        '''pbtn_charts'''
        self.pbtn_charts.setIcon(QIcon('icon\iconCharts.png'))
        self.pbtn_charts.setIconSize(QSize(160, 80))
        '''pbtn_clear'''
        self.pbtn_clear.setIcon(QIcon('icon\iconClear.png'))
        self.pbtn_clear.setIconSize(QSize(160, 80))
        '''pbtn_personal'''
        self.pbtn_personal.setIcon(QIcon('icon\iconSettings.png'))
        self.pbtn_personal.setIconSize(QSize(160, 80))




    def set_mouse(self, img, size=int):
        mouseImage = QPixmap(img)
        mouseImage = mouseImage.scaled(7*size, 8*size)  # 比例 7:8
        cursor = QCursor(mouseImage, 5, 15)
        self.setCursor(cursor)

    def file_name(self, file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.jpg':
                    L.append(os.path.join(root, file))
        return L


    def changeBackground(self):
        self.setup_media.play()
        background_img = QPixmap(random.choice(self.file_name('background')))
        self.lb_background.setPixmap(background_img)

    def ring(self):
        ringdata = random.choice(self.file_name('media'))
        if k[:4] == 'Ring':
            ring_media = QSound(ringdata)
            ring_media.play()
        else:
            self.ring()

    def menuBar(self):
        pass

    def plan(self):
        self.newplan = newplan()
        self.newplan.show()
        self.newplan.lb_background.setPixmap(QPixmap(self.bkg))
        self.newplan.pbtn_yes.clicked.connect(self.note)
    
    def note(self):
        if self.newplan.textEdit.toPlainText():
            #[计划名称,计划开始时间,计划结束时间]
            self.plan_content = [self.newplan.textEdit.toPlainText(), self.newplan.dte1.text(),
            self.newplan.dte2.text(),]
            with open('data.json', 'w')as f:
                f.write(json.dumps(self.plan_content))
            self.newplan.c()
        else:
            QMessageBox.warning(self.newplan,'WARNING','您还没有输入计划的内容.')
            pass
        self.lb_note.setText(f"当前计划\n{self.plan_content[0]}")


    def time_cut():
        print(self.newplan.dte2.text())

# 类 newplan  设置新计划的窗口
class newplan(QMainWindow, Ui_Newplan):
    def __init__(self):                                 # 初始化对象
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("= 设置新计划 =")
        self.setup()
        
    def setup(self):
        '''pbtn_plan'''
        self.lb_newplan.setPixmap(QPixmap('icon\iconNewplan.png'))
        self.time_add_value = 3600 #每次添加3600s = 1h  （间隔的时间）
        time = QTime.currentTime()
        date = QDateTime.currentDateTime().date()
        self.dte1.setDate(date)
        self.dte1.setTime(time)
        self.dte2.setDate(date)
        self.dte2.setTime(time.addSecs(self.time_add_value))

    def c(self):
        Toast(name=self.textEdit.toPlainText(), t1=self.dte1.text(),
            t2=self.dte2.text())
        self.close()
# 类 tray 托盘图标相关设置等.
class tray(QSystemTrayIcon, scheduler):
    def __init__(self):
        super().__init__()
        self.show()
        self.setup()

    def setup(self):
        self.systime = str(datetime.datetime.now())[:16]
        m = QIcon('icon/gifLogo.gif')
        self.setIcon(m)
        self.infoShowed = f'当前时间{self.systime}'
        self.is_window_show = '隐藏'
        self.add_menu()
        self.icon_index = 0
        self.timer = QTimer()
        self.change_icon()

    def add_menu(self):
        self.menu = QMenu()
        self.menu.clear()
        #tiggered参数可以不填，显示信息作用
        # QAction对象输入一个功能选项的对象 参数['功能选项上面显示的文字&符号','图标对象','传入要激活功能选项(要实现的函数)']
        information = QAction(self.infoShowed, self)
        whether = QAction(f'{self.is_window_show}窗口',
                          self, triggered=self.show_or_hide)
        quit = QAction('退出', self, triggered=self.quit)
        # action4 = QAction('', self, triggered=)
        #加入这个功能到menu菜单中
        #顺序由添加顺序决定 , 自上而下
        self.menu.addAction(information)
        self.menu.addAction(whether)
        self.menu.addAction(quit)
        # self.menu.addAction(action4)
        #把menu传入系统托盘当中
        self.setContextMenu(self.menu)

    def change_icon(self):
        self.tray_icon = QIcon(f'icon/gif/{self.icon_index % 60}.png')
        self.setIcon(self.tray_icon)
        self.icon_index += 1
        self.timer.singleShot(100, self.change_icon)

    def quit(self):
        scheduler.hide(window)
        self.hide()
        sys.exit()

    def show_or_hide(self):
        if self.is_window_show == '隐藏':
            self.is_window_show = '显示'
            scheduler.hide(window)
        elif self.is_window_show == '显示':
            self.is_window_show = '隐藏'
            scheduler.show(window)
        self.add_menu()

class Pie():
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = scheduler()
    print("- window-show-successful")
    sys.exit(app.exec_())
