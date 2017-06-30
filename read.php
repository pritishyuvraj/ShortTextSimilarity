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
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>Table Style</title>
	<meta name="viewport" content="initial-scale=1.0; maximum-scale=1.0; width=device-width;">
</head>
<body>
<div class="table-title">
<table border = 1 class="table-fill">
	<thead>
	<tr>
		<th class="text-left">Name</th>
		<th class="text-left">Sentence 1</th>
		<th class="text-left">Sentence 2</th>
	</tr>
	</thead>
	<tbody class="table-hover">
	<tr>
		<td class="text-left">Input Sentences</td>
		<td class="text-left"><?php 
			echo $sentence_read[0];
			?>
		</td>
		<td class="text-left"><?php 
			echo $sentence_read[1];
			?>
		</td>
	</tr>
	<tr>
		<td class="text-left">POS Tagging</td>
		<td class="text-left">
		<?php 
		#print_r($sentence_1_word_type);
		foreach ($sentence_1_word_type as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?>
		</td>
		<td class="text-left">
		<?php 
		#print_r($sentence_1_word_type);
		foreach ($sentence_2_word_type as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?>
		</td>
	</tr>
	<tr>
		<td class="text-left">Word Align and Score</td>
		<td class="text-left">
		<?php 
		foreach ($sentence_1_word_align as $key => $value){
			echo $key, "=>", $value[0], " (Score:", $value[1], ")<br>";
		}
		?>
		</td>
		<td class="text-left">
		<?php 
		foreach ($sentence_2_word_align as $key => $value){
			echo $key, "=>", $value[0], " (Score:", $value[1], ")<br>";
		}
		?>
		</td>
	</tr>
	<tr>
		<td class="text-left">Information Content</td>
		<td class="text-left"><?php 
		foreach ($sentence_1_info_content as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?>
		</td>
		<td class="text-left">
		<?php 
		foreach ($sentence_2_info_content as $key => $value){
			echo $key, "=>", $value, "<br>";
		}
		?>
		</td>
	</tr>
	<tr>
		<td class="text-left">Accuracy</td>
		<td class="text-left">
		<?php 
		echo $result_read[2], " (Author's method)";
		?>
		</td>
		<td class="text-left">
		<?php 
		echo $result_read[3], " (Our proposed method)";
		?>
		</td>
	</tr>
	</tbody>
</table>