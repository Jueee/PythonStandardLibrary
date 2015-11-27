'''
网络协议

本章描述了 Python 的 socket 协议支持以及其他建立在 socket 模块上的网络模块. 
这些包含了对大多流行 Internet 协议客户端的支持, 以及一些可用来实现 Internet 服务器的框架.

将使用两个协议作为样例: Internet TimeProtocol ( Internet 时间协议 ) 以及 Hypertext Transfer Protocol (超文本传输协议, HTTP 协议).

'''

'''
7.1.1. Internet 时间协议

Internet 时间协议 ( RFC 868, Postel 和 Harrenstien, 1983) 可以让一个网
络客户端获得一个服务器的当前时间.
因为这个协议是轻量级的, 许多 Unix 系统(但不是所有)都提供了这个服务.
它可能是最简单的网络协议了. 服务器等待连接请求并在连接后返回当前时间
( 4 字节整数, 自从 1900 年 1 月 1 日到当前的秒数).

'''

'''
7.1.2. HTTP 协议


超文本传输协议 ( HTTP, RFC 2616 ) 是另个完全不同的东西. 最近的格式说明
书( Version 1.1 )超过了 100 页.

从它最简单的格式来看, 这个协议是很简单的. 客户端发送如下的请求到服务
器, 请求一个文件:

GET /hello.txt HTTP/1.0
Host: hostname
User-Agent: name
[optional request body , 可选的请求正文]

服务器返回对应的响应:

HTTP/1.0 200 OK
Content-Type: text/plain
Content-Length: 7
Hello

请求和响应的 headers (报头)一般会包含更多的域, 但是请求 header 中的
Host 域/字段是必须提供的.

header 行使用 "\r\n " 分割, 而且 header 后必须有一个空行, 即使没有正
文 (请求和响应都必须符合这条规则).
'''