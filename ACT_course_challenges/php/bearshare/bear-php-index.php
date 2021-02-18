<?php
	if(isset($_POST['message'])){
		$message = (string)$_POST['message'];
		$rand_id = rand(1000000000, 9999999999).'salt^&#@!'.rand(1000000000, 9999999999);
		$messid = md5($rand_id);
		$store_location = rand(0,10);
		if($store_location%2===0){
			die('Writing to message1 is not implemented');
		} else {
			die('Writing to message2 is not implemented');
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
 *         -------------------------------------------------- */
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
 *         -------------------------------------------------- */
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
            <li class="nav-item active">
              <a class="nav-link" href="index.php">Create message<span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="download.php">Get message</a>
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
      <?php if(isset($messid)){ 
        $at="";
        if($store_location%2===0){ 
          $at="message1.local"; 
        }else{
          $at="message2.local";
        } ?>
      <p>Your message stored at server: <code><?php echo $at; ?></code></p>
      <p>Your message's ID: <code><?php echo $messid; ?></code></p>
      <?php  
    } ?>
        <form class="form-signin" method="POST" action="index.php">
            <input type="text" placeholder="Your private message" class="form-control" name="message"/>
            <button class="btn btn-lg btn-primary btn-block" style="max-width:300px;margin:auto;margin-top:30px;" type="submit">Create</button>
        </form>
    </main>

    <footer class="footer">
      <div class="container">
        <span class="text-muted">Content 2018 - AceBear</span>
</div>
    </footer>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="assets/js/vendor/popper.min.js"></script>
    <script src="dist/js/bootstrap.min.js"></script>
  </body>
</html>