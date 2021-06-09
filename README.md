# DBMS FINAL PROJECT
contributed by <`徐郁淞 P76091543`>

## 目標：
* 學習使用SQL指令
* 使用現成資料庫(MySQL, …)，開發一個簡易且人性化的DBMS
  * (如：人事薪資系統、學生學籍系統、醫療管理系統、圖書管理系統……可自行發揮)
* 分組
  * 一人一組

## 實作軟體說明
* 系統介面(GUI): `PyQt`
* 系統資料庫：`MySQL`
* 實作語言：`python`

## 介面說明

### 角色功能
#### 創建帳戶
* 輸入帳號
* 輸入密碼
* 輸入電子郵件
* 點擊右方`創建帳戶`按鈕

#### 創建角色
* 輸入帳號
* 輸入角色名字
* 輸入職業

### 公會功能
#### 建立公會
* 輸入角色名字
* 輸入公會名稱
* 輸入公會地址
* 點擊右方`建立公會`

#### 加入公會
* 輸入角色名字
* 輸入公會名稱
* 點擊右方`加入公會`

* sql instruction:
```
sql = INSERT INTO Guild (Gname, Address, Level, Cname) VALUES (%s, %s, %s, %s)
```