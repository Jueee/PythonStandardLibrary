# 03-StandardLibrary
《Python Standard Library》学习笔记。  
###说明：
《Python标准库》原书为 Python2.X 版，在学习的过程中，把所遇到的标准库模块用 Python3.X 进行实现改写；部分无法改写的模块，进行了说明和跳过处理。
##《Python Standard Library》目录
###1. 核心模块                     
o  1.1. 介绍                    
o  1.2. _ _builtin_ _ 模块      
o  1.3. exceptions 模块         
o  1.4. os 模块                 
o  1.5. os.path 模块            
o  1.6. stat 模块               
o  1.7. string 模块             
o  1.8. re 模块                 
o  1.9. math 模块               
o  1.10. cmath 模块             
o  1.11. operator 模块          
o  1.12. copy 模块              
o  1.13. sys 模块               
o  1.14. atexit 模块            
o  1.15. time 模块              
o  1.16. types 模块             
o  1.17. gc 模块                
###2. 更多标准模块                 
o  2.1. 概览                    
o  2.2. fileinput 模块          
o  2.3. shutil 模块             
o  2.4. tempfile 模块           
o  2.5. StringIO 模块           
o  2.6. cStringIO 模块          
o  2.7. mmap 模块               
o  2.8. UserDict 模块           
o  2.9. UserList 模块           
o  2.10. UserString 模块        
o  2.11. traceback 模块         
o  2.12. errno 模块             
o  2.13. getopt 模块            
o  2.14. getpass 模块           
o  2.15. glob 模块              
o  2.16. fnmatch 模块           
o  2.17. random 模块            
o  2.18. whrandom 模块          
o  2.19. md5 模块               
o  2.20. sha 模块               
o  2.21. crypt 模块             
o  2.22. rotor 模块             
o  2.23. zlib 模块              
o  2.24. code 模块              
###3. 线程和进程                   
o  3.1. 概览                    
o  3.2. threading 模块          
o  3.3. Queue 模块              
o  3.4. thread 模块             
o  3.5. commands 模块           
o  3.6. pipes 模块              
o  3.7. popen2 模块             
o  3.8. signal 模块             
###4. 数据表示                     
o  4.1. 概览                    
o  4.2. array 模块              
o  4.3. struct 模块             
o  4.4. xdrlib 模块             
o  4.5. marshal 模块            
o  4.6. pickle 模块             
o  4.7. cPickle 模块            
o  4.8. copy_reg 模块           
o  4.9. pprint 模块             
o  4.10. repr 模块              
o  4.11. base64 模块            
o  4.12. binhex 模块            
o  4.13. quopri 模块            
o  4.14. uu 模块                
o  4.15. binascii 模块          
###5. 文件格式                     
o  5.1. 概览                    
o  5.2. xmllib 模块             
o  5.3. xml.parsers.expat 模块  
o  5.4. sgmllib 模块            
o  5.5. htmllib 模块            
o  5.6. htmlentitydefs 模块     
o  5.7. formatter 模块          
o  5.8. ConfigParser 模块       
o  5.9. netrc 模块              
o  5.10. shlex 模块             
o  5.11. zipfile 模块           
o  5.12. gzip 模块              
###6. 邮件和新闻消息处理           
o  6.1. 概览                    
o  6.2. rfc822 模块             
o  6.3. mimetools 模块          
o  6.4. MimeWriter 模块         
o  6.5. mailbox 模块            
o  6.6. mailcap 模块            
o  6.7. mimetypes 模块          
o  6.8. packmail 模块           
o  6.9. mimify 模块             
o  6.10. multifile 模块         
###7. 网络协议                     
o  7.1. 概览                    
o  7.2. socket 模块             
o  7.3. select 模块             
o  7.4. asyncore 模块           
o  7.5. asynchat 模块           
o  7.6. urllib 模块             
o  7.7. urlparse 模块           
o  7.8. cookie 模块             
o  7.9. robotparser 模块        
o  7.10. ftplib 模块            
o  7.11. gopherlib 模块         
o  7.12. httplib 模块           
o  7.13. poplib 模块            
o  7.14. imaplib 模块           
o  7.15. smtplib 模块           
o  7.16. telnetlib 模块         
o  7.17. nntplib 模块           
o  7.18. SocketServer 模块      
o  7.19. BaseHTTPServer 模块    
o  7.20. SimpleHTTPServer 模块  
o  7.21. CGIHTTPServer 模块     
o  7.22. cgi 模块               
o  7.23. webbrowser 模块        
###8. 国际化                       
o  8.1. locale 模块             
o  8.2. unicodedata 模块        
o  8.3. ucnhash 模块            
9. 多媒体相关模块               
o  9.1. 概览                    
o  9.2. imghdr 模块             
o  9.3. sndhdr 模块             
o  9.4. whatsound 模块          
o  9.5. aifc 模块               
o  9.6. sunau 模块              
o  9.7. sunaudio 模块           
o  9.8. wave 模块               
o  9.9. audiodev 模块           
o  9.10. winsound 模块          
###10.数据储存                     
o  10.1. 概览                   
o  10.2. anydbm 模块            
o  10.3. whichdb 模块           
o  10.4. shelve 模块            
o  10.5. dbhash 模块            
o  10.6. dbm 模块               
o  10.7. dumbdbm 模块           
o  10.8. gdbm 模块              
###11.工具和实用程序               
o  11.1. dis 模块               
o  11.2. pdb 模块               
o  11.3. bdb 模块               
o  11.4. profile 模块           
o  11.5. pstats 模块            
o  11.6. tabnanny 模块          
###12.其他模块                     
o  12.1. 概览                   
o  12.2. fcntl 模块             
o  12.3. pwd 模块               
o  12.4. grp 模块               
o  12.5. nis 模块               
o  12.6. curses 模块            
o  12.7. termios 模块           
o  12.8. tty 模块               
o  12.9. resource 模块          
o  12.10. syslog 模块           
o  12.11. msvcrt 模块           
o  12.12. nt 模块               
o  12.13. _winreg 模块          
o  12.14. posix 模块            
###13.执行支持模块                 
o  13.1. dospath 模块           
o  13.2. macpath 模块           
o  13.3. ntpath 模块            
o  13.4. posixpath 模块         
o  13.5. strop 模块             
o  13.6. imp 模块               
o  13.7. new 模块               
o  13.8. pre 模块               
o  13.9. sre 模块               
o  13.10. py_compile 模块       
o  13.11. compileall 模块       
o  13.12. ihooks 模块           
o  13.13. linecache 模块        
o  13.14. macurl2path 模块      
o  13.15. nturl2path 模块       
o  13.16. tokenize 模块         
o  13.17. keyword 模块          
o  13.18. parser 模块           
o  13.19. symbol 模块           
o  13.20. token 模块            
###14.其他模块                     
o  14.1. 概览                   
o  14.2. pyclbr 模块            
o  14.3. filecmp 模块           
o  14.4. cmd 模块               
o  14.5. rexec 模块             
o  14.6. Bastion 模块           
o  14.7. readline 模块          
o  14.8. rlcompleter 模块       
o  14.9. statvfs 模块           
o  14.10. calendar 模块         
o  14.11. sched 模块            
o  14.12. statcache 模块        
o  14.13. grep 模块             
o  14.14. dircache 模块         
o  14.15. dircmp 模块           
o  14.16. cmp 模块              
o  14.17. cmpcache 模块         
o  14.18. util 模块             
o  14.19. soundex 模块          
o  14.20. timing 模块           
o  14.21. posixfile 模块        
o  14.22. bisect 模块           
o  14.23. knee 模块             
o  14.24. tzparse 模块          
o  14.25. regex 模块            
o  14.26. regsub 模块           
o  14.27. reconvert 模块        
o  14.28. regex_syntax 模块     
o  14.29. find 模块             
###15.Py 2.0 后新增模块            
###16.后记                         