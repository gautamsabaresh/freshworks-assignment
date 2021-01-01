import datastore_manipulation as x
from threading import Timer


def fun():
    re = x.read("tobekilled")
    print(re)


x.create("abc", {"hi": "12344"})
x.create("tobekilled", {"obj1": "gautam"}, 25)
res = x.read("tobekilled")
print(res)
t = Timer(20, fun)
t.start()




