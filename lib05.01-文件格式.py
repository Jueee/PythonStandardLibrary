'''
文件格式

本章将描述用于处理不同文件格式的模块.


5.1.1. Markup 语言

Python 提供了一些用于处理可扩展标记语言( Extensible Markup Language ,XML ) 和超文本标记语言( Hypertext Markup Language , HTML )的扩展. 
Python 同样提供了对标准通用标记语言( Standard Generalized Markup Language ,SGML )的支持.

所有这些格式都有着相同的结构, 因为 HTML 和 XML 都来自 SGML . 
每个文档都是由起始标签( start tags ), 结束标签( end tags ), 文本(又叫字符数据), 以及实体引用( entity references )构成:

<document name="sample.xml">
	<header>This is a header</header>
	<body>This is the body text. The text can contain
	plain text (&quot;character data&quot;), tags, and
	entities.
	</body>
</document>

在这个例子中, <document> , <header> , 以及 <body> 是起始标签. 
每个起始标签都有一个对应的结束标签, 使用斜线 "/ " 标记. 
起始标签可以包含多个属性, 比如这里的 name 属性.

起始标签和它对应的结束标签中的任何东西被称为元素( element ) . 
这里 document 元素包含 header 和 body 两个元素.

&quot; 是一个字符实体( character entity ). 
字符实体用于在文本区域中表示特殊的保留字符, 使用 & 指示. 
这里它代表一个引号, 常见字符实体还有 "< ( &lt; ) " 和 " > ( &gt; ) " .

虽然 XML , HTML , SGML 使用相同的结构块, 但它们还有一些不同点. 
在 XML 中, 所有元素必须有起始和结束标签, 所有标签必须正确嵌套( well-formed ).
而且 XML 是区分大小写的, 所以 <document> 和 <Document> 是不同的元素类型.

HTML 有很高灵活性, HTML 语法分析器一般会自动补全缺失标签; 例如, 当遇到一个以 <P> 标签开始的新段落, 却没有对应结束标签, 语法分析器会自动添加一个 </P> 标签. HTML 也是区分大小写的. 
另一方面, XML 允许你定义任何元素, 而 HTML 使用一些由 HTML 规范定义的固定元素.

SGML 有着更高的灵活性, 你可以使用自己的声明( declaration ) 定义源文件如何转换到元素结构, DTD ( document type description , 文件类型定义)可
以用来检查结构并补全缺失标签. 
技术上来说, HTML 和 XML 都是 SGML 应用, 有各自的 SGML 声明, 而且 HTML 有一个标准 DTD .

Python 提供了多个 makeup 语言分析器. 
由于 SGML 是最灵活的格式, Python 的 sgmllib 事实上很简单. 
它不会去处理 DTD , 不过你可以继承它来提供更复杂的功能.

Python 的 HTML 支持基于 SGML 分析器. 
htmllib 将具体的格式输出工作交给 formatter 对象. 
formatter 模块包含一些标准格式化标志.

Python 的 XML 支持模块很复杂. 
先前是只有与 sgmllib 类似的 xmllib , 后来加入了更高级的 expat 模块(可选). 而最新版本中已经准备废弃 xmllib , 启用 xml 包作为工具集.


5.1.2. 配置文件

ConfigParser 模块用于读取简单的配置文件, 类似 Windows 下的 INI 文件.
netrc 模块用于读取 .netrc 配置文件, shlex 模块用于读取类似 shell 脚本语法的配置文件.


5.1.3. 压缩档案格式

Python 的标准库提供了对 GZIP 和 ZIP ( 2.0 及以后) 格式的支持. 
基于 zlib 模块, gzip 和 zipfile 模块分别用来处理这类文件.

'''