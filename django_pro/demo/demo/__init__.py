import pymysql

# 解决mysql的驱动问题；
# 伪装成mysqlclient 和 mysql-python
# mysqlclient 对python2, 3都支持,但是对mysql安装有要求, 必须制定位置存在配置文件; mysql-python 支支持Python2 不支持python3.
pymysql.install_as_MySQLdb()
