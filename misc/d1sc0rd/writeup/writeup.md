# d1sc0rd

1. Download FTK Imager to open the .ad1 file.
2. If you look around the file system, you should find the first flag located at `C:\Users\noroshi\Desktop\flag1.txt.`
3. Based on the title, or if you look around a bit more, you can see that Discord is installed on this computer.
4. Discord caches messages and image links in `C:\Users\noroshi\AppData\Roaming\discord\Cache\Cache_Data`
5. You can choose to view the cache data using a tool like [ChromeCacheView](https://www.nirsoft.net/utils/chrome_cache_view.html) (It works even if it is not Chrome)
6. You can find the second flag in a cache file called `50.json`, the flag is encoded in Base58
7. You can find the third flag by searching for `GIF` cache files

Flag: 
`MOCSCTF{1n7r0duc710n_70_d15k_1m463_4nd_d15c0rd_f0r3n51c5_4nd_4l50_h3r3_1s_fr13r3n_1n_cach3}`

