print('''content-type:text/html\n\n
<html>
<head>
<script>
function AllowAlphabet(){
if (!frm.name.value.match(/^[a-z A-Z]+$/) && frm.name.value !=""){
frm.name.value="";
frm.name.focus();

}
}
</script>

<script>
function validateForm()
{
var x=document.forms["frm"]["email"].value;
var atpos=x.indexOf("@");
var dotpos=x.lastIndexOf(".");
if (atpos<1 || dotpos<atpos+5 || dotpos+3>=x.length)
{
alert("Not a valid e-mail address");
return false;
}
}
</script>


<title>Contact Us</title>
<link href="st2.css" rel="stylesheet">
</head>
<body>
<div class="header">
<img src="logo.png" class="img" width="103" height="96" alt="not avilable">
<h1>Name:Stock Market<br>Mob No.:7694960860</h1>
</div>
<div class="nav">
<div id="menu">
<ul>
<li><a href="main.py">Home</a></li>

<li><a href="about.py">About</a></li>
<li><a href="contact.py">Contact</a></li>
</ul>
</div>
<div class="social">
<ul>
<li><a href="#"><img src="facebook.png"></a></li>
<li><a href="#"><img src="twitter.png"></a></li>
</ul>
</div>
</div>
<div id="main">
<div class="lefts">
<div class="contactdtl">
 <h3>Contact Detail</h3>
 <p><b>Name:</b> Stock Market</p>
 <p><b>Contact No.:</b> 7694960860</p>
 <p><b>E-Mail:</b> shreyashmehta12@gmail.com</p>
 <p><b>Address:</b> Amity University, Gwalior.</p>

 </div>
 <div class="right">
 <div class="contact">
  <h4>Contact Form</h4>
  <p><form action='contactreg.py' method=post name="frm" ></p>
  <p><input type="text" placeholder="Name" required maxlength="30" name='name' onkeyup="AllowAlphabet()"></p>
  <p><input type=text placeholder="Mobile No." required maxlength=10 pattern=[1-9]{1}[0-9]{9} name='mob'></p>
  <p> <input type="email" placeholder="E-Mail" name=email required maxlength="30" onChange="return validateForm()"></p>
  <p><textarea rows="5" cols="30" placeholder="Message:" required maxlength="1000" name=msg></textarea></p>
  <input type="submit" value="Submit">
  </form>
 </div>
 </div>
 </div>


 <div class="right">
 <h3>Contact Us</h3>
 <p><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3577.6594095247315!2d78.22620101503146!3d26.272715183407502!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3976c0e647bece07%3A0xd848338a0d6a5393!2sAmity+University+Gwalior%2CMadhya+Pradesh!5e0!3m2!1sen!2sin!4v1534011465053" width="1200" height="600" frameborder="0" style="border:0"></iframe> </p>
 
 </div>
</div>
<div id="footermain">
<div class="block1">
<h4>About</h4>
<li><a href="main.py">&#9755; Home</a></li>

<li><a href="about.py">&#9755; About</a></li>
<li><a href="contact.py">&#9755; Contact</a></li>
</div>
<div class="block1">
<h4>Contact</h4>
<p><b>Name:</b> Stock Market</p>
 <p><b>Contact No.:</b> 7694960860</p>
 <p><b>E-Mail:</b> shreyashmehta12@gmail.com</p>
 <p><b>Address:</b> Amity University, Gwalior.</p>

</div>
<div class="block1">
<h4>Gallery</h4>
<img src="img1.png">
<img src="img2.png">
<img src="img3.jpg">
<img src="img7.jpg">
<img src="img.jpg">
<img src="img5.jpg">
<img src="img6.jpg">
<img src="img9.jpg">
</div>
</div>
<div id="footer">
<p class="copy">Designed By:Stock Market</a></p>
</footer>
</body>
</html>''')
