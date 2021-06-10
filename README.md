# DBMS FINAL PROJECT
contributed by <`徐郁淞 P76091543`>

## 目標：
* 學習使用SQL指令
* 使用現成資料庫(MySQL, …)，開發一個簡易且人性化的DBMS
  * (如：人事薪資系統、學生學籍系統、醫療管理系統、圖書管理系統……可自行發揮)
* 分組
  * 一人一組

## 應用場景
* 建立遊戲帳戶資料庫
* 使用遊戲資料庫來記錄各個帳號所創立的角色，街道的任務，公會系統等等。

## 實作軟體說明
* 系統介面(GUI): `PyQt`
* 系統資料庫：`MySQL`
* 實作語言：`python`

## 介面說明
![](gui_picture/GUI.png)

### 帳戶功能
<p align="center">
<img src="gui_picture/account.png" alt="drawing" width="400"/>
</p>

**創建帳戶**
* BUTTON
  * 輸入帳號
  * 輸入密碼
  * 輸入電子郵件
  * 點擊右方`創建帳戶`按鈕

* QUERY
需替換[帳號], [密碼], [電子郵件]
(e.g. `'john_account'`, `'john_password'`, `'john@gmail.com'`)
```
INSERT INTO Account (Account_number, Password, Email) VALUES ([帳號], [密碼], [電子郵件])

// e.g. 
// INSERT INTO Account (Account_number, Password, Email) VALUES ('john_account', 'john_password', 'john@gmail.com')
```


**創建角色**
* BUTTON
  * 輸入帳號
  * 輸入角色名字
  * 輸入職業

* QUERY
  * 需替換 `%s`

```
INSERT INTO  Role (Cname, Occupation, Speed, HP, MP, Power, Anumber, Gname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

// e.g.
// INSERT INTO  Role (Cname, Occupation, Speed, HP, MP, Power, Anumber, Gname) VALUES ('john_role', 'worrier', '200', '300', '300', '400', 'john_account', 'noob')
```

### 公會功能
<p align="center">
<img src="gui_picture/guild.png" alt="drawing" width="400"/>
</p>

**建立公會**
* BUTTON
  * 輸入角色名字
  * 輸入公會名稱
  * 輸入公會地址
  * 點擊右方`建立公會`

* QUERY
  * 需替換 [公會名稱], [公會地址], [公會等級],[角色名字]
  * (e.g. `'noob_guild'`, `'green_island'`, `'1'`, `'john'`)

```
INSERT INTO Guild (Gname, Address, Level, Cname) VALUES ([公會名稱], [公會地址], [公會等級],[角色名字])

// e.g.
// INSERT INTO Guild (Gname, Address, Level, Cname) VALUES ('noob_guild', 'green_island', '1', 'john')
```


**加入公會**
* BUTTON
  * 輸入角色名字
  * 輸入公會名稱
  * 點擊右方`加入公會`

* QUERY
  * 需替換 [公會名字]、[角色名字]
  * (e.g. `'noob_guild'`, `john`)

```
UPDATA Role SET Gname=[公會名字] WHERE Cname=[角色名字]

// e.g.
// UPDATA Role SET Gname='noob_guild' WHERE Cname='john'
```

**查看公會**
* BUTTON
  * 輸入公會名稱
  * 點擊右方`查看公會`

* QUERY
  * 需替換[公會名字]
  * (e.g. 'noob_guild')
```
SELECT * FROM Role WHERE Gname IN ([公會名字])"

// e.g.
// SELECT * FROM Role WHERE Gname IN ('noob_guild')
// 
```

### 任務功能
<p align="center">
<img src="gui_picture/task.png" alt="drawing" width="400"/>
</p>

**建立任務**
* BUTTON
  * 輸入角色名字
  * 輸入任務名稱
  * 點擊右方`建立任務`

* QUERY
  * 需替換 `%s`

```
INSERT INTO Task (Tname, Reward, Cname) VALUES (%s, %s, %s)

// e.g.
// INSERT INTO Task (Tname, Reward, Cname) VALUES ('travel_task', '100', 'john')
```

**查看任務**
* BUTTON
  * 輸入角色名字
  * 點擊右方`查看任務`

* QUERY
  * 需替換[角色名字]
  * e.g.('john')

```
SELECT * FROM Task WHERE Cname = [角色名字]

// e.g.
// SELECT * FROM Task WHERE Cname = 'john'
```

## 寵物功能
<p align="center">
<img src="gui_picture/pet.png" alt="drawing" width="400"/>
</p>

**豢養寵物**
* BUTTON
  * 輸入角色名字
  * 寵物名字
  * 點擊右方`豢養寵物`

* QUERY
  * 需替換 `%s`

```
INSERT INTO Pet (Pname, Hungry, Cname) VALUES (%s, %s, %s)

// e.g.
// INSERT INTO Pet (Pname, Hungry, Cname) VALUES ('john_pet', '100', 'john')
```

**查看寵物**
* BUTTON
  * 輸入角色名字
  * 點擊右方`查看寵物`

* QUERY
  * 需替換[寵物名字]
  * e.g.('john')

```
SELECT * FROM Pet WHERE Cname = [寵物名字]

// e.g.
// SELECT * FROM Pet WHERE Cname = 'john'
```

## Complex queries in SQL 
<p align="center">
<img src="gui_picture/advance.png" alt="drawing" width="400"/>
</p>

* 查看其他公會的人數,平均血量,最大血量,最小血量,全體總血量

```
select Guild.Gname, Count(Role.Cname), AVG(HP), MAX(HP), MIN(HP),SUM(HP) from Guild, Role WHERE Guild.Gname=Role.Gname AND Guild.Gname NOT IN ('gura') group by guild.gname;
```

* 查看哪些角色有接報酬大於 1000 的任務
```
select cname from Role where exists (select * from task where Reward > 1000);
```

* 查看哪些角色都讓自己的寵物挨餓
```
select cname from Role where not exists (select * from pet where Hungry > 200);
```

* 查看公會人數大於 10 人的公會人數

```
select COUNT(Cname), Gname FROM Role GROUP BY Gname HAVING COUNT(Cname) > 2;
```

## ER diagram
![](database_Diagram_final.png)

## 第三正規化後的 Relational Schema
![](relation_schema.png)
* 說明意義和關係
  1. 帳戶(Account):
     * 一個帳戶可建立多個角色(Role)
  2. 玩家角色(Role):
     * 每個角色可擁有寵物(Pet)以及任務(Task)，每個角色可管理參與以及管理公會 
  3. 任務(Task)
     * 每個任務可被一個角色(Role)所擁有
  4. 寵物(Pet)
     * 每個寵物可被一個角色(Role)所擁有
  5. 公會(Guild)
     * 公會可被一個玩家角色(Role)管理，可以有多個玩家角色(Role)參與公會



