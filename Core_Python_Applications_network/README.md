##注意事项

---

* Python 3中bytes和str类型的区别

> 在Python3中最重要的特性之一就是对字符串和二进制数据流作了明确的区分，文本总是```Unicode```，由```str```类型表示，二进制数据则由```bytes```类型表示。
> 在Python3中，不会以任意隐式的方式混用```str```和```bytes```，你不能拼接字符串和字节流，也无法在字节流里搜索字符串，也不能将字符串传入参数为字节流的函数。

* bytes和str之间的相互转换
> 通过下面的示例来解释为了要使用```encode```和```decode```。

```
>>> s = '中文'
>>> s
'中文'
>>> type(s)
<class 'str'>
>>> b = bytes(s, encoding='utf-8')
>>> b
b'\xe4\xb8\xad\xe6\x96\x87'
>>> type(b)
<class 'bytes'>
>>> b = s.encode()
>>> b
b'\xe4\xb8\xad\xe6\x96\x87'
>>> s = b.decode()
>>> s
'中文'
>>> s = b
>>> s
b'\xe4\xb8\xad\xe6\x96\x87'
>>> type(b.decode())
<class 'str'>

```
> 由此可见```str```向```bytes```的转换可使用方法```encode()```
> 而```bytes```向```str```的转换可使用方法```decode()```