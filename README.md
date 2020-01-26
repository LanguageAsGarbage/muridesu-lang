## muridesu

听说最近有人想用Python编译器骗经费?

还用的是**PLY**?! 这都0202年了我的天.

您好，这儿是一位不愿透露姓名的你红姐制作的一个木兰那样的语言, 学你们木兰,
**只有前端, 编译到Python**.

居然用了我**三个小时零28分钟**！加上从QQ里爬出来开机建项目的时间.

语法如下，见`excuse_me.muridesu`.

```go
func f(x, seq){
    for i in seq
    {
        print(i + x)
    }
}

f(1, [2, 3, 4])

class A {
    func f(self){
        print("A")
    }
}
class S <: A {
    func g(self){
        print("S")
    }
}

S().g()
S().f()
```

编译到`.pyc`:

```shell script
λ> muridesu excuse_me.muridesu excuse_me.pyc                                                                           
λ> python excuse_me.pyc
3
4
5
S
A
```

我们支持了什么呢?

请看`muridesu.exrbnf`.

语句:
- `import`
- `try`, `except`(这里改成了`catch`, 因为搞点新东西), `finally`.
- `assert`
- `global`
- `nonlocal`
- `break`
- `continue`
- `with`, `with A as B, ...`
- `for ... in`
- `class Name <: Base1, Base2`
- `meta 你的Type构造器 class Name <: Base1, Base2`
- `return`, `return expr`
- `if`
- 函数定义`func`(让我们学学木兰?)
- 解构`(a, b, [c, d, (f, g, h)]) = ...`

表达式:
- lambda: `fn args... -> expr`
- bool表达式 `and, or, not`
- 比较: `<, >, ...`(Python所有的)
- 二元运算(Python所有的, 懒得实现优先级了, 毕竟这只是个迫害项目)
- 单目运算(`-`, `~`)
- `yield`, `yield from`
- `set`, `dict`没有字面量, 但参考julia, 引入广泛可扩展的构造方式: `set [1, 2, 3]`, `dict [1 => 2, 2 => 3]`.
- 其他的Python字面量, 除comprehensions

注: Python中的`a[b]`在muridesu中是`a.[b]`, 因为我的想法是`A[b, c, d]`表示`A_list([b, c, d])`, `A"string"`表示`A_str("string")`.

基本上接近Python的全集了.


所有说编译到Python AST真的是很简单的，不能让他骗经费是对的。

Python牛逼的编译器应该是这里这样的:
- [FINISHED: 丰富的模式匹配, 尾递归优化, 自定义算符优先级, let绑定控制作用域](https://github.com/RemuLang/urgent-lang)
- [FINISHED: 易用的Python字节码代码生成后端, 提供Label as Value(实现stackless coroutine), Switch(不是嵌套if-else)](https://github.com/RemuLang/sijuiacion-lang)
- [WIP: HM类型系统扩展, Extensible Records等强力的静态语言特性](https://github.com/RemuLang/proud)
