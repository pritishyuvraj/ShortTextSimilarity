<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);


#echo "Running output";
#$output = shell_exec("sh script.sh");
#echo "Ran output";
#print $output;

#$cmd = escapeshellcmd('python sts1.py');
#$output = shell_exec($cmd);
#echo $output;
#echo $f1;
function clean($string) {
   $string = str_replace('[', '', $string); // Replaces all spaces with hyphens.
   $string = str_replace(']', '', $string);
   return $string;
   #return preg_replace('/[^A-Za-z0-9\-\ ]/', '', $string); // Removes special chars.
}

$f1 = fopen('f1', "r") or die("Unable to open feature 1 file!");
$f1_read = fread($f1, filesize('f1'));
$f2 = fopen('f2', "r") or die("Unable to open feature 2 file!");
$f2_read = fread($f2, filesize('f2'));
$result = fopen('result_text', "r") or die("Unable to open result file!");
$result_read = fread($result, filesize('result_text'));
$sentences  = fopen('sentence', "r") or die("Unable to open sentences file!");
$sentence_read = fread($sentences, filesize("sentence"));
#echo "hey";
#$f1_read = clean($f1_read);
#$f2_read = clean($f2_read);
#$result_read = clean($result_read);
#$sentence_read = clean($sentence_read);
$f1_read = explode("start", $f1_read);
$f2_read = explode("start", $f2_read);
$result_read = explode("\n", $result_read);
$sentence_read = explode("\n", $sentence_read);
#print_r($f1_read);
#echo "<br> Sentence2 <br>";
#print_r($f1_read);
#print_r($result_read);
#print_r($sentence_read); 

#Splitting arrays:
#Sentence 1
#echo "<br>Sentence1<br>";
for($i = 0; $i < count($f1_read); $i++){
	#Word POS Tagging
	if ($i == 1){
		$temp = explode(";", $f1_read[$i]);
		array_pop($temp);
		#print_r($temp);
		$sentence_1_word_type = [];
		for($j = 1; $j < count($temp); $j++){
			
			$temp2 = explode(",", $temp[$j]);
			$sentence_1_word_type[$temp2[0]] = $temp2[1];
		}
		#print_r($sentence_1_word_type);
		#print_r($temp);
	}
	#Word Alignment Score
	if ($i == 2){
		$temp = explode(";", $f1_read[$i]);
		array_pop($temp);
		#echo "<br> sentenc2 <br>";
		#print_r($temp);
		$sentence_1_word_align = [];
		#echo "<br> result 1<br>";
		for($j = 1; $j < count($temp); $j++){
			#echo "<br>Value sentence 1<br>";
			#print_r($temp[$j]);
			$temp2 = explode(",", $temp[$j]);
			#print_r($temp2);
			$sentence_1_word_align[$temp2[0]] = [$temp2[1], $temp2[2]];
		}
		#print_r($sentence_1_word_align);
		#print_r($temp);
	}
	#Information Content Score
	if ($i == 3){
		$temp = explode(";", $f1_read[$i]);
		array_pop($temp);
		$sentence_1_info_content = [];
		for($j = 1; $j < count($temp); $j++){
			$temp2 = explode(",", $temp[$j]);
			$sentence_1_info_content[$temp2[0]] = $temp2[3];
		}
		#print_r($sentence_1_info_content);
	}
}

#Sentence 2
#echo "<br>Sentence 2<br>";
for($i = 0; $i < count($f2_read); $i++){
	#Word POS Tagging
	if ($i == 1){
		$temp = explode(";", $f2_read[$i]);
		array_pop($temp);
		#print_r($temp);
		$sentence_2_word_type = [];
		for($j = 1; $j < count($temp); $j++){
			
			$temp2 = explode(",", $temp[$j]);
			$sentence_2_word_type[$temp2[0]] = $temp2[1];
		}
		#print_r($sentence_2_word_type);
		#print_r($temp);
	}
	#Word Alignment Score
	if ($i == 2){
		$temp = explode(";", $f2_read[$i]);
		array_pop($temp);
		#echo "<br> sentenc2 <br>";
		#print_r($temp);
		$sentence_2_word_align = [];
		#echo "<br> result 1<br>";
		for($j = 1; $j < count($temp); $j++){
			#echo "<br>Value sentence 1<br>";
			#print_r($temp[$j]);
			$temp2 = explode(",", $temp[$j]);
			#print_r($temp2);
			$sentence_2_word_align[$temp2[0]] = [$temp2[1], $temp2[2]];
		}
		#print_r($sentence_2_word_align);
		#print_r($temp);
	}
	#Information Content Score
	if ($i == 3){
		$temp = explode(";", $f2_read[$i]);
		array_pop($temp);
		$sentence_2_info_content = [];
		for($j = 1; $j < count($temp); $j++){
			$temp2 = explode(",", $temp[$j]);
			$sentence_2_info_content[$temp2[0]] = $temp2[3];
		}
		#print_r($sentence_2_info_content);
	}
}

#print_r($result_read);
#print_r($sentence_read);
?>

<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Sticky Table Headers Revisited | Demo 1</title>
		<meta name="description" content="Sticky Table Headers Revisited: Creating functional and flexible sticky table headers" />
		<meta name="keywords" content="Sticky Table Headers Revisited" />
		<meta name="author" content="Codrops" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/normalize.css" />
		<link rel="stylesheet" type="text/css" href="css/demo.css" />
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		<!--[if IE]>
  		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
	</head>
	<body>
		<div class="container">
			<!-- Top Navigation -->
			<div class="codrops-top clearfix">
				<a class="codrops-icon codrops-icon-prev" href="http://tympanus.net/Tutorials/ShapeHoverEffectSVG/"><span>Previous Demo</span></a>
				<span class="right"><a class="codrops-icon codrops-icon-drop" href="http://tympanus.net/codrops/?p=18116"><span>Back to the Codrops Article</span></a></span>
			</div>
			<header>
				<h1>Short Text Similarity</em> <span>Results page</span></h1>	
				<nav class="codrops-demos">
					<a class="current-demo" href="index.html" title="Basic Usage">Home Page</a>
					<a class="current-demo" href="index.html" title="Basic Usage">Final Results</a>
					<a href="index2.html" title="Biaxial Headers">Inputs</a>
					<a href="index.php" title="Wide Tables">Outputs</a>
				</nav>
			</header>
			<div class="component">
				<h2>Page shows results</h2>
				<table>
					<thead>
						<tr>
							<th>Name</th>
							<th>Sentence 1</th>
							<th>Sentence 2</th>
						</tr>
					</thead>
					<tbody>
						<tr><td class="user-name">Input Sentences</td><td class="user-email"><?php echo $sentence_read[0];	?></td><td class="user-phone"><?php echo $sentence_read[1];			?></td></tr>
						<tr><td class="user-name">POS Tagging</td><td class="user-email"><?php 
		#print_r($sentence_1_word_type);
		foreach ($sentence_1_word_type as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?></td><td class="user-phone"><?php 
		#print_r($sentence_1_word_type);
		foreach ($sentence_2_word_type as $key => $value){
			echo $key, "=>", $value, "<br>";
		}?></td></tr>
						<tr><td class="user-name">Word Align and Score</td><td class="user-email"><?php 
		foreach ($sentence_1_word_align as $key => $value){
			echo $key, "=>", $value[0], " (Score:", $value[1], ")<br>";
		}
		?></td><td class="user-phone"><?php 
		foreach ($sentence_2_word_align as $key => $value){
			echo $key, "=>", $value[0], " (Score:", $value[1], ")<br>";
		}
		?></td></tr>
						<tr><td class="user-email">Information Content</td><td class="user-mobile"><?php 
		foreach ($sentence_1_info_content as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?></td>
						<td class="user-name"><?php 
		foreach ($sentence_2_info_content as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?></td>
		<tr><td class="user-phone">Accuracy</td><td class="user-name"><?php 
		echo $result_read[2], " (Author's method)";
		?></td><td class="user-email"><?php 
		echo $result_read[3], " (Our proposed method)";
		?>
		</td></td></tr>
						
					</tbody>
				</table>
				
			</div>
			<section class="related">
				<p>If you enjoyed these effects you might also like:</p>
				<div><a href="http://tympanus.net/Development/HeaderEffects/"><h4>On Scroll Header Effects</h4></a></div>
				<div><a href="http://tympanus.net/Development/MultiElementSelection/"><h4>Multi-Item Selection</h4></a></div>
			</section>
		</div><!-- /container -->
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js"></script>
		<script src="js/jquery.stickyheader.js"></script>
	</body>
</html>