# pypi-mirror

将 pypi 缓存文件夹链接到 /data。

配置 INTERVAL 环境变量可以控制更新频率，默认值是 3600 秒。

配置 CMD 环境变量可以配置需要运行的命令，如： `bandersnatch -c bandersnatch.conf mirror --force-check`
