<?
/************************************************************\
*
*		PHP Pass Copyright 2005 Howard Yeend
*		www.puremango.co.uk
*
*    This file is part of PHP Pass.
*
*    PHP Pass is free software; you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation; either version 2 of the License, or
*    (at your option) any later version.
*
*    PHP Pass is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with PHP Pass; if not, write to the Free Software
*    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*
*
\************************************************************/

session_start();

//--------------------------
// user definable variables:
//--------------------------

// maximum number of seconds user can remain idle without having to re-login:
// use a value of zero for no timeout
$max_session_time = 28800;

// type of alert to give on incorrect password:
// eg:
// $alert = "joe@foo.com";	- sends email to joe@foo.com
// $alert = "blah";		- appends to file named 'blah'
// $alert = "";			- no alerts
$alert = "";

// acceptable passwords:
$cmp_pass = Array();
$cmp_pass[] = md5("password"); // No, this is not the actual password.
// add as many as you like

// maximum number of bad logins before user locked out
// use a value of zero for no hammering protection
$max_attempts = 5;

//-----------------------------
// end user definable variables
//-----------------------------


// save session expiry time for later comparision
$session_expires = $_SESSION['mpass_session_expires'];

// have to do this otherwise max_attempts is actually one less than what you specify.
$max_attempts++;

if(!empty($_POST['mpass_pass']))
{
	// store md5'ed password
	$_SESSION['mpass_pass'] = md5($_POST['mpass_pass']);
}

if(empty($_SESSION['mpass_attempts']))
{
	$_SESSION['mpass_attempts'] = 0;
}

// if the session has expired, or the password is incorrect, show login page:
if(($max_session_time>0 && !empty($session_expires) && mktime()>$session_expires) || empty($_SESSION['mpass_pass']) || !in_array($_SESSION['mpass_pass'],$cmp_pass))
{
	if(!empty($alert) && !in_array($_SESSION['mpass_pass'],$cmp_pass))
	{
		// user has submitted incorrect password
		// generate alert:

		$_SESSION['mpass_attempts']++;
		
		$alert_str = $_SERVER['REMOTE_ADDR']." entered ".htmlspecialchars($_POST['mpass_pass'])." on page ".$_SERVER['PHP_SELF']." on ".date("l dS of F Y h:i:s A")."\r\n";
		
		if(stristr($alert,"@")!==false)
		{
			// email alert
			@mail($alert,"Bad Login on ".$_SERVER['PHP_SELF'],$alert_str,"From: ".$alert);
		} else {
			// textfile alert
			$handle = @fopen($alert,'a');
			if($handle)
			{
				fwrite($handle,$alert_str);
				fclose($handle);
			}
		}
	}
	// if hammering protection is enabled, lock user out if they've reached the maximum
	if($max_attempts>1 && $_SESSION['mpass_attempts']>=$max_attempts)
	{
		exit("Too many login failures.");
	}


	// clear session expiry time
	$_SESSION['mpass_session_expires'] = "";

	?>
<?php include("/f5/hpscience/public/includes/header.php"); ?>
<title>HP Science: Physics</title>
<link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>
<header>HP Science: Physics</header>
<?php include("/f5/hpscience/public/includes/navigation.php"); ?>
<form action="<?=$_SERVER['PHP_SELF']?>" method="post">
<p><center>
Please log in to continue:<br>
<input type="password" name="mpass_pass">
<input type="submit" value="Login"></center></p>
</form>
<?php include("/f5/hpscience/public/includes/footer.php"); ?>
</footer>
</body>
</html>
	<?

	// and exit
	exit();
}

// if they've got this far, they've entered the correct password:

// reset attempts
$_SESSION['mpass_attempts'] = 0;

// update session expiry time
$_SESSION['mpass_session_expires'] = mktime()+$max_session_time;

// end password protection code
?>
<?php include("/f5/hpscience/public/includes/header.php"); ?>
<title>HP Science: Physics</title>
<link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>
<header>HP Science: Physics</header>
<?php include("/f5/hpscience/public/includes/navigation.php"); ?>
<p>
<a href="FormulaSheet.pdf">Formula Sheet (.pdf)</a><br>
<a href="http://www.uiltexas.org/files/academics/science-physics-note-2010-11.pdf">Note from the physics director (.pdf)</a><br>
<a href="http://www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf"><i>A Brief History of Time</i> (.pdf)</a><br>
<a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#3"><i>A Brief History of Time</i> (.html)</a><br>
<a href="http://vega.org.uk/video/subseries/8">Richard Feynman's video lecutres</a>
</p>

The questions for each contest will be based on the following book chapters and videos as follows:

<h1>Hawking’s Book</h1>
<p>
<a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#3">Chapter 1: Our Picture of the Universe</a> (Invitational A & B)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#10">Chapter 2: Space and Time</a> (Invitational A & B)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#22">Chapter 3: The Expanding Universe</a> (Invitational A & B)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#94">Biographical sketches on Einstein, Galileo, and Newton</a> (Invitational A & B)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#31">Chapter 4: The Uncertainty Principle</a> (District 1)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#36">Chapter 5: Elementary Particles and the Forces of Nature</a> (District 1)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#44">Chapter 6: Black Holes</a> (District 2)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#53">Chapter 7: Black Holes Ain’t So Black</a> (District 2)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#61">Chapter 8: The Origin and Fate of the Universe</a> (Regional)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#72">Chapter 9: The Arrow of Time</a> (Regional)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#82">Chapter 10: The Unification of Physics</a> (State)
<br><a href="http://webcache.googleusercontent.com/search?q=cache:6Q5d3xd5GaQJ:www.fisica.net/relatividade/stephen_hawking_a_brief_history_of_time.pdf&hl=en&gl=us#93">Chapter 11: Conclusion</a> (State)
</p>

<h1>Feynman’s Video Lectures</h1>
<p>
<a href="http://vega.org.uk/video/programme/45">Part 1: Photons – Corpuscles of Light</a> (Invitational A & B)
<br><a href="http://vega.org.uk/video/programme/46">Part 2: Fits of Reflection and Transmission – Quantum Behavior</a> (District 1)
<br><a href="http://vega.org.uk/video/programme/46">Part 2: Fits of Reflection and Transmission – Quantum Behavior</a> (District 2)
<br><a href="http://vega.org.uk/video/programme/47">Part 3: Electrons and their Interactions</a> (Regional)
<br><a href="http://vega.org.uk/video/programme/48">Part 4: New Queries</a> (State)
</p>

<?php include("/f5/hpscience/public/includes/footer.php"); ?>
</footer>
</body>
</html>
