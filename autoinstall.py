#自动安装所有库
import os
os.system('pip freeze > requirements.txt')
os.system('pip install -r requirements.txt')
os.remove('requirements.txt')