#coding=utf-8
from mDBs import Connection
from mAuth import miniAuth
from uuid import uuid4

conn = Connection('localhost', 'test', 'root', '3520936')

mA = miniAuth(conn, conn)
email = uuid4().hex
email2 = uuid4().hex
uid = mA.userInsert(email, email, email)
uid2 = uid * 10

print "Email: %s" % (email, )
print "uid: %s" % (uid, )
print "GetById: %s" % (bool(mA.userGetById(uid)), )
print "GetByEmail: %s" % (bool(mA.userGetByEmail(email)), )
print "LockById: %s" % (mA.userLock(uid=uid),)
print "UnlockById: %s" % (mA.userUnlock(uid=uid),)
print "LockByEmail: %s" % (mA.userLock(email=email),)
print "UnlockByEmail: %s" % (mA.userUnlock(email=email),)
print "ActivateById: %s" % (mA.userActivate(uid=uid),)
print "ActivateByEmail: %s" % (mA.userActivate(email=email),)
print "NoUserById: %s" % (mA.userGet(uid=uid2))
print "NoUserByEmail: %s" % (mA.userGet(email=email2))