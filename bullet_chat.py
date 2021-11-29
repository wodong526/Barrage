#coding:gbk
#*******************************************
#����: �Җ|
#mail:wodong526@dingtalk.com
#time:2021/11/28
#�汾��V1.0
#******************************************

from PySide2.QtCore import Qt, QPoint, QParallelAnimationGroup, QEasingCurve, QPropertyAnimation
from PySide2.QtGui import QFont, QMovie
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication

gif_path = r''      #gif·��������gif����
text = u''          #��Ļ����

class barrageWindow(QWidget):
    def __init__(self):
        super(barrageWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)#���ô���Ϊ�ޱ߿򴰿����ڴ�����ǰ����ʾ
        self.setAttribute(Qt.WA_TranslucentBackground, True)               #���ô�������Ϊ����͸��

        self.label_aim = QLabel(self)                                      #����ؼ�������ʾ�ı���ͼ�񡢶���
        self.label_tex = QLabel(self)

        self.main_layout = QHBoxLayout(self)                               #���ɺ᲼��
        self.main_layout.addWidget(self.label_aim)
        self.main_layout.addWidget(self.label_tex)

        self.desktop = QApplication.instance().desktop()                   #���ƻ�ȡ������ʾ���������׵Ĵ����鷳�̽���^_^��

        self.setText(text)
        self.setAim(gif_path)

    def setText(self, tex):
        self.Font_obj = QFont(u"΢���ź�", 30)
        self.label_tex.setText(tex)
        self.label_tex.setFont(self.Font_obj)
        self.label_tex.setStyleSheet('color:rgb(255, 255, 0)')

    def setAim(self, aimPath):
        self.movie_obj = QMovie('{}'.format(aimPath))
        self.label_aim.setMovie(self.movie_obj)
        self.movie_obj.start()

    def initAim(self, start, end):
        prop_aim = QPropertyAnimation(self, 'pos')#���ö���
        prop_aim.setStartValue(start)
        prop_aim.setEndValue(end)

        prop_aim.setEasingCurve(QEasingCurve.OutInCubic)#���ٶȱ仯��ʽ��������ʽ�μ�https://doc.bccnsoft.com/docs/PyQt4/qeasingcurve.html#Type-enum

        prop_aim.setDuration(20000)                     #����ʱ������λ��΢��

        self.aim_grp = QParallelAnimationGroup(self)    #����һ�������飬���Լ��������ؼ�
        self.aim_grp.addAnimation((prop_aim))           #������������ڷ��붯����
        self.aim_grp.finished.connect(self.stop)        #���źźͲ�����
        self.aim_grp.start()                            #�����鿪ʼ����

    def stop(self):
        self.aim_grp.stop()#������ֹͣ
        self.movie_obj.setFileName('')#����һ���ն������ͷ�֮ǰ��gifռ��
        self.close()       #���ڹر�

    def run(self):
        super(barrageWindow, self).show()
        start_poistion = QPoint(self.desktop.screenGeometry().width(), 100)#��Ļ�����ĳ�ʼλ�ã�������ʾ����Ŀ����أ� �������µ�100�����أ�
        end_poistion = QPoint(-500, 100)                                   #��Ļ�Ľ���λ��
        self.move(start_poistion)                                          #�ƶ����ڵ���ʼλ��
        self.initAim(start_poistion, end_poistion)

a = barrageWindow()
a.run()

