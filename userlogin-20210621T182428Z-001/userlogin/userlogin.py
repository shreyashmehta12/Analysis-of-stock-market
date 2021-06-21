print('''content-type:text/html\n\n                                                                                                                                                                                                                                                                      
 <html>                                                                                                                                                                                                                                                                                
 <head>                                                                                                                                                                                                                                                                                
      <title>User Login</title>                                                                                                                                                                                                                                                        

<script>
function fileValidation(){
var fileInput=document.getElementById("file");
var filePath=fileInput.value;
var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
if(!allowedExtensions.exec(filePath)){
alert('Please upload file having extensions .jpg/.jpeg/.png/.gif only.');
fileInput.value = '';
return false;
}else{
return true;
}
}
</script>

<script>
function fileValidationn(){
var fileInput=document.getElementById("filee");
var filePath=fileInput.value;
var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
if(!allowedExtensions.exec(filePath)){
alert('Please upload file having extensions .jpg/.jpeg/.png/.gif only.');
fileInput.value = '';
return false;
}else{
return true;
}
}
</script>

<script>
function fileValidationnn(){
var fileInput=document.getElementById("fileee");
var filePath=fileInput.value;
var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
if(!allowedExtensions.exec(filePath)){
alert('Please upload file having extensions .jpg/.jpeg/.png/.gif only.');
fileInput.value = '';
return false;
}else{
return true;
}
}
</script>

<script>
function AllowAlphabet(){
if (!frm.ufnm.value.match(/^[a-z A-Z]+$/) && frm.ufnm.value !=""){
frm.ufnm.value="";
frm.ufnm.focus();

}
}
</script>

<script>
function AllowAlphabett(){
if (!frm.ulnm.value.match(/^[a-z A-Z]+$/) && frm.ulnm.value !=""){
frm.ulnm.value="";
frm.ulnm.focus();

}
}
</script>

<script>
function validateForm()
{
var x=document.forms["frm"]["ueid"].value;
var atpos=x.indexOf("@");
var dotpos=x.lastIndexOf(".");
if (atpos<1 || dotpos<atpos+5 || dotpos+3>=x.length)
{
alert("Not a valid e-mail address");
return false;
}
}
</script>

<script>


    function dobValidate() {


        var today = new Date();
        var nowyear = today.getFullYear();
        var nowmonth = today.getMonth();
        var nowday = today.getDate();
        var b = document.getElementById("dob").value;



        var birth = new Date(b);

        var birthyear = birth.getFullYear();
        var birthmonth = birth.getMonth();
        var birthday = birth.getDate();

        var age = nowyear - birthyear;
        var age_month = nowmonth - birthmonth;
        var age_day = nowday - birthday;


        if (age > 100) {
            alert("Age cannot be more than 100 Years.Please enter correct age")
            return false;
        }
        if (age_month < 0 || (age_month == 0 && age_day < 0)) {
            age = parseInt(age) - 1;


        }
        if ((age == 18 && age_month <= 0 && age_day <= 0) || age < 18) {
            alert("Age should be more than 18 years.Please enter a valid Date of Birth");
            return false;
        }
    }
</script>

<script>
function checkCheckBox(){
var agree=document.frm.agree;
if (agree.checked == false )
{
alert('Please check the box to continue.');
return false;
}else
return true;
}
</script>



      <link href='http://fonts.googleapis.com/css?family=Ropa+Sans' rel='stylesheet'>                                                                                                                                                                                                 
<link href=http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css rel='stylesheet'>  
<style>                                                                                                                                                                                                                                                                                
body{font-family: 'Ropa Sans', sans-serif; color:#666; font-size:14px; color:#333}                                                                                                                                                                                                     
li,ul,body,input{margin:0; padding:0; list-style:none}                                                                                                                                                                                                                                 
#login-form{width:350px; background:#FFF; margin:0 auto; margin-top:70px; background:#f8f8f8; overflow:hidden; border-radius:7px}                                                                                                                                                      
.form-header{display:table; clear:both}                                                                                                                                                                                                                                                
.form-header label{display:block; cursor:pointer; z-index:999}                                                                                                                                                                                                                         
.form-header li{margin:0; line-height:60px; width:175px; text-align:center; background:#eee; font-size:18px; float:left; transition:all 600ms ease}                                                                                                                                    
                                                                                                                                                                                                                                                                                       
/*sectiop*/                                                                                                                                                                                                                                                                            
.section-out{width:700px; float:left; transition:all 600ms ease}                                                                                                                                                                                                                       
.section-out:after{content:''; clear:both; display:table}                                                                                                                                                                                                                              
.section-out section{width:350px; float:left}                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                       
.login{padding:20px}                                                                                                                                                                                                                                                                   
.ul-list{clear:both; display:table; width:100%}                                                                                                                                                                                                                                        
.ul-list:after{content:''; clear:both; display:table}                                                                                                                                                                                                                                  
.ul-list li{ margin:0 auto; margin-bottom:12px}                                                                                                                                                                                                                                        
.input{background:#fff; transition:all 800ms; width:247px; border-radius:3px 0 0 3px; font-family: 'Ropa Sans', sans-serif; border:solid 1px #ccc; border-right:none; outline:none; color:#999; height:40px; line-height:40px; display:inline-block; padding-left:10px; font-size:16px}
.input,.login span.icon{vertical-align:top}                                                                                                                                                                                                                                            
.login span.icon{width:50px; transition:all 800ms; text-align:center; color:#999; height:40px; border-radius:0 3px 3px 0; background:#e8e8e8; height:40px; line-height:40px; display:inline-block; border:solid 1px #ccc; border-left:none; font-size:16px}                            
.input:focus:invalid{border-color:red}                                                                                                                                                                                                                                                 
.input:focus:invalid+.icon{border-color:red}                                                                                                                                                                                                                                           
.input:focus:valid{border-color:green}                                                                                                                                                                                                                                                 
.input:focus:valid+.icon{border-color:green}                                                                                                                                                                                                                                           
#check,#check1{top:1px; position:relative}                                                                                                                                                                                                                                             
.btn{border:none; outline:none; background:#0099CC; border-bottom:solid 4px #006699; font-family: 'Ropa Sans', sans-serif; margin:0 auto; display:block; height:40px; width:100%; padding:0 10px; border-radius:3px; font-size:16px; color:#FFF}                                       
                                                                                                                                                                                                                                                                                       
.social-login{padding:15px 20px; background:#f1f1f1; border-top:solid 2px #e8e8e8; text-align:right}                                                                                                                                                                                   
.social-login a{display:inline-block; height:35px; text-align:center; line-height:35px; width:35px; margin:0 3px; text-decoration:none; color:#FFFFFF}                                                                                                                                 
.form a i.fa{line-height:35px}                                                                                                                                                                                                                                                         
.fb{background:#305891} .tw{background:#2ca8d2} .gp{background:#ce4d39} .in{background:#006699}                                                                                                                                                                                        
.remember{width:50%; display:inline-block; clear:both; font-size:14px}                                                                                                                                                                                                                 
.remember:nth-child(2){text-align:right}                                                                                                                                                                                                                                               
.remember a{text-decoration:none; color:#666}                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                       
.hide{display:none}                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                       
/*swich form*/                                                                                                                                                                                                                                                                         
#signup:checked~.section-out{margin-left:-350px}                                                                                                                                                                                                                                       
#login:checked~.section-out{margin-left:0px}                                                                                                                                                                                                                                           
#login:checked~div .form-header li:nth-child(1),#signup:checked~div .form-header li:nth-child(2){background:#e8e8e8}                                                                                                                                                                   
</style>   
 </head>                                                                                                                                                                                                                                                                               
 <body style=background-image:url('aaa.png');>                                                                                                                                                                                                                             
 <div id=login-form>                                                                                                                                                                                                                                                                   
 <center><h1>Stock</h1></center>                                                                                                                                                                                                                                                                                      
<input type=radio checked id=login name=switch class=hide>                                                                                                                                                                                                                             
<input type=radio id=signup name=switch class=hide>                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                       
<div>                                                                                                                                                                                                                                                                                  
<ul class=form-header>                                                                                                                                                                                                                                                                 
<li><label for=login><i class=fa fa-lock></i> LOGIN<label for=login></li>                                                                                                                                                                                                              
<li><label for=signup><i class=fa fa-credit-card></i> REGISTER</label></li>                                                                                                                                                                                                     
</ul>                                                                                                                                                                                                                                                                                  
</div>                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                       
<div class=section-out>                                                                                                                                                                                                                                                                
<section class=login-section>                                                                                                                                                                                                                                                          
<div class=login>                                                                                                                                                                                                                                                                      
<form action='UserHome.py' method=post>                                                                                                                                                                                                                 
<ul class=ul-list>                                                                                                                                                                                                                                                                     
<li><input type=Text name=userlogin required class=input placeholder="Login ID"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                     
<li><input type=password name=userpwd required class=input placeholder=Password><span class=icon><i class=fa fa-lock></i></span></li>                                                                                                                                                   
<li><!--<span class=remember><input type=checkbox id=check> <label for=check>Remember Me</label></span>--><span class=remember><a href=ForgetPassword.py>Forget Password</a></span></li>                                                                                                                       
<li><input type=submit name=login value=SIGN IN class=btn></li>                                                                                                                                                                                                                        
</ul>                                                                                                                                                                                                                                                                                  
</form>                                                                                                                                                                                                                                                                                
</div>                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                       
<div class=social-login>                                                                                                                                                                         
<a href= class=fb><i class=fa fa-facebook></i></a>                                                                                                                                                                                                                                 
<a href= class=tw><i class=fa fa-twitter></i></a>                                                                                                                                                                                                                                      
<a href= class=gp><i class=fa fa-google-plus></i></a>                                                                                                                                                                                                                                  
<a href= class=in><i class=fa fa-linkedin></i></a>                                                                                                                                                                                                                                     
</div>                                                                                                                                                                                                                                                                              
</section>                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                       
<section class=signup-section>                                                                                                                                                                                                                                                         
<div class=login>                                                                                                                                                                                                                                                                      
<form action='UserReg1.py' method=post name="frm" onsubmit= "return checkCheckBox()">                                                                                                                                                                                                                 
<ul class=ul-list>                                                                                                                                                                                                                                                                     
<li><input type=text name=ufnm required maxlength=30 class=input placeholder="Enter First Name" onkeyup="AllowAlphabet()"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                               	
<li><input type=text name=ulnm required maxlength=30 class=input placeholder="Enter Last Name" onkeyup="AllowAlphabett()"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                              
<li><td> Date of Birth</td><input type=date name=dob required class=input id=dob onChange= dobValidate() ><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                            
<li><td> Select Gender </td><input type=radio name=usergen value=Male>Male<input type=radio name=usergen  value=Female>female<span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                              
<li><input type=text name=umno pattern=[1-9]{1}[0-9]{9} maxlength=10 required class=input placeholder="Mobile Number"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                               
<li><input type=email name=ueid required class=input placeholder="Enter Email" onChange="return validateForm()"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                              
<li><input type=text name=ano pattern=[0-9]{12} maxlength=12 required class=input placeholder="Enter Addhar Number"><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                        
<li><td> Upload Aadhar Card</td><input type=file id="file" name=ac  class=input placeholder="Upload Aadhar Card" onChange="return fileValidation()" required ><span class=icon><i class=fa fa-user></i></span></li>     

<li><td> Upload Photograph</td><input type=file id="filee" name=ph  class=input placeholder="Upload Photo" onChange="return fileValidationn()"  required><span class=icon><i class=fa fa-user></i></span></li>

<li><td> Upload Signature</td><input type=file  id="fileee" name=sign class=input placeholder="Upload sign" onChange="return fileValidationnn()"  required><span class=icon><i class=fa fa-user></i></span></li>                                                                                                                                                             

<li><input type=password name=userpwd required class=input placeholder=Password><span class=icon><i class=fa fa-lock></i></span></li>                                                                                                                                                              
<tr><td><input type= reset ></td></tr>
<li><input type=checkbox id=check1 value="0" name="agree"> <label for=check1>I accept terms and conditions</label></li>                                                                                                                                                                                       
<li><input type=submit name=login value="SIGN UP" class=btn></li>                                                                                                                                                                                                                        
<tr><td><a href=ForgetPassword.py>Forget Password</a></td></tr>
</ul>                                                                                                                                                                                                                                                                                  
</form>                                                                                                                                                                                                                                                                                
</div>                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                       
<div class=social-login>                                                                                                                                                                         
<a href= class=fb><i class=fa fa-facebook></i></a>                                                                                                                                                                                                                                 
<a href= class=tw><i class=fa fa-twitter></i></a>                                                                                                                                                                                                                                      
<a href= class=gp><i class=fa fa-google-plus></i></a>                                                                                                                                                                                                                                  
<a href= class=in><i class=fa fa-linkedin></i></a>                                                                                                                                                                                                                                 
</div>                                                                                                                                                                                                                                                                                 
</section>                                                                                                                                                                                                                                                                             
</div>                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                       
</div>                                                                                                                                                                                                                                                                                 
 </body>                                                                                                                                                                                                                                                                               
 </html> ''')