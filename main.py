import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_dop = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_dop)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.d_delete = QPushButton("AC", self)
        self.hbox_dop.addWidget(self.d_delete)

        self.d_plm = QPushButton("+/-", self)
        self.hbox_dop.addWidget(self.d_plm)

        self.d_prc = QPushButton("%", self)
        self.hbox_dop.addWidget(self.d_prc)

        self.d_del = QPushButton("/", self)
        self.hbox_dop.addWidget(self.d_del)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_multi = QPushButton("x", self)
        self.hbox_third.addWidget(self.b_multi)

        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)

        self.b_dot = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_dot)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)




        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_result.clicked.connect(self._result)

        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_result.clicked.connect(self._result2)

        self.b_multi.clicked.connect(lambda: self._operation("x"))
        self.b_result.clicked.connect(self._result3)

        self.d_del.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result4)

        self.d_delete.clicked.connect(self._clear)

        self.d_plm.clicked.connect(lambda: self._operation("+/-"))
        self.d_plm.clicked.connect(self._result6)

        self.d_prc.clicked.connect(lambda: self._operation("%"))
        self.d_prc.clicked.connect(self._result7)


        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_dot.clicked.connect(lambda: self._button("."))

    def _button(self, param):
        line = self.input.text()
        if param == ".":
            if param not in line:
                self.input.setText(line + param)
            return
        self.input.setText(line + param)


    def _operation(self, op):
        self.num_1 = self.input.text()
        if self.num_1 == "/":
            self.input.setText("")
        if self.num_1 == "x":
            self.input.setText("")
        if self.num_1 == "+":
            self.input.setText("")
        if self.num_1 == "-":
            self.input.setText("")
        if self.num_1 == "%":
            self.input.setText("")
        if self.num_1 == "+/-":
            self.input.setText("")
        else:
            self.num_1 = (self.input.text())
            self.op = op
            self.input.setText("")



    def _result(self):
        if self.num_1.find('.') != -1:
            self.num_1 = float(self.num_1)
        else:
            self.num_1 = int(self.num_1)
        self.num_2 = (self.input.text())
        if self.num_2.find('.') != -1:
            self.num_2 = float(self.num_2)
        else:
            self.num_2 = int(self.num_2)

        if self.op == "+":
            if (type(self.num_1)) == float:
                if (type(self.num_2)) == float:
                    self.input.setText(str(float(self.num_1) + (float(self.num_2))))
                else:
                    self.input.setText(str(float(self.num_1) + (int(self.num_2))))
            else:
                if (type(self.num_2)) == float:
                    self.input.setText(str(int(self.num_1) + (float(self.num_2))))
                else:
                    self.input.setText(str(int(self.num_1) + (int(self.num_2))))




    def _result2(self):
        self.num_2 = (self.input.text())
        if self.num_2.find('.') != -1:
            self.num_2 = float(self.num_2)
        else:
            self.num_2 = int(self.num_2)

        if self.op == "-":
            if (type(self.num_1)) == float:
                if (type(self.num_2)) == float:
                    self.input.setText(str(float(self.num_1) - (float(self.num_2))))
                else:
                    self.input.setText(str(float(self.num_1) - (int(self.num_2))))
            else:
                if (type(self.num_2)) == float:
                    self.input.setText(str(int(self.num_1) - (float(self.num_2))))
                else:
                    self.input.setText(str(int(self.num_1) - (int(self.num_2))))

    def _result3(self):
        self.num_2 = (self.input.text())
        if self.num_2.find('.') != -1:
            self.num_2 = float(self.num_2)
        else:
            self.num_2 = int(self.num_2)

        if self.op == "x":
            if (type(self.num_1)) == float:
                if (type(self.num_2)) == float:
                    self.input.setText(str(float(self.num_1) * (float(self.num_2))))
                else:
                    self.input.setText(str(float(self.num_1) * (int(self.num_2))))
            else:
                if (type(self.num_2)) == float:
                    self.input.setText(str(int(self.num_1) * (float(self.num_2))))
                else:
                    self.input.setText(str(int(self.num_1) * (int(self.num_2))))

    def _result4(self):
        self.num_2 = (self.input.text())
        if self.num_2.find('.') != -1:
            self.num_2 = float(self.num_2)
        else:
            self.num_2 = int(self.num_2)

        if self.op == "/":
            if (type(self.num_1)) == float:
                if (type(self.num_2)) == float:
                    self.input.setText(str(float(self.num_1) / (float(self.num_2))))
                else:
                    self.input.setText(str(float(self.num_1) / (int(self.num_2))))
            else:
                if (type(self.num_2)) == float:
                    self.input.setText(str(int(self.num_1) / (float(self.num_2))))
                else:
                    self.input.setText(str(int(self.num_1) / (int(self.num_2))))

    def _clear(self):
        self.input.setText("")

    def _result6(self):
        if self.num_1.find('.') != -1:
            self.num_1 = float(self.num_1)
        else:
            self.num_1 = int(self.num_1)
        if self.op == "+/-":
            self.input.setText(str(self.num_1 * (-1)))

    def _result7(self):
        if self.num_1.find('.') != -1:
            self.num_1 = float(self.num_1)
        else:
            self.num_1 = int(self.num_1)
        if self.op == "%":
            self.input.setText(str(self.num_1 * 0.01))

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())