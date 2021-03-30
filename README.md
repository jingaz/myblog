网站基于 Django3.0.4，用uwsgi+nginx部署。

用了博主[一叶斋](https://xieguanglei.github.io/)的样式表。

开启virtualenv环境，在本地先测试一下： python manage.py runserver 如果成功就可以进行部署。
项目的根文件夹 在 **/var/www/** 下。

首先给nginx创建配置文件

~~~
vim /etc/nginx/conf.d/myblog.conf
~~~

内容如下：

~~~
server {
	listen 443 ssl;
	server_name ljwonder.com;
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;
	charset utf-8;
	ssl on;
	ssl_certificate /var/www/ssl_path/full_chain.pem;
	ssl_certificate_key /var/www/ssl_path/private.key;

	location /{
		include /var/www/myblog/uwsgi_params;
		uwsgi_connect_timeout 30;
		uwsgi_pass unix:/var/www/myblog/script/uwsgi.sock;
		}

	location /static/ {
		alias /var/www/myblog/static/;
		}

	location /media/ {
		alias /var/www/myblog/media/;
		}
	}
server {
    listen 80;
    server_name  ljwonder.com  www.ljwonder.com;
    rewrite ^(.*) https://ljwonder.com$1 permanent;
}
~~~

第8、9行的full_chain.pem和private.key是在[FreeSSl](https://freessl.cn/)用**浏览器**生成的。


然后开启virtualenv环境 source bin/activate
进入srcip目录，执行

~~~
uwsgi --ini uwsgi.ini   # 启动uwsgi配置
~~~

行了。

附带几个nginx uwsgi常用命令

~~~
~/myblog/script$ sudo /etc/init.d/nginx start   # 启动nginx
~/myblog/script$ sudo /etc/init.d/nginx stop    # 停止nginx
~/myblog/script$ sudo /etc/init.d/nginx restart # 重启nginx
~/myblog/script$ sudo /etc/init.d/nginx reload  # 重新载入nginx配置,影响比较小，适合运行中的服务。
~/myblog/script$ sudo killall nginx

$ uwsgi --ini uwsgi.ini   # 启动uwsgi配置
$ uwsgi --stop uwsgi.pid  # 关闭uwsgi
$ uwsgi --reload uwsgi.pid  #重新加载配置

$ ps -ef | grep uwsgi
~~~

---
---
后台上传原始markdown格式的稿件之前，可以用浏览器打开*渲染预览.html* **预览网页显示效果。**