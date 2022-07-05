# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import robots
import time
import mw

class RobotsClass(QtWidgets.QMainWindow, mw.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)  # Для инициализации дизайна

		# вставляем иконку
		self.label_for_image.setPixmap(pixmap)
		self.setWindowIcon(QIcon('robots.ico'))

		# connect
		self.pbURL_1.clicked.connect(self.url_1)
		self.pbSucces_2.clicked.connect(self.Succes_2)
		self.pbSite_3.clicked.connect(self.site)

	def url_1(self):
		url = self.URL_string.text()
		self.Print_SuccesRequest.setText("")
		self.Error_string.setText("")
		self.Print_Requests.setText("")
		self.PrintHTTP.setText("")
		self.Time_work.setText("")
		self.Search_Site.setText("")

		global pathlist
		global CodeError

		t1 = time.time()
		salida, Exept, pathlist, CodeError = robots.conn_check(url, False)

		if salida==0:
			self.Error_string.setText(Exept)
			return
		for p in pathlist:
			self.Print_Requests.append("http://" + url + '/' + p)
		for e in CodeError:
			if e == '200 OK':
				e = '<span style="color: #00FF00">' + e + '</span>'
			else:
				self.PrintHTTP.setStyleSheet("""
									color: red;
									""")
			self.PrintHTTP.append(e)
		self.Time_work.setText(str(round(time.time() - t1, 3)) + " сек")

	def Succes_2(self):
		self.Print_SuccesRequest.setText("")
		url = self.URL_string.text()
		for pi in range(0,len(pathlist)):
			if CodeError[pi] == "200 OK":
				self.Print_SuccesRequest.append("http://" + url + '/' +pathlist[pi])
				self.Print_SuccesRequest.setStyleSheet("""
					color: green;
					""")

	def site(self):
		self.Search_Site.setText("")
		url = self.URL_string.text()
		t1 = time.time()
		Data, Err, count = robots.search_yandex(url, "", False)
		for p in Data:
			self.Search_Site.append(p)
		if count ==0:
			self.Error_string_2.setText(Err)
		else:
			self.Error_string_2.setText("OK")

		self.Time_work_2.setText(str(round(time.time() - t1, 3)) + " сек")

def main():
	app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
	window = RobotsClass() # Создаем объект класса ExampleApp
	window.show() # Показать окно
	app.exec() # Запускаем приложение

if __name__ == '__main__':
	main()