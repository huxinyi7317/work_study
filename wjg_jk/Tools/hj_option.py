 
import os

def pip_all():
    libs = {"selenium", "requests","pywin32","PyAutoIt",
    "Appium-Python-Client","PyMySQL","PyUserInput","locust",
    "xlrd"}
    
    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system("pip install " + lib)
            print("{} install successful".format(lib))
        print("All Successful")
    except:
        print("第三方库安装失败")

if __name__ == "__main__":
    pip_all()