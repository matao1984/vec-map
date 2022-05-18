# -*- coding: utf-8 -*-
'''
Change History
05/18/2022 VecMap0.2
[001] and [011] radio selection
ABF couple with HAADF function to calculate O map
Algorithm to calculate O map on [011] direction
Bug fixes
06/13/2020 VecMap0.11
Minor bug fix
06/10/2020 VecMap0.1
The first versio of VecMap
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

ver = 'VecMap 0.2'
r_date = '05/18/2022'

class Ui_VecMap(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_VecMap,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        


    def setupUi(self, VecMap):
        VecMap.setObjectName("VecMap")
        VecMap.resize(402, 876)
        VecMap.setMinimumSize(QtCore.QSize(402, 836))
        VecMap.setMaximumSize(QtCore.QSize(1024, 1024))
        self.pushButton = QtWidgets.QPushButton(VecMap)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 95, 41))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_3 = QtWidgets.QRadioButton(VecMap)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 10, 95, 20))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(VecMap)
        self.radioButton_4.setGeometry(QtCore.QRect(200, 10, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.load_group = QtWidgets.QButtonGroup(VecMap)
        self.load_group.addButton(self.radioButton_3)
        self.load_group.addButton(self.radioButton_4)
        self.checkBox = QtWidgets.QCheckBox(VecMap)
        self.checkBox.setGeometry(QtCore.QRect(130, 35, 111, 20))
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(VecMap)
        self.line.setGeometry(QtCore.QRect(20, 95, 371, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(VecMap)
        self.label.setGeometry(QtCore.QRect(20, 10, 100, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(VecMap)
        self.label_2.setGeometry(QtCore.QRect(130, 55, 251, 51))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(VecMap)
        self.lineEdit.setGeometry(QtCore.QRect(130, 130, 30, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(VecMap)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 191, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(VecMap)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(VecMap)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 95, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(VecMap)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 95, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(VecMap)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 251, 51))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(VecMap)
        self.label_6.setGeometry(QtCore.QRect(130, 230, 251, 51))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(VecMap)
        self.line_2.setGeometry(QtCore.QRect(20, 280, 371, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(VecMap)
        self.label_9.setGeometry(QtCore.QRect(20, 300, 191, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox_2 = QtWidgets.QCheckBox(VecMap)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 330, 111, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(VecMap)
        self.checkBox_3.setGeometry(QtCore.QRect(130, 330, 131, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(VecMap)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 370, 95, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(VecMap)
        self.label_10.setGeometry(QtCore.QRect(130, 360, 251, 51))
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.checkBox_4 = QtWidgets.QCheckBox(VecMap)
        self.checkBox_4.setGeometry(QtCore.QRect(230, 35, 141, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.line_3 = QtWidgets.QFrame(VecMap)
        self.line_3.setGeometry(QtCore.QRect(20, 420, 371, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_11 = QtWidgets.QLabel(VecMap)
        self.label_11.setGeometry(QtCore.QRect(20, 440, 191, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(VecMap)
        self.label_12.setGeometry(QtCore.QRect(170, 130, 191, 32))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(VecMap)
        self.label_14.setGeometry(QtCore.QRect(20, 510, 381, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_4 = QtWidgets.QLineEdit(VecMap)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 550, 251, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_15 = QtWidgets.QLabel(VecMap)
        self.label_15.setGeometry(QtCore.QRect(20, 530, 181, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(VecMap)
        self.label_16.setGeometry(QtCore.QRect(20, 580, 381, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(VecMap)
        self.label_17.setGeometry(QtCore.QRect(20, 600, 181, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_5 = QtWidgets.QLineEdit(VecMap)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 620, 251, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(VecMap)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 550, 101, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(VecMap)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 680, 80, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_18 = QtWidgets.QLabel(VecMap)
        self.label_18.setGeometry(QtCore.QRect(200, 680, 191, 51))
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.pushButton_7 = QtWidgets.QPushButton(VecMap)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 460, 95, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_4 = QtWidgets.QFrame(VecMap)
        self.line_4.setGeometry(QtCore.QRect(20, 730, 371, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_8 = QtWidgets.QPushButton(VecMap)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 780, 120, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_19 = QtWidgets.QLabel(VecMap)
        self.label_19.setGeometry(QtCore.QRect(60, 850, 300, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(VecMap)
        self.label_20.setGeometry(QtCore.QRect(20, 750, 211, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_9 = QtWidgets.QPushButton(VecMap)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 780, 120, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(VecMap)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 810, 120, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(VecMap)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 810, 120, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(VecMap)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 780, 101, 58))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.radioButton = QtWidgets.QRadioButton(VecMap)
        self.radioButton.setGeometry(QtCore.QRect(20, 480, 95, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(VecMap)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 480, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.cal_group = QtWidgets.QButtonGroup(VecMap)
        self.cal_group.addButton(self.radioButton)
        self.cal_group.addButton(self.radioButton_2)
        self.label_21 = QtWidgets.QLabel(VecMap)
        self.label_21.setGeometry(QtCore.QRect(20, 460, 171, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_13 = QtWidgets.QPushButton(VecMap)
        self.pushButton_13.setGeometry(QtCore.QRect(200, 460, 85, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_7 = QtWidgets.QLabel(VecMap)
        self.label_7.setGeometry(QtCore.QRect(20, 650, 41, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(VecMap)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 650, 30, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_14 = QtWidgets.QPushButton(VecMap)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 680, 80, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(VecMap)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 650, 30, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(VecMap)
        self.label_13.setGeometry(QtCore.QRect(110, 650, 41, 16))
        self.label_13.setObjectName("label_13")
        self.checkBox_5 = QtWidgets.QCheckBox(VecMap)
        self.checkBox_5.setGeometry(QtCore.QRect(200, 650, 111, 20))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(VecMap)
        self.checkBox_6.setGeometry(QtCore.QRect(280, 650, 111, 20))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_4.setEnabled(False)
        self.checkBox.toggled.connect(self.checkBox_4.setEnabled)
        self.checkBox.toggled.connect(lambda checked: not checked and self.checkBox_4.setChecked(False))

        self.retranslateUi(VecMap)
        QtCore.QMetaObject.connectSlotsByName(VecMap)
        
        
#=======Connect all the functions=============================================
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.ini_atom_position)
        self.pushButton_3.clicked.connect(self.find_separation)
        self.pushButton_4.clicked.connect(self.refine_atom_position)
        self.pushButton_13.clicked.connect(self.cal_disp)
        self.pushButton_5.clicked.connect(self.vec_ang_dist)
        self.pushButton_6.clicked.connect(self.show_vec_map)
        self.pushButton_14.clicked.connect(self.show_O_vec_map)
        self.pushButton_7.clicked.connect(self.load_from_csv)
        self.pushButton_8.clicked.connect(self.disclaimer)
        self.pushButton_9.clicked.connect(self.show_about)
        self.pushButton_10.clicked.connect(self.acknowledgments)
        self.pushButton_11.clicked.connect(self.show_contact)
        self.pushButton_12.clicked.connect(self.donate)
    

    def retranslateUi(self, VecMap):
        _translate = QtCore.QCoreApplication.translate
        VecMap.setWindowTitle(_translate("VecMap", ver))
        #VecMap.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("VecMap", "Load Image"))
        self.checkBox.setText(_translate("VecMap", "ABF image"))
        self.label.setText(_translate("VecMap", "Step 1. Load image"))
        self.label_2.setText(_translate("VecMap", "<html><head/><body><p>Load a HR-STEM image with a perovskite structure. Support [001] and [011] zone axes. Filtered image is preferred.</p><p><br/></p></body></html>"))
        self.lineEdit.setText(_translate("VecMap", "8"))
        self.label_3.setText(_translate("VecMap", "Step 2. Initialize atom positions"))
        self.label_4.setText(_translate("VecMap", "Separation factor"))
        self.pushButton_2.setText(_translate("VecMap", "Initialize"))
        self.pushButton_3.setText(_translate("VecMap", "Find \n"
"separation"))
        self.label_5.setText(_translate("VecMap", "<html><head/><body><p>Input an appropriate separation factor to initialize the atom positions for refining. Adding/removing atoms by left-click.</p></body></html>"))
        self.label_6.setText(_translate("VecMap", "<html><head/><body><p>Try a few separation factors around the given number to determine the best separation factor.</p></body></html>"))
        self.label_9.setText(_translate("VecMap", "Step 3. Refine atom positions"))
        self.checkBox_2.setText(_translate("VecMap", "Refine Oxygen"))
        self.checkBox_3.setText(_translate("VecMap", "Save result plots"))
        self.pushButton_4.setText(_translate("VecMap", "Refine"))
        self.label_10.setText(_translate("VecMap", "<html><head/><body><p>Refine atom positions. Check [001] or [011] zone. Only check Refine Oxygen if O columns are visible.</p></body></html>"))
        self.checkBox_4.setText(_translate("VecMap", "Couple with HAADF"))
        self.label_11.setText(_translate("VecMap", "Step 4. Generate a vector map"))
        self.label_12.setText(_translate("VecMap", "A positive integer used to separate the \nA-site and B-site atoms."))
        self.label_14.setText(_translate("VecMap", "List of angles (degrees) of vectors that will be colored differently:"))
        self.lineEdit_4.setText(_translate("VecMap", "45"))
        self.label_15.setText(_translate("VecMap", "e.g., 45 135 225 315"))
        self.label_16.setText(_translate("VecMap", "List of colors (should match the angles):"))
        self.label_17.setText(_translate("VecMap", "e.g., yellow blue red green"))
        self.lineEdit_5.setText(_translate("VecMap", "yellow"))
        self.pushButton_5.setText(_translate("VecMap", "Vector angle\n"
"distrubution"))
        self.pushButton_6.setText(_translate("VecMap", "Cation \n"
"map"))
        self.label_18.setText(_translate("VecMap", "<html><head/><body><p>Generate a vector map. Set the coloring pattern by checking the vector angle distribution.</p></body></html>"))

        self.pushButton_7.setText(_translate("VecMap", "Load csv"))
        self.pushButton_8.setText(_translate("VecMap", "Disclaimer"))
        self.label_19.setText(_translate("VecMap", ver + " Released: " + r_date +" by Dr. Tao Ma"))
        self.label_20.setText(_translate("VecMap", "Check here for more information!"))
        self.pushButton_9.setText(_translate("VecMap", "About"))
        self.pushButton_10.setText(_translate("VecMap", "Acknoledgments"))
        self.pushButton_11.setText(_translate("VecMap", "Contact"))
        self.pushButton_12.setText(_translate("VecMap", "Buy me a\n" "LUNCH!"))
        self.radioButton.setText(_translate("VecMap", "A-site"))
        self.radioButton_2.setText(_translate("VecMap", "B-site"))
        self.label_21.setText(_translate("VecMap", "Select which site to calculate"))
        self.pushButton_13.setText(_translate("VecMap", "Calculate"))
        self.label_7.setText(_translate("VecMap", "Scale:"))
        self.lineEdit_2.setText(_translate("VecMap", "8"))
        self.pushButton_14.setText(_translate("VecMap", "Oxygen\n"
" map"))
        self.lineEdit_3.setText(_translate("VecMap", "4"))
        self.label_13.setText(_translate("VecMap", "Scale:"))
        self.checkBox_5.setText(_translate("VecMap", "Scale bar"))
        self.checkBox_6.setText(_translate("VecMap", "Overlay image"))
        self.radioButton_3.setText(_translate("VecMap", "[001]"))
        self.radioButton_4.setText(_translate("VecMap", "[011]"))

#===== Open file and set up global variables such as path etc. ======================
#===== Connected to self.pushButton =================================================       
    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Select Image','','DigitalMicrograph (*.dm3 , *.dm4);;Image files (*.tif , *.tiff , *.jpg , *.jpeg , *.png ,*.bmp);;All Files (*)')
        global file, my_path, file_path, title, title_adf, scale, units, s, s_adf, im, image, image_adf, ABF, img_110, Couple, overlay
        file = openfile_name[0]
                
        if self.checkBox.isChecked(): #Set ABF toggle from the checkbox
            ABF = True
        else:
            ABF = False
            
        if self.checkBox_4.isChecked(): #Couple with HAADF
            Couple = True
        else:
            Couple = False
            
            
        if self.radioButton_4.isChecked():
            img_110 = True
        else:
            img_110 = False
            

            
        if file:
            print('{} has been loaded!'.format(file))
            my_path = getDirectory(file) #Set the working path
            file_path = getDirectory(file, '/') #Set the parent path
            file_name = getFileName(file) #Read file name as its title
            if not os.path.exists(my_path):
                os.makedirs(my_path)
            s = readImage(file) 
            title = file_name
            scale = s.axes_manager[0].scale #Read scale data from the image
            units = s.axes_manager[0].units #Read units
            s.metadata.General.title = title
            s.save(my_path + title +'.hspy', overwrite=True) #Save a backup file in hspy format
            image = s.data
            #s.data = norm_img(s.data)
            
            if ABF:
                s.data = np.divide(1, s.data) #Inverse the ABF contrast to make a ADF-like image
                #s.data = abf2haadf(s.data) #Inverse the ABF contrast to make a ADF-like image

                
        # Draw an image
            global f_original_img
            f_original_img = PlotCanvas()
            f_original_img.setWindowTitle(file)
            f_original_img.axes.imshow(image,cmap='gray')
            f_original_img.axes.set_axis_off()
            f_original_img.axes.set_title('{} \n has been successfully loaded!'.format(title))
            f_original_img.show()

            #Load HAADF if couple is checked
            if Couple:
                openfile_adf = QFileDialog.getOpenFileName(self,'Select corresponding HAADF Image','','DigitalMicrograph (*.dm3 , *.dm4);;Image files (*.tif , *.tiff , *.jpg , *.jpeg , *.png ,*.bmp);;All Files (*)')
                adf_file = openfile_adf[0]
                s_adf = readImage(adf_file)
                title_adf = getFileName(adf_file)
                s_adf.metadata.General.title = title_adf
                s_adf.save(my_path + title_adf + '.hspy', overwrite=True) #Save a backup file in hspy format
                image_adf = s_adf.data
                im = s_adf
                global f_original_adf
                f_original_adf = PlotCanvas()
                f_original_adf.setWindowTitle(adf_file)
                f_original_adf.axes.imshow(image_adf,cmap='gray')
                f_original_adf.axes.set_axis_off()
                f_original_adf.axes.set_title('The coupled HAADF image has been successfully loaded!')
                f_original_adf.show()        
            
            else:
                im = s

#==== Initialize atom position module ===============================================
#==== Connected to self.pushButton_2 ================================================ 
    def ini_atom_position(self):
        sep = int(self.lineEdit.text())

        try:
            A_positions_ini = get_atom_positions(im,separation=sep)
            global A_positions, f_ini
            A_positions = A_positions_ini.tolist()
            f_ini = PlotCanvas()
            f_ini.setWindowTitle('Initial atom positions for refining')
            f_ini.axes.imshow(im.data,cmap='gray')
            f_ini.axes.set_axis_off()
            f_ini.axes.set_title('Left click to add or remove atoms')
            f_ini.show()
           
            def onclick(event):
                if event.inaxes != f_ini.axes:
                    return
                if event.button == 1:  # Left mouse button
                    x = float(event.xdata)
                    y = float(event.ydata)
                    atom_nearby = closest_node((x,y), A_positions)[0]
                    if distance.euclidean((x,y), A_positions[atom_nearby]) > 5:
                        A_positions.append([x, y])
                    else:
                        A_positions.pop(atom_nearby)
                    replot(f_ini)
                
                
            def get_xy_pos_lists(atom_lst):
                return np.asarray(atom_lst)[:,0], np.asarray(atom_lst)[:,1]
                
            def replot(f):
                x_pos, y_pos = get_xy_pos_lists(A_positions)
                dp.set_xdata(x_pos)
                dp.set_ydata(y_pos)
                f.fig.canvas.draw()
                f.fig.canvas.flush_events()        
            
            
            xy_positions = get_xy_pos_lists(A_positions)
            dp, = f_ini.axes.plot(xy_positions[0], xy_positions[1], marker='o', ms=5, color='r', ls='')
            cid = f_ini.fig.canvas.mpl_connect('button_press_event', onclick)
        
        except NameError:
            #Pop up an error window
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please load the image file first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()
        

        

#==== Find separation module ======================================================== 
#==== Connected to self.pushButton_3 ================================================      
    def find_separation(self):
        #sep_range = (int(self.lineEdit_2.text()), int(self.lineEdit_3.text()))
        #s_peaks=am.get_feature_separation(s, separation_range=sep_range) #Range might be changed for different images
        #s_peaks.metadata.General.title = 'Use Arrow keys to find an appropriate separation factor'
        #s_peaks.plot(colorbar=False,scalebar=False,axes_off=True)
        sep = int(self.lineEdit.text())
        sep_range = list(range(sep - 4, sep + 5))
        # Create canvas for drawing
        try:
            global f_sep
            f_sep = SeparationCanvas()
            for i in range(9):
                s_factor = sep - 4 + i  
                f_sep.axes[i].set_aspect('equal')
                f_sep.axes[i].set_axis_off()
                if s_factor < 1:
                    continue
                ini_position = get_atom_positions(im, separation=s_factor)
                f_sep.axes[i].imshow(im.data,cmap='gray')
                f_sep.axes[i].scatter(np.asarray(ini_position)[:,0], np.asarray(ini_position)[:,1], s=5, color='r')
                f_sep.axes[i].set_title('Separation = {}'.format(s_factor))
            f_sep.show()
        
        except NameError:
            #Pop up an error window
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please load the image file first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()
            
        
#==== Refine atom position module ===================================================
#==== Connected to self.pushButton_4 ================================================
    def refine_atom_position(self):
        #Global variables:
        global ap_A, ap_B, ap_O, Ua, Uc, find_O, ap_A_abf, ap_B_abf
        #Read checkboxes
        if self.checkBox_2.isChecked():
            find_O = True
        else:
            find_O = False
                
        if self.checkBox_3.isChecked():
            plotpos = True
        else:
            plotpos = False
        try:
            #Refine atom positions
            print('='*50)
            print('Refining atom positions for A-site atoms...')
            print('This may take time...')
            sublattice_A = find_atom(im.data, A_positions, 'A-site atoms')
            print('Refining A-site atoms done!')
            ap_A = sublattice_A.atom_positions #Refined atoms positions for A-site. NumPy array.
            #lattice_list = []
            #lattice_list.append(sublattice_A)
            print('='*50)
    
            print('Finding the initial positions for B-site atoms...')
            
            sublattice_A.construct_zone_axes()
    
            #Find the zone axis for the initial position of B: typically 3 for [001] and 1 for [110]
            if img_110 == True:
                zone_axis = sublattice_A.zones_axis_average_distances[1]
            else:        
                zone_axis = sublattice_A.zones_axis_average_distances[2]
            #Calculate lattice parameter
            z0 = sublattice_A.zones_axis_average_distances[0]
            z1 = sublattice_A.zones_axis_average_distances[1]
            Ua = math.sqrt(z0[0]**2 + z0[1]**2) * scale
            Uc = math.sqrt(z1[0]**2 + z1[1]**2) * scale
            print('='*50)
            print('Estimated lattice parameters (average) from the image:')
            print('a = {:.3f} {}'.format(Ua, units))
            print('c = {:.3f} {}'.format(Uc, units))
            B_positions = sublattice_A.find_missing_atoms_from_zone_vector(zone_axis)
    
            #Reomve A-site atoms from the image
            print('='*50)
            print('Subtracting sublattice A from the image using 2D gaussian fit...')
            print('This may take time...')
            image_without_A = remove_atoms_from_image_using_2d_gaussian(sublattice_A.image, sublattice_A, show_progressbar=False)
    
            #Refine B-site atoms
            print('='*50)
            print('Refining atom positions for sublattice B...')
            print('Almost there...')
            sublattice_B = find_atom(image_without_A, B_positions, 'B-site atoms', atom_color='blue')
            ap_B = sublattice_B.atom_positions ##Refined atoms positions for B-site. NumPy array.
            print('Refining B-site atoms done!')
            #Save refined atom positions in csv
            with open(my_path + title + '-A_positions_refined.csv','w') as A_positions_data:
                A_positions_data.write('Refined positions for A-site atoms\n')
                A_positions_data.write('x (px), y (px)\n')
                for data in ap_A.tolist():
                    A_positions_data.write('{}, {}'.format(data[0], data[1]))
                    A_positions_data.write('\n')
            print('Refined positions for the A-site atoms have been saved to ' + my_path + title + '-A_positions_refined.csv')
            with open(my_path + title + '-B_positions_refined.csv','w') as B_positions_data:
                B_positions_data.write('Refined positions for B-site atoms\n')
                B_positions_data.write('x (px), y (px)\n')
                for data in ap_B.tolist():
                    B_positions_data.write('{}, {}'.format(data[0], data[1]))
                    B_positions_data.write('\n')
            print('Refined positions for the B-site atoms have been saved to ' + my_path + title + '-B_positions_refined.csv')
            #lattice_list.append(sublattice_B)
            #Find the position of O atoms
            if Couple:
                print('='*50)
                print('Refining atom positions for A-site atoms on ABF image...')
                print('This may take time...')
                sublattice_A_abf = find_atom(s.data, ap_A, 'ABF A-site atoms')
                print('Refining A-site atoms done!')
                ap_A_abf = sublattice_A_abf.atom_positions #Refined atoms positions for A-site. NumPy array.
                #lattice_list = []
                #lattice_list.append(sublattice_A)
                print('='*50)
                print('Subtracting sublattice A from the image using 2D gaussian fit...')
                print('This may take time...')
                abf_image_without_A = remove_atoms_from_image_using_2d_gaussian(sublattice_A_abf.image, sublattice_A_abf, show_progressbar=False)
                print('='*50)
                print('Refining atom positions for sublattice B on ABF image...')
                print('Almost there...')
                sublattice_B_abf = find_atom(abf_image_without_A, ap_B, 'ABF B-site atoms', atom_color='blue')
                ap_B_abf = sublattice_B_abf.atom_positions ##Refined atoms positions for B-site. NumPy array.
                print('Refining B-site atoms done!')
                #Save refined atom positions in csv
                with open(my_path + title + '-A_positions_ABF_refined.csv','w') as A_ABF_positions_data:
                    A_ABF_positions_data.write('Refined positions for A-site atoms in the ABF image\n')
                    A_ABF_positions_data.write('x (px), y (px)\n')
                    for data in ap_A_abf.tolist():
                        A_ABF_positions_data.write('{}, {}'.format(data[0], data[1]))
                        A_ABF_positions_data.write('\n')
                print('Refined positions for the A-site atoms in the ABF image have been saved to ' + my_path + title + '-A_positions_ABF_refined.csv')
                with open(my_path + title + '-B_positions_ABF_refined.csv','w') as B_ABF_positions_data:
                    B_ABF_positions_data.write('Refined positions for B-site atoms in the ABF image\n')
                    B_ABF_positions_data.write('x (px), y (px)\n')
                    for data in ap_B_abf.tolist():
                        B_ABF_positions_data.write('{}, {}'.format(data[0], data[1]))
                        B_ABF_positions_data.write('\n')
                print('Refined positions for the B-site atoms in the ABF image have been saved to ' + my_path + title + '-B_positions_ABF_refined.csv')
                
            if find_O:
                #Find initial positions for O
                #For [001] images:
                if not img_110:
                    AB_positions = ap_A.tolist() + B_positions #Use initial B positions instead of refined to get better plane symmetry
                    sublattice_AB = Sublattice(AB_positions,image=s.data,color='y',name='Sublattice A + B')
                    sublattice_AB.construct_zone_axes(atom_plane_tolerance=0.8)
                    zone_axis_002 = sublattice_AB.zones_axis_average_distances[2]#Only work for [001] currently
                    O_positions = sublattice_AB.find_missing_atoms_from_zone_vector(zone_axis_002) #Initial positions of O
                    print('='*50)
                    print('Subtracting sublattice A and B from the image using 2D gaussian fit...')
                    print('This may take time...')
                    
                else:
                    zone_axis2 = sublattice_A.zones_axis_average_distances[2]
                    O_positions = sublattice_A.find_missing_atoms_from_zone_vector(zone_axis2)
                
                if Couple:
                    image_without_AB=remove_atoms_from_image_using_2d_gaussian(sublattice_B_abf.image,sublattice_B_abf,show_progressbar=False)
                else:
                    image_without_AB=remove_atoms_from_image_using_2d_gaussian(sublattice_B.image,sublattice_B,show_progressbar=False) #Subtract both A and B from the original image
                #Refine O positions
                print('='*50)
                print('Refining atom positions for sublattice O...')
                sublattice_O = find_atom(image_without_AB, O_positions, 'O sites', atom_color='g')
                ap_O = sublattice_O.atom_positions #Refined atoms positions for O. NumPy array.
                print('Refining O atoms done!')
                with open(my_path + title + '-B_positions_refined.csv','w') as O_positions_data:
                    O_positions_data.write('Refined positions for O\n')
                    O_positions_data.write('x (px), y (px)\n')
                    for data in ap_O.tolist():
                        O_positions_data.write('{}, {}'.format(data[0], data[1]))
                        O_positions_data.write('\n')
                print('Refined positions for O have been saved to ' + my_path + title + '-O_positions.csv')
                #lattice_list.append(sublattice_O)
            print('Refining atoms done!') 
            #Construct atom position results with sublattice A and B.
            #atom_lattice = am.Atom_Lattice(image=image, name='Atoms positions', sublattice_list=lattice_list)
    
            #Save the refined positions and original image as hdf5 file. This file can be called later.
            #atom_lattice.save(my_path + 'atom_position.hdf5', overwrite=True)
            #=======================
            #Plot and save figures
            #=======================
            if plotpos: 
                print('='*50)
                print('Saving result plots...')
                global f_A_site, f_B_site, f_AB, f_A_site_adf, f_B_site_abf, f_AB_adf
                if Couple:
                    #Plot A-site atom positions with the original image overlayed.
                    f_A_site = PlotCanvas()
                    f_A_site.setWindowTitle(ver + ': Refined positions of A-site atoms in ABF')
                    f_A_site.axes.imshow(image,cmap='gray')
                    f_A_site.axes.scatter(ap_A_abf[:,0], ap_A_abf[:,1], s=2, color='r')
                    f_A_site.axes.set_axis_off()
                    f_A_site.show()
                    f_A_site.fig.savefig(my_path + title + '_A-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot B-site atom positions with the original image overlayed.
                    f_B_site = PlotCanvas()
                    f_B_site.setWindowTitle(ver + ': Refined positions of B-site atoms in ABF')
                    f_B_site.axes.imshow(image,cmap='gray')
                    f_B_site.axes.scatter(ap_B_abf[:,0], ap_B_abf[:,1], s=2, color='b')
                    f_B_site.axes.set_axis_off()
                    f_B_site.show()
                    f_B_site.fig.savefig(my_path + title + '_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot both A-site and B-site on the image
                    f_AB = PlotCanvas()
                    f_AB.setWindowTitle(ver + ': A-site atoms vs. B-site atoms in ABF')
                    f_AB.axes.imshow(image,cmap='gray')
                    f_AB.axes.scatter(ap_A_abf[:,0], ap_A_abf[:,1], s=2, color='r')
                    f_AB.axes.scatter(ap_B_abf[:,0], ap_B_abf[:,1], s=2, color='b')
                    f_AB.axes.set_axis_off()
                    f_AB.show()
                    f_AB.fig.savefig(my_path + title + '_A_and_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
                    
                    #Plot A-site atom positions on ADF with the original image overlayed.
                    f_A_site_adf = PlotCanvas()
                    f_A_site_adf.setWindowTitle(ver + ': Refined positions of A-site atoms in ADF')
                    f_A_site_adf.axes.imshow(image_adf,cmap='gray')
                    f_A_site_adf.axes.scatter(ap_A[:,0], ap_A[:,1], s=2, color='r')
                    f_A_site_adf.axes.set_axis_off()
                    f_A_site_adf.show()
                    f_A_site_adf.fig.savefig(my_path + title_adf + '_A-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot B-site atom positions with the original image overlayed.
                    f_B_site_adf = PlotCanvas()
                    f_B_site_adf.setWindowTitle(ver + ': Refined positions of B-site atoms in ADF')
                    f_B_site_adf.axes.imshow(image_adf,cmap='gray')
                    f_B_site_adf.axes.scatter(ap_B[:,0], ap_B[:,1], s=2, color='b')
                    f_B_site_adf.axes.set_axis_off()
                    f_B_site_adf.show()
                    f_B_site_adf.fig.savefig(my_path + title_adf + '_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot both A-site and B-site on the image
                    f_AB_adf = PlotCanvas()
                    f_AB_adf.setWindowTitle(ver + ': A-site atoms vs. B-site atoms in ADF')
                    f_AB_adf.axes.imshow(image_adf,cmap='gray')
                    f_AB_adf.axes.scatter(ap_A[:,0], ap_A[:,1], s=2, color='r')
                    f_AB_adf.axes.scatter(ap_B[:,0], ap_B[:,1], s=2, color='b')
                    f_AB_adf.axes.set_axis_off()
                    f_AB_adf.show()
                    f_AB_adf.fig.savefig(my_path + title_adf + '_A_and_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
                else:
                    #Plot A-site atom positions with the original image overlayed.
                    f_A_site = PlotCanvas()
                    f_A_site.setWindowTitle(ver + ': Refined positions of A-site atoms')
                    f_A_site.axes.imshow(image,cmap='gray')
                    f_A_site.axes.scatter(ap_A[:,0], ap_A[:,1], s=2, color='r')
                    f_A_site.axes.set_axis_off()
                    f_A_site.show()
                    f_A_site.fig.savefig(my_path + title + '_A-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot B-site atom positions with the original image overlayed.
                    f_B_site = PlotCanvas()
                    f_B_site.setWindowTitle(ver + ': Refined positions of B-site atoms')
                    f_B_site.axes.imshow(image,cmap='gray')
                    f_B_site.axes.scatter(ap_B[:,0], ap_B[:,1], s=2, color='b')
                    f_B_site.axes.set_axis_off()
                    f_B_site.show()
                    f_B_site.fig.savefig(my_path + title + '_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
        
                    #Plot both A-site and B-site on the image
                    f_AB = PlotCanvas()
                    f_AB.setWindowTitle(ver + ': A-site atoms vs. B-site atoms')
                    f_AB.axes.imshow(image,cmap='gray')
                    f_AB.axes.scatter(ap_A[:,0], ap_A[:,1], s=2, color='r')
                    f_AB.axes.scatter(ap_B[:,0], ap_B[:,1], s=2, color='b')
                    f_AB.axes.set_axis_off()
                    f_AB.show()
                    f_AB.fig.savefig(my_path + title + '_A_and_B-site atoms' + '.tif',dpi=600,bbox_inches='tight')
                #Plot O atoms if available
                if find_O:
                    global f_O_site, f_all
                    f_O_site = PlotCanvas()
                    f_O_site.setWindowTitle(ver + ': Refined positions of O atoms')
                    f_O_site.axes.imshow(image,cmap='gray')
                    f_O_site.axes.scatter(ap_O[:,0], ap_O[:,1], s=2, color='g')
                    f_O_site.axes.set_axis_off()
                    f_O_site.show()
                    f_O_site.fig.savefig(my_path + title + '_O atoms' + '.tif',dpi=600,bbox_inches='tight')                
    
                    #Plot all the atoms on the image
                    f_all = PlotCanvas()
                    f_all.setWindowTitle(ver + ': A-site vs. B-site vs. O atoms')
                    f_all.axes.imshow(image,cmap='gray')
                    f_all.axes.scatter(ap_A[:,0], ap_A[:,1], s=2, color='r')
                    f_all.axes.scatter(ap_B[:,0], ap_B[:,1], s=2, color='b')
                    f_all.axes.scatter(ap_O[:,0], ap_O[:,1], s=2, color='g')
                    f_all.axes.set_axis_off()
                    f_all.show()
                    f_all.fig.savefig(my_path + title + '_A_B_O atoms' + '.tif',dpi=600,bbox_inches='tight')  
                print('All figures have been saved to '+ my_path)
        except NameError:
            #Pop up an error window
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please initialize the atom positions first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()


#==================== Calculate displacement module =================================
#==================== Connected to self.pushButton_13 ===============================
    def cal_disp(self):
        try:
            #Global variables
            global U_avg, disp, disp_O, disp_adf, disp_atom, ideal_pos, ideal_O_pos
            # Read cal_site from the radio button
            # 0 to calculate A site in relative to B site; 1 to calculate B site in relative to A site
            if self.radioButton.isChecked():
                cal_site = 0
            if self.radioButton_2.isChecked():
                cal_site = 1
    
            cal_110 = img_110 #If the input image is [110], turn this on. O map is not supported for [110] yet.
            O_map = find_O #If enabled, will calculate the displacement of O atoms in relation to sublattice B.
            U_avg = (Ua + Uc)/2  #Unit cell parameter estimated from the image.     
            #=========================================================================
            #The main scripts start from here
            if cal_site == 0:#Calculate A site
                disp_atom = 'A-site'
                rel_atom = 'B-site' 
                if Couple:
                   ap_0 = ap_A_abf.tolist()
                   ap_1 = ap_B_abf.tolist()
                   ap_0_adf = ap_A.tolist()
                   ap_1_adf = ap_B.tolist()
                else:
                    ap_0 = ap_A.tolist()
                    ap_1 = ap_B.tolist()
            else:
                disp_atom = 'B-site'
                rel_atom = 'A-site'
                if Couple:
                    ap_0 = ap_B_abf.tolist()
                    ap_1 = ap_A_abf.tolist() 
                    ap_0_adf = ap_B.tolist()
                    ap_1_adf = ap_A.tolist()
                else:
                    ap_0 = ap_B.tolist()
                    ap_1 = ap_A.tolist()
            print('='*50)
            print('====Calculate {} in relative to {}===='.format(disp_atom, rel_atom))
    
            ideal_pos, neighbor_pos = find_ideal_pos(ap_0, ap_1, U_avg, scale, img_110=cal_110)

            disp = find_displacement(ap_0, ideal_pos, U_avg, scale)


            #Save the displacement data
            with open(my_path + title + '-{}-disp.csv'.format(disp_atom),'w') as disp_data:
                disp_data.write('x (px), y (px), x disp (px), y disp (px), disp (nm), angle (deg), Neighboring atoms (x y)\n')
                for i in range(len(disp)):
                    disp_data.write('{}, {}, {}, {}, {}, {}, '.format(disp[i][0], disp[i][1], disp[i][2], disp[i][3], disp[i][4], disp[i][5]))
                    for pos in neighbor_pos[i]:
                        for atom in pos:
                            disp_data.write('{}, '.format(atom))
                    disp_data.write('\n')
            print(my_path + title + '-{}-disp.csv'.format(disp_atom) + ' has been saved!')
            #Couple ABF/HAADF
            if Couple:
                ideal_pos_adf, neighbor_pos_adf = find_ideal_pos(ap_0_adf, ap_1_adf, U_avg, scale, img_110=cal_110)
                disp_adf = find_displacement(ap_0_adf, ideal_pos_adf, U_avg, scale)
                with open(my_path + title_adf + '-{}-disp.csv'.format(disp_atom),'w') as disp_data_adf:
                    disp_data_adf.write('x (px), y (px), x disp (px), y disp (px), disp (nm), angle (deg)\n')
                    for i in range(len(disp_adf)):
                        disp_data_adf.write('{}, {}, {}, {}, {}, {}, '.format(disp_adf[i][0], disp_adf[i][1], disp_adf[i][2], disp_adf[i][3], disp_adf[i][4], disp_adf[i][5]))
                        for pos in neighbor_pos_adf[i]:
                            for atom in pos:
                                disp_data_adf.write('{}, '.format(atom))
                        disp_data_adf.write('\n')
                print(my_path + title_adf + '-{}-disp.csv'.format(disp_atom) + ' has been saved!')
    
            #Save the neigboring atoms as well
            #with open(my_path + 'neighboring atoms.csv','w') as neighbor_data:
            #    for data in neighbor_pos:
            #        n = len(data)
            #        for idx in range(n):
            #            neighbor_data.write('{0}, {1}, '.format(*data[idx]))
            #        neighbor_data.write('\n')
            #print('Atomic displacement data saved to ' + my_path + title + '-disp.csv.')
            #Calculate O map and save        
            if O_map == 1:
                ap_2 = ap_O.tolist()
                ideal_O_pos = find_ideal_O_pos(ap_0, ap_1, Ua, scale, O = ap_2, img_110 = img_110, ref = rel_atom)
                disp_O = find_displacement(ap_2, ideal_O_pos, Ua, scale)
        
                with open(my_path + title + '-disp_O_by_{}.csv'.format(disp_atom),'w') as disp_data:
                    disp_data.write('x (px), y (px), x disp (px), y disp (px), disp (nm), angle (deg)\n')
                    for data in disp_O:
                        disp_data.write('{}, {}, {}, {}, {}, {}'.format(data[0], data[1], data[2], data[3], data[4], data[5]))
                        disp_data.write('\n')
                print('O displacement data saved to ' + my_path + title + '-disp_O_by_{}.csv.'.format(disp_atom))
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please refine the atom positions first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()

        
#======== Display angle distribution of the vectors module ===========================
#======== Connected to self.pushButton_5 =============================================
    def vec_ang_dist(self):
        try:
            global disp_angles
            disp_angles = [lst[5] for lst in disp]
            global f_vec_ang_dist
            f_vec_ang_dist = PlotCanvas()
            f_vec_ang_dist.setWindowTitle('Histogram of Displacement Directions')
            f_vec_ang_dist.axes.hist(disp_angles, bins=50, range=(0,360))
            f_vec_ang_dist.axes.set_xlabel('Displacement angles (Degrees)')
            f_vec_ang_dist.axes.set_xticks(list(range(0,390,30)))
            f_vec_ang_dist.axes.set_ylabel('Frequency')
            f_vec_ang_dist.axes.set_title('Put your cursor on the peak(s) to see the\n displacement directions')
            f_vec_ang_dist.show()
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please calculate the displacement first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()
            print('')
        
#========= Generate vector map module =============================================
#========= Connected to self.pushButton_6 ===========================================
    def show_vec_map(self):
        if self.checkBox_6.isChecked():
            overlay = True
        else:
            overlay = False
        a_len = int(self.lineEdit_2.text())
        if self.checkBox_5.isChecked():
            s_bar = True
        else:
            s_bar = False
        try:
            # Read from lineEdits:
            ang_lst = str(self.lineEdit_4.text()).split() #A list of displacement directions. This is used to determine the coloring pattern. For single color rendering, just leave it as [0].
            ang_lst = [int(a) for a in ang_lst]
            color_lst = str(self.lineEdit_5.text()).split()
            #====Plot====
            disp_color = set_arrow_color(disp, ang_lst, color_lst)
            
            v_x, v_y =image.shape
            img_blank = 255 * np.ones((v_x, v_y,3), dtype=np.uint8)

            global f_vec_map
            f_vec_map = PlotCanvas()
            f_vec_map.setWindowTitle(ver + ': Vector Map')
            
            f_vec_map.axes.set_axis_off()

            if overlay:               
                f_vec_map.axes.imshow(image,cmap='gray')
            else:                
                f_vec_map.axes.imshow(img_blank)
                s_bar = False
                f_vec_map.axes.axis('on')
                f_vec_map.axes.get_xaxis().set_visible(False)
                f_vec_map.axes.get_yaxis().set_visible(False)
                f_vec_map.axes.spines['bottom'].set_color('blue')
                f_vec_map.axes.spines['top'].set_color('blue')
                f_vec_map.axes.spines['left'].set_color('blue')
                f_vec_map.axes.spines['right'].set_color('blue')
            
            for vec in disp_color:
                f_vec_map.axes.arrow(vec[0],vec[1],vec[2]*a_len,vec[3]*a_len,color=vec[6], linewidth=1, head_width=a_len/3, head_length=a_len/3)

            #Add a scale bar
            if s_bar:            
                scalebar = ScaleBar(scale,'nm',location='lower left',scale_loc='top',sep=2)
                f_vec_map.axes.add_artist(scalebar)            
    
            f_vec_map.show()
            if overlay:
                f_vec_map.fig.savefig(my_path + title + "_{}_vec_map_img_overlaid.tif".format(disp_atom),dpi=1200,bbox_inches='tight')
            else:
                f_vec_map.fig.savefig(my_path + title + "_{}_vec_map.tif".format(disp_atom),dpi=1200,bbox_inches='tight')
            print('The vector map has been saved to ' + my_path + title + "_{}_vec_map.tif! Enjoy!".format(disp_atom))

            if Couple:
                disp_color_adf = set_arrow_color(disp_adf, ang_lst, color_lst)
                global f_vec_map_adf
                f_vec_map_adf = PlotCanvas()
                f_vec_map_adf.setWindowTitle(ver + ': Vector Map')
                f_vec_map_adf.axes.set_axis_off()
                if overlay:
                    f_vec_map_adf.axes.imshow(image_adf,cmap='gray')
                else:
                    f_vec_map_adf.axes.imshow(img_blank)
                    s_bar = 0
                    f_vec_map_adf.axes.axis('on')
                    f_vec_map_adf.axes.get_xaxis().set_visible(False)
                    f_vec_map_adf.axes.get_yaxis().set_visible(False)
                    f_vec_map_adf.axes.spines['bottom'].set_color('blue')
                    f_vec_map_adf.axes.spines['top'].set_color('blue')
                    f_vec_map_adf.axes.spines['left'].set_color('blue')
                    f_vec_map_adf.axes.spines['right'].set_color('blue')


                for vec in disp_color_adf:
                    f_vec_map_adf.axes.arrow(vec[0],vec[1],vec[2]*a_len,vec[3]*a_len,color=vec[6], linewidth=1, head_width=a_len/3, head_length=a_len/3)

                #Add a scale bar
                if s_bar:            
                    scalebar = ScaleBar(scale,'nm',location='lower left',scale_loc='top',sep=2)
                    f_vec_map_adf.axes.add_artist(scalebar)
                
                f_vec_map_adf.show()
                if overlay:
                    f_vec_map_adf.fig.savefig(my_path + title_adf + "_{}_vec_map_img_overlaid.tif".format(disp_atom),dpi=1200,bbox_inches='tight')
                else:
                    f_vec_map_adf.fig.savefig(my_path + title_adf + "_{}_vec_map.tif".format(disp_atom),dpi=1200,bbox_inches='tight')

                print('The vector map has been saved to ' + my_path + title + "_{}_vec_map.tif! Enjoy!".format(disp_atom))

        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please calculate the displacement first!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()
        
        except IndexError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The list of colors should match the list of angles!")
            msg.setWindowTitle("Hey guys")

            returnValue = msg.exec()
            
#========= Generate O vector map module =============================================
#========= Connected to self.pushButton_14 =========================================== 
    def show_O_vec_map(self):
        O_len = int(self.lineEdit_3.text())
        if self.checkBox_6.isChecked():
            overlay = True
        else:
            overlay = False
        if self.checkBox_5.isChecked():
            s_bar = True
        else:
            s_bar = False
        v_x, v_y =image.shape
        img_blank = 255 * np.ones((v_x, v_y, 3),dtype=np.uint8)
        try:
            global f_vec_map_O
            f_vec_map_O = PlotCanvas()
            f_vec_map_O.setWindowTitle(ver + ': Vector Map of Oxygen atoms')
            f_vec_map_O.axes.set_axis_off()
            if overlay:
                f_vec_map_O.axes.imshow(image,cmap='gray')
            else:
                f_vec_map_O.axes.imshow(img_blank)
                s_bar = False
                f_vec_map_O.axes.axis('on')
                f_vec_map_O.axes.get_xaxis().set_visible(False)
                f_vec_map_O.axes.get_yaxis().set_visible(False)
                f_vec_map_O.axes.spines['bottom'].set_color('blue')
                f_vec_map_O.axes.spines['top'].set_color('blue')
                f_vec_map_O.axes.spines['left'].set_color('blue')
                f_vec_map_O.axes.spines['right'].set_color('blue')
                

            for vec in disp_O:
                f_vec_map_O.axes.arrow(vec[0],vec[1],vec[2]*O_len,vec[3]*O_len,color='red',linewidth=1,head_width=O_len/3,head_length=O_len/3)
            #Add a scale bar
            if s_bar:            
                scalebar = ScaleBar(scale,'nm',location='lower left',scale_loc='top',sep=2)
                f_vec_map_O.axes.add_artist(scalebar)            
            
            f_vec_map_O.show()
            if overlay:
                f_vec_map_O.fig.savefig(my_path + title + "_O_vec_map_by_{}_img_overlaid.tif".format(disp_atom),dpi=1200,bbox_inches='tight')
            else:
                f_vec_map_O.fig.savefig(my_path + title + "_O_vec_map_by_{}.tif".format(disp_atom),dpi=1200,bbox_inches='tight')
            print('The O vector map has been saved to ' + my_path + title + "_O_vec_map_by_{}.tif! Enjoy!".format(disp_atom))
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No O displacement data exist!")
            msg.setWindowTitle("Hey guys")
            returnValue = msg.exec()    
            

#============ Load displacement from csv module ====================================
#============ Connected to self.pushButton_7 =======================================
    def load_from_csv(self):
        # Load displacement data from the csv file saved previously
        global s, my_path, title, scale, units, disp, disp_O, image, disp_atom, Couple, find_O
        openfile_name = QFileDialog.getOpenFileName(self,'Select the displacement data','','CSV (*.csv);;All Files (*)')
        file = openfile_name[0]
        if file:
            my_path = getDirectory(file,'/')
            file_name = getFileName(file)
            title = file_name[:-12]
            s = readImage(my_path + title + '.hspy')
            scale = s.axes_manager[0].scale
            units = s.axes_manager[0].units
            image = s.data
            disp = load_disp_data_from_csv(file)
            Couple = False #Do not support "couple" mode
            # Look for the O data
            disp_atom = file[-15:-9]
            file_O_disp = my_path + title + '-disp_O_by_' + disp_atom + '.csv'
            if os.path.isfile(file_O_disp):
                disp_O = load_disp_data_from_csv(file_O_disp)
                find_O = True
                print('Found O displacement data!')
            else:
                find_O = False
                print('No O displacement data was found! Will do {} atom displacement only!'.format(disp_atom))
                
                    
                
        
#============ Disclaimer button ====================================================
#============ Connected to self.pushButton_8 =======================================
    def disclaimer(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("<b>Disclaimer</b><br>" \
        "This app was designed by Dr Tao Ma. Redistribution and use in source, " \
        "with or without modification, are permitted. Any redistribution must remain "\
        "the above copyright. When a scientific publication is reached through the "\
        "app, please add the following reference: <br>"\
        "1. Ma, T. et al. <a href=\"https://doi.org/10.1103/PhysRevLett.123.217602\">Phys. Rev. Lett. 123, 217602 (2019).</a>"\
        "<br>"\
        "2. Ma, T. et al. <a href=\"https://doi.org/10.1063/1.5115039\">Appl. Phys. Lett. 115, 122902 (2019).</a>"
        "<br>" \
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND.<br>")
        msg.setWindowTitle(ver + ": Disclaimer")

        
        def disclaimerButtonClick():
            msg = QMessageBox()
            msg.setText('Thanks for using VecMap')
            msg.setWindowTitle('Thank you!')
            returnValue = msg.exec()
        
        msg.buttonClicked.connect(disclaimerButtonClick)

        returnValue = msg.exec()

#============ About button ====================================================
#============ Connected to self.pushButton_9 =======================================
    def show_about(self):
        msg = QMessageBox()
#        msg.setIcon(QMessageBox.Information)
        msg.setText("VecMap: a convenient tool to calculate atomic displacements in perovskite structures"\
                    "<br>"\
                    "This app was designed by Dr. Tao Ma"\
                    "<br>"\
                    "Version: {}  Released: {}"\
                    "<br>"\
                    "Hope you get good results and publications from it!"\
                    "<br>"\
                    "Get more information and source code from <a href=\"https://github.com/matao1984/vec-map\">here</a>.".format(ver, r_date))
        msg.setWindowTitle(ver + ": About")

        returnValue = msg.exec()


#============ Acknowledgments button ====================================================
#============ Connected to self.pushButton_10 =======================================
    def acknowledgments(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This program was written with Python 3. The author " \
                    "acknowledges the HyperSpy and Atomap packages which "\
                    "are partially incorporated in the program. Please "\
                    "consider citing/adding acknowledgement for Hyperspy "\
                    "and Atomap packages in your publication:"\
                    "<br>"
                    "Peña, F. de la et al. <a href=\"http://doi.org/10.5281/zenodo.3396791\">hyperspy/hyperspy: HyperSpy v1.5.2 (2019).</a>" \
                    "<br>"
                    "Nord, M. et al. <a href=\"https://doi.org/10.1186/s40679-017-0042-5\">Adv. Struct. Chem. Imaging 3, 9 (2017).</a>")
        msg.setWindowTitle(ver + ": Acknowledgments")

        returnValue = msg.exec()
        
#============ Contact button ====================================================
#============ Connected to self.pushButton_11 =======================================
    def show_contact(self):
        msg = QMessageBox()
        msg.setText("Ask questions and report bugs to:"\
                    "<br>"
                    "<a href=\"mailto:matao1984@gmail.com\">matao1984@gmail.com</a>")
        msg.setWindowTitle(ver + ": Contact")

        returnValue = msg.exec()
        
#============ Donate me button ====================================================
#============ Connected to self.pushButton_12 =======================================
    def donate(self):
        msg = QMessageBox()
        msg.setText("I will make this app freely available for the society.<br>"\
                    "If you like this app, show your appreciation and <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=NQTP8WZX9VDRQ&currency_code=USD&source=url\">buy me a lunch!</a>"\
                    "<br>"\
                    "Your support is my motivation!")
        msg.setWindowTitle(ver + ": Buy me a LUNCH!")

        returnValue = msg.exec()

        
#=========== Define figure canvas ===================================================
class PlotCanvas(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(ver + ': Plot')

        self.create_main_frame()
        
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)
       
        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

#==================== Find separation canvas =========================================
class SeparationCanvas(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(ver + ': Find separation factors')

        self.create_main_frame()
        
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        # Create the mpl Figure and FigCanvas objects. 
        # 10x10 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((10.0, 10.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        # Add a 9x9 axes layout 
        #
        self.axes = [self.fig.add_subplot(3,3,n) for n in range(1,10)]
        self.fig.set_tight_layout(True)
       
        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

       

#==================== Modules and helper functions ===================================

 
from hyperspy.io import load
from atomap.atom_finding_refining import get_atom_positions
from atomap.sublattice import Sublattice
from atomap.tools import remove_atoms_from_image_using_2d_gaussian
import os
import numpy as np
import matplotlib.pyplot as plt
import math
import copy
from scipy.spatial import distance
from matplotlib_scalebar.scalebar import ScaleBar

#====Helper functions, do not change====
def readImage(file):
    #Load raw image file for process.
    #Require Hyperspy package
    s = load(file)
    return s
    

def getDirectory(file, s='.'):
    #Make the working directory and return the path.
    for idx in range(-1, -len(file), -1): 
        if file[idx] == s: #find the file extension and remove it. '/' for parent path
            path = file[:idx] + '/'
            return path
        
def getFileName(file):
    full_name = getDirectory(file)
    full_path = getDirectory(file, s='/')
    f_name = full_name[len(full_path):-1]
    return f_name

def norm_img(img):
    #Normalize an image from 0 to 1
    img_norm = (img - img.min())/(img.max()-img.min())
    return img_norm


def abf2haadf(img):
    #Invert the contrast for BF/ABF images. img is a 2d array.
    img1 = -1 * img
    img_invert = norm_img(img1)
    return img_invert

def find_atom(img, ini_pos, atom_name, atom_color='r'):
    #Refine atom positions for a sublattice
    #img: an array of image data; ini_pos: initial positions; atom_name: a string for name; atom_color: a string for color
    #img_110: For [110] image
    sublattice = Sublattice(ini_pos, image=img, color=atom_color, name=atom_name, fix_negative_values=True)
    sublattice.find_nearest_neighbors()
    sublattice.refine_atom_positions_using_center_of_mass(show_progressbar=False)
    sublattice.refine_atom_positions_using_2d_gaussian(show_progressbar=False)
    return sublattice #Return an atomap sublattice object


def find_neighboring_atoms(P, A, Ua, tol=1.3):
    # Define a function to find the neighboring atoms of P(x,y) from a list of atoms A.
    # P: a given atom (x,y); A: a list of atoms; Ua: A threashold in px, 0.707*a for [001] and 0.5*a for [110]
    x, y = P
    N = [a for a in A if (a[0]-x)**2 + (a[1]-y)**2 < (Ua * tol) **2] #A list to store the neighboring atoms
    N = sorted(N, key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)
    return N

def closest_node(node, nodes):
    #A function to find the closest node in an array
    closest_index = distance.cdist([node], nodes).argmin()
    return closest_index,nodes[closest_index]    

def line(p1, p2):
    #Find a line function from two points
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C
def intersection(L1, L2):
    #A function to find the intersection point of two lines
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

def math_center(a, b, c, d):
    #Define a function to find the mathematical center of four points, a, b, c, d
    #Find the diagonal of a
    M = [b,c,d]
    diag_idx = distance.cdist([a],M).argmax()
    L1 = line(a,M[diag_idx])
    del M[diag_idx]
    L2 = line(M[0],M[1])
    center = intersection(L1, L2)
    return center

def find_ideal_pos(A, B, Ua, scale, img_110=False):
    #calculate the ideal atomic positions for A in a un-distorted perovskite structure
    #A, B are lists of atom coordinates; Ua is the estimated lattice paramter in nm; scale is the image pixel size
    #return a list of tuples
    ideal_positions = []
    Neighbor_positions = []
    if not img_110: #calculate image [001]
        for atom in A:
            Neighbor = find_neighboring_atoms(atom,B,Ua / scale * 0.707)
            if len(Neighbor) == 4:
                ap_center = math_center(*Neighbor)
                ideal_positions.append(ap_center)
                Neighbor_positions.append(Neighbor) #Save neighbors for plotting 
        return ideal_positions, Neighbor_positions
    for atom in A:
        Neighbor = find_neighboring_atoms(atom,B,Ua / scale * 0.5)
        if len(Neighbor) == 2:
            ap_center = ((Neighbor[0][0]+Neighbor[1][0])/2,(Neighbor[0][1]+Neighbor[1][1])/2)
            ideal_positions.append(ap_center)
            Neighbor_positions.append(Neighbor)
    return ideal_positions, Neighbor_positions
    
def find_ideal_O_pos(A, B, Ua, scale, O = None, img_110=False, ref = None):
    #calculate the ideal atomic positions for O in a un-distorted perovskite structure
    #[001] images
    ideal_O_positions = []

    if not img_110:
        for atom in A:
            Neighbor = find_neighboring_atoms(atom,B,Ua / scale * 0.707)
            if len(Neighbor) == 4:
                n_0 = Neighbor.pop(0)
                n_1 = Neighbor.pop(closest_node(n_0, Neighbor)[0])
                n_2 = Neighbor.pop(closest_node(n_0,Neighbor)[0])
                n_3 = Neighbor.pop()
                o_0 = (n_0[0] + n_1[0]) / 2, (n_0[1] + n_1[1]) / 2
                ideal_O_positions.append(o_0)

                o_1 = (n_0[0] + n_2[0]) / 2, (n_0[1] + n_2[1]) / 2
                ideal_O_positions.append(o_1)

                o_2 = (n_1[0] + n_3[0]) / 2, (n_1[1] + n_3[1]) / 2
                ideal_O_positions.append(o_2)

                o_3 = (n_2[0] + n_3[0]) / 2, (n_2[1] + n_3[1]) / 2
                ideal_O_positions.append(o_3)

        ideal_O_positions = list(dict.fromkeys(ideal_O_positions))
        return ideal_O_positions
    #[110] images
    #B-site is the reference
    if ref == 'B-site':
        for atom in O:
            Neighbor = find_neighboring_atoms(atom, B, Ua / scale * 0.5)
            if len(Neighbor) == 2:
                O_pos = (Neighbor[0][0] + Neighbor[1][0]) / 2, (Neighbor[0][1] + Neighbor[1][1]) / 2
                ideal_O_positions.append(O_pos)
        return ideal_O_positions
    if ref == 'A-site':
        for atom in O:
            Neighbor = find_neighboring_atoms(atom, B, Ua / scale * 0.866)
            if len(Neighbor) == 4:
                ap_center = math_center(*Neighbor)
                ideal_O_positions.append(ap_center)
        return ideal_O_positions
            
def find_displacement(A, A_com, Ua, scale):
    #find atomic displacement of A
    #A_com, A are lists of atom coordinates; Ua is the estimated lattice paramter in nm; scale is the image pixel size
    disp = []
    for atom in A_com:
        arrow = closest_node(atom,A)[1] 
        vec_len = distance.euclidean(arrow,atom)
        if vec_len > 0.3 * Ua / scale:
            continue
        dx = arrow[0]-atom[0]
        dy = arrow[1]-atom[1]
    #calculate the displacement vector angle according to dx, dy. 
        if dy >= 0 and dx >= 0:
            vec_ang = math.degrees(math.atan(dy/dx)) 
        elif dy >= 0 and dx < 0:
            vec_ang = math.degrees(math.atan(dy/dx)) + 180
        elif dx < 0 and dy < 0:
            vec_ang = math.degrees(math.atan(dy/dx)) + 180
        else:
            vec_ang = 360 + math.degrees(math.atan(dy/dx))
        disp.append([arrow[0], arrow[1], dx, dy, scale*1000*vec_len, vec_ang])
    return disp

    
def set_arrow_color(vec_data, ang_lst, color_lst):
    color_lst = color_lst
    vec_data_color = copy.deepcopy(vec_data) #Make a copy so it does not modify the original list
    if len(ang_lst) == 1:
        for vec in vec_data_color:
            vec.append(color_lst[0]) #set yellow for single-color rendering
        return vec_data_color
    ang_lst_mod = [a - ang_lst[0] for a in ang_lst]
    ang_bond = []
    for idx in range(len(ang_lst_mod)-1):
        ang_bond.append((ang_lst_mod[idx + 1] - ang_lst_mod[idx]) // 2 + ang_lst_mod[idx])
    ang_bond.append((360 - ang_lst_mod[-1]) // 2 + ang_lst_mod[-1])
    for vec in vec_data_color:
        ang = vec[5] - ang_lst[0]
        if ang < 0:
            ang = ang + 360
        for i in range(len(ang_bond)-1):
            if round(ang) in range(ang_bond[i], ang_bond[i+1]):
                vec.append(color_lst[i+1])
    for vec in vec_data_color:
        if len(vec) == 6:
            vec.append(color_lst[0])
    return vec_data_color
        
def load_disp_data_from_csv(file):
    with open(file,'r') as disp:
        disp_data = []
        lines = disp.readlines()
        print('Displacement data:\n')
        print(lines[0])
        for lin in lines[1:]:
            lin_data = lin.strip().split(', ')
            disp_data.append([float(data) for data in lin_data[:6]])
        return disp_data
    

#====Application entry==================================
def main():
    print('='*50)
    print('''
          Welcome to the first version of VecMap 
          --- a convenient tool to calculate atomic displacements in perovskite structures
              
          This app was designed by Dr. Tao Ma. 
          Address your questions and suggestions to matao1984@gmail.com.
          Please see the "Disclaimer" before use!
          Hope you get good results and publications from it!
          ''')
                
    print('          Version: ' + ver + ' Released: ' + r_date)
    print('='*50)
    import sys
    app = QtWidgets.QApplication(sys.argv)
#    app.setWindowIcon(QIcon("./icon.png"))
    VecMap = QtWidgets.QWidget()
    ui = Ui_VecMap()
    ui.setupUi(VecMap)
    VecMap.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

