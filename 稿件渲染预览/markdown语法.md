
# 这是一级标题

## 这是二级标题

### 这是三级标题

#### 这是四级标题

##### 这是五级标题

###### 这是六级标题

**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~
>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容
---
---

![天空之城](https://cdn-hz.skypixel.com/uploads/cn_files/photo/image/3edc3097-6708-4d59-8a0e-0cf827bde8f2.JPG@!1920 "天空之城")

另一种超链接写法：[链接名][链接代号]

[here][3]
然后在别的地方定义 3 这个详细链接信息，

[3]: https://cdn-hz.skypixel.com/uploads/cn_files/photo/image/15916e69-234a-4b77-9a38-bfa82197c91c.JPG@!1920 "秋"

直接展示链接的写法：<http://www.izhangbo.cn>

[简书](http://jianshu.com)
[百度](http://baidu.com)
[超链接名](超链接地址 "超链接title")


<video width="100%" controls="controls">
    <source src="https://us-videos.dji.net/video_trans/aa59483be0b34052ba62c4430ad966ef/720.mp4">
</video>

<audio controls="controls" src="https://s128.xiami.net/978/978/4905/59454_1511602653251.mp3?ccode=xiami_web_web&expire=86400&duration=271&psid=bd764e41cbf65a52e853a71ed27f0950&ups_client_netip=222.89.18.128&ups_ts=1584274605&ups_userid=0&utid=VonxFtn1e34CAasMvf40aPYk&vid=59454&fn=59454_1511602653251.mp3&vkey=Bd3064b5fadf46e0939f440bb7af34458">
</audio>

<i class="iconfont icon-github"></i> 图标文字

- 列表内容
+ 列表内容
* 列表内容

注意：无序列表用 - + * 任何一种都可以，- + * 跟内容之间都要有一个空格

1. 列表内容
2. 列表内容
3. 列表内容

注意：序号跟内容之间要有空格

表头|表头|表头
---|--:|---:
内容|内容|内容
内容|内容|内容

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右

注：原生的语法两边都要用 | 包起来。此处省略

~~~c
#include<stdio.h>
int main(void){
    printf("Hello World.\n");
}
~~~

流程图

```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```

>- 块引用里使用列表，需要和上面的内容隔开一个空行
>- 记得加空格哦。

任务列表
- [x] 完成更改
- [ ] 推送提交到 GitHub
- [ ] 打开拉取请求