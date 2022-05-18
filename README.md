# vec-map
VecMap is a convenient and lightweight tool to calculate the atomic displacements in some polarized materials such as perovskite. The tool was written by Dr. Tao Ma. For questions and suggestions, please send a message to matao1984@gmail.com.

## 1. Installation
The tool requires Python 3 environment. I recommend to install Anaconda which is the most straightforward way. Download and install the Python 3 version of Anaconda from here: https://www.anaconda.com/.

After the Anaconda is installed, open the Anaconda prompt console. Run the following commands:

### 1.1 Create a virtual environment for the VecMap with python version = 3.8
```
conda create -n vecmap python=3.8
```
### 1.2 Activate the virtual environment
```
conda activate vecmap
```
### 1.3 Install git 
Navigate to a desired loaction on your hard disk (e.g., C:/Users/xxx/Documents) and download the installation files from the github. Replace the "xxx" with your actual user name.
```
cd c:/Users/xxx/Documents
git clone "https://github.com/matao1984/vec-map" vecmap
```

In case you don't have git installed, run the following script:

```
conda install git -c anaconda
```

If git raises an error about an existing "vecmap" folder, delete it and retry.
Then navigate to the folder that was just downloaded, and run the setup script:

```
cd c:/Users/xxx/Documents/vecmap
pip install -e ./
```

If other errors happen in the installation, most likely they are related to ``hyperSpy`` or ``atomap`` packages which are the main dependencies. It is worth trying in the Anaconda console to install them first: ``pip install hyperspy atomap``.

## 2. Usage
To run the app from anaconda cmd window:

```
conda activate vecmap
vecmap
```

A GUI will pop up.

In the Windows system, you can create a bat file with the following content:

```
@echo off
CALL  C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3\envs\vecmap
vec-map
echo on 
```

Replace the path and environment name if they are different in your system. Save this bat, e.g., "VecMap App.bat", on your desktop and double-click it to run the app. Note that you can name this bat file in any strings EXCEPT FOR "vecmap.bat", otherwise it will go into an infinite loop when you run it!
