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
            `activated`  smallint(1) NOT NULL DEFAULT 0,
            `locked`  smallint(1) NOT NULL DEFAULT 0,
            `register_time`  int(12) NOT NULL,
            `register_ip`  varchar(50) NOT NULL,
            PRIMARY KEY (`uid`),
            UNIQUE INDEX `_nick` (`nick`),
            UNIQUE INDEX `_email` (`email`)
        )
        '''
        res = self.sqlWrite.execute(sql)
        return res

    def userInsert(self, email, password, ip):
        sql = '''
        INSERT INTO user_basic
        (email, password, register_time, register_ip)
        VALUES ("%s", "%s", %s, "%s")
        '''
        now = int(time.time())
        res = self.sqlWrite.execute(sql, email, password, now, ip)
        return res

    def userGetAll(self):
        sql = '''
        SELECT uid, email, nick, status, activated, locked, register_time, register_ip
        FROM user_basic
        '''
        res = self.sqlRead.query(sql)
        return res

    def userGet(self, uid=None, email=None):
        if uid is not None:
            return self.userGetById(uid)
        elif email is not None:
            return self.userGetByEmail(email)
        return

    def userGetById(self, uid):
        sql = '''
        SELECT uid, email, nick, status, activated, locked, register_time, register_ip
        FROM user_basic
        WHERE uid=%s
        '''
        res = self.sqlRead.get(sql, uid,)
        return res

    def userGetByEmail(self, email):
        sql = '''
        SELECT uid, email, nick, status, activated, locked, register_time, register_ip
        FROM user_basic
        WHERE email = "%s"
        '''
        res = self.sqlRead.get(sql, email,)
        return res

    def userLock(self, uid=None, email=None):
        if uid is not None:
            return self.userLockById(uid)
        elif email is not None:
            return self.userLockByEmail(email)
        return

    def userLockById(self, uid):
        sql = '''
        UPDATE user_basic
        SET locked=1
        WHERE uid=%s AND locked=0
        '''
        res = self.sqlWrite.execute_rowcount(sql, uid)
        return res > 0

    def userLockByEmail(self, email):
        sql = '''
        UPDATE user_basic
        SET locked=1
        WHERE email="%s" AND locked=0
        '''
        res = self.sqlWrite.execute_rowcount(sql, email)
        return res > 0

    def userUnlock(self, uid=None, email=None):
        if uid is not None:
            return self.userUnlockById(uid)
        elif email is not None:
            return self.userUnlockByEmail(email)
        return

    def userUnlockById(self, uid):
        sql = '''
        UPDATE user_basic
        SET locked=0
        WHERE uid=%s AND locked=1
        '''
        res = self.sqlWrite.execute_rowcount(sql, uid)
        return res > 0

    def userUnlockByEmail(self, email):
        sql = '''
        UPDATE user_basic
        SET locked=0
        WHERE email="%s" AND locked=1
        '''
        res = self.sqlWrite.execute_rowcount(sql, email)
        return res > 0

    def userActivate(self, uid=None, email=None):
        if uid is not None:
            return self.userActivateById(uid)
        elif email is not None:
            return self.userActivateByEmail(email)
        return

    def userActivateById(self, uid):
        sql = '''
        UPDATE user_basic
        SET activated=1
        WHERE uid=%s AND activated=0
        '''
        res = self.sqlWrite.execute_rowcount(sql, uid)
        return res > 0

    def userActivateByEmail(self, email):
        sql = '''
        UPDATE user_basic
        SET activated=1
        WHERE email="%s" AND activated=0
        '''
        res = self.sqlWrite.execute_rowcount(sql, email)
        return res > 0