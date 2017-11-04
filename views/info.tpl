<!DOCTYPE html>
<html>
<head>
	<title>Bílar</title>
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
</head>
<body>
<form action="/results" method="post">
	<fieldset>
	<legend><h2>Leita að bíl</h2></legend>
	<input type="text" name="fastanr" placeholder="Fastanúmer bíls" title="AB-123 eða AB-C12" required><br>
	<input type="submit" value="Leita">
	</fieldset>
</form>
<h3>Upplýsingar<h3>
<p>Fastanúmer: {{a}}</p>
<p>Tegund: {{b}}</p>
<p>Verksmiðjunúmer: {{c}}</p>
<p>Skráningardagur: {{d}}</p>
<p>CO2: {{e}}</p>
<p>Þyngd: {{f}}</p>
<p>Skoðun: {{g}}</p>
<p>Staða: {{h}}</p>
<a href="innskraning"><div class="signup"><h3>Login</h3></div></a>
</body>
</html>
<style type="text/css">
	*{
		font-family: Roboto;
	}
	body{
		margin: 0;
		margin-top:200px;
		background-color:#F5F5F5 ;
	}
	.signup{
		position:fixed;
		bottom:40px;
		right:40px;
		border:black solid 4px;
		font-size 1.6em;
		padding: 0 20px;
	}
	.signup h3{
		color:black;
	}
	.signup:hover{
		background-color:#E0E0E0;
	}
	form{
		max-width: 600px;
		margin: auto;
	}
	h2{
		font-family: arial;
		margin-bottom: 0;
	}
	input{
		width: 95%;
		padding: 10px;
		outline-style: outset;
		margin: 10px 0 10px 0;
		font-size: 1.2em;
		margin:10px auto;
	}
	input[type=submit]{
		width:99%;
	}
	input[type=radio]{
		outline: none;
	}
	ul li{
		color: #AAAAAA;
		display: block;
		position: relative;
		float: left;
		width: 100%;
		height: 100px;
		border-bottom: 1px solid white;
	}
	ul li input[type=radio]{
		position: absolute;
		visibility: hidden;
	}
	ul li input[type=checkbox]{
		position: absolute;
		visibility: hidden;
	}
	ul li label{
		display: block;
		position: relative;
		font-weight: 300;
		font-size: 1.35em;
		padding: 25px 25px 25px 80px;
		margin: 10px auto;
		height: 30px;
		z-index: 9;
		cursor: pointer;
		-webkit-transition: all 0.25s linear;
	}
	ul li:hover label{
		color: black;
	}
	ul li .check{
		display: block;
		position: absolute;
		border: 5px solid #AAAAAA;
		border-radius: 100%;
		height: 25px;
		width: 25px;
		top: 30px;
		left: 20px;
		z-index: 5;
		transition: border .25s linear;
		-webkit-transition: border .25s linear;
	}
	ul li .checkb{
		border-radius: 0%;
	}
	ul li:hover .check {
		border: 5px solid black;
	}
	ul li .check::before {
		display: block;
		position: absolute;
		content: '';
		border-radius: 100%;
		height: 15px;
		width: 15px;
		top: 5px;
		left: 5px;
		margin: auto;
		transition: background 0.25s linear;
		-webkit-transition: background 0.25s linear;
	}
	ul li .checkb::before{
		border-radius: 0%;
	}
	input[type=radio]:checked ~ .check {
		border: 5px solid DodgerBlue;
	}
	input[type=radio]:checked ~ .check::before{
		background: DodgerBlue;
	}
	input[type=radio]:checked ~ label{
		color: DodgerBlue;
	}
	input[type=checkbox]:checked ~ .check {
		border: 5px solid DodgerBlue;
	}
	input[type=checkbox]:checked ~ .check::before{
		background: DodgerBlue;
	}
	input[type=checkbox]:checked ~ label{
		color: DodgerBlue;
	}
</style>