# VolunteerEZgo 志工EZgo
## 架構
前端：Vue <br>後端：Python-FastAPI <br>資料庫：MariaDB 
## started
[virtualenvwrapper教學](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/91986/)
```
pip install virtualenv #安裝virtualenv
pip install virtualenvwrapper-win #安裝wrapper
#wrapper only run in cmd,powershell doesn't work.
lsvirtualenv  #顯示現有虛擬環境(根據WORKON_PATH)
cdvirtualenv #移動至虛擬環境資料夾
workon <venv_name> #啟用虛擬環境
deactive #退出虛擬環境
```
## run test
Vue
```
/frontend
npm run serve
```

FastAPI
```
/Backend/src
uvicorn main:app --reload
```
### 