# scf-lighthouse-snapshot

利用云函数，自动为腾讯轻量应用服务器创建快照。可以为云函数设置定时触发以定期自动更新快照。

运行此脚本会占用一个快照配额，使用前请确保快照配额有空余。默认快照名称为`SCF-Snapshot-实例ID`。

## 环境变量

| 变量名称    | 描述             |
| ----------- | ---------------- |
| SECRET_ID   | API密钥SecretId  |
| SECRET_KEY  | API密钥SecretKey |
| REGION      | 服务器地域       |
| INSTANCE_ID | 服务器实例ID     |

### 服务器地域列表

| 地域描述             | 地域名称         |
| -------------------- | ---------------- |
| 华北地区(北京)       | ap-beijing       |
| 西南地区(成都)       | ap-chengdu       |
| 华南地区(广州)       | ap-guangzhou     |
| 港澳台地区(中国香港) | ap-hongkong      |
| 华东地区(上海)       | ap-shanghai      |
| 东南亚地区(新加坡)   | ap-singapore     |
| 欧洲地区(法兰克福)   | eu-frankfurt     |
| 美国西部(硅谷)       | na-siliconvalley |
| 亚太地区(孟买)       | ap-mumbai        |
| 欧洲地区(莫斯科)     | eu-moscow        |
| 亚太地区(东京)       | ap-tokyo         |
| 华东地区(南京)       | ap-nanjing       |
