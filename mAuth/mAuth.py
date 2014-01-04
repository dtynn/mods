#coding=utf-8
import time


class miniAuth(object):
    def __init__(self, sqlRead, sqlWrite):
        self.sqlRead = sqlRead
        self.sqlWrite = sqlWrite
        self.tableInit()
        return

    def tableInit(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS `user_basic` (
            `uid`  int(10) NOT NULL AUTO_INCREMENT,
            `email`  varchar(150) NULL,
            `nick`  varchar(50) NULL,
            `password`  varchar(50) NULL,
            `status`  smallint(3) NOT NULL DEFAULT 0,
            `locked`  smallint(1) NOT NULL DEFAULT 0,
            `register_time`  int(12) NOT NULL,
            `register_ip`  varchar(50) NOT NULL,
            PRIMARY KEY (`uid`),
            UNIQUE INDEX `_nick` (`nick`),
            UNIQUE INDEX `_email` (`email`)
        )
        ;
        '''
        res = self.sqlWrite.execute(sql)
        return res

    def userNew(self, email, password, ip):
        return