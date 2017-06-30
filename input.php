<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
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
		<link rel="stylesheet" type="text/css" href="normalize.css" />
		<link rel="stylesheet" type="text/css" href="demo.css" />
		<link rel="stylesheet" type="text/css" href="component.css" />
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
				<table style="background-color:black; width:100%; height:10%";>
					<thead>
						<tr>
							<th> </th>
							<th>Input Sentence 1</th>
							<th>Input Sentence 2</th>
							<th></th>
						</tr>
					</thead>
					<tbody>
					<form action="http://127.0.0.1:5000/login" name="name" method=post>
						<tr>
						<td class="user-name"></td>
						<td class="user-email">
						<input type = "textarea" name = "sent2" rows = "4" cols = "50" placeholder="Enter sentence"/>
						</td>
						<td class="user-phone"><input type = "textarea" name="sent1" rows = "4" cols = "50" placeholder="Enter sentence"/>
						</td>
						<td class="user-phone"><input type ="submit"/>
						<input type="hidden" name="action">
						</tr>
						
						
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

