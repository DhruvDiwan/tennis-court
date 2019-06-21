function validate_login()
{
  var username = document.forms["Login form"]["username"]
  var email = document.forms["Login form"]["E-mail"]

  if(username.value == "")
  {
    window.alert("Please enter your username.");
    name.focus();
    return false;
  }
  if(email.value == "")
  {
    window.alert("Please enter your email.");
    email.focus();
    return false;
  }
}

function validate_signUp()
{
  var fName = document.forms["Signup form"]["fName"]
  var sName = document.forms["Signup form"]["sName"]
  var username = document.forms["Signup form"]["username"]
  var email = document.forms["Signup form"]["E-mail"]
  var mobNo = document.forms["Signup form"]["mobNo"]
  var pass1 = document.forms["Signup form"]["New pass"]
  var pass2 = document.forms["Signup form"]["Confirm pass"]
  if(fName.value == "")
  {
    window.alert("Please enter your First Name.");
    fName.focus();
    return false;
  }
  if(sName.value == "")
  {
    window.alert("Please enter your Surname.");
    sName.focus();
    return false;
  }
  if(username.value == "")
  {
    window.alert("Please enter your username.");
    username.focus();
    return false;
  }
  if(email.value == "")
  {
    window.alert("Please enter your email.");
    email.focus();
    return false;
  }
  if(mobNo.value == "")
  {
    window.alert("Please enter your Mobile Number.");
    mobNo.focus();
    return false;
  }
  if(pass1.value == "")
  {
    window.alert("Please enter your new password.");
    pass1.focus();
    return false;
  }
  if(pass2.value == "")
  {
    window.alert("Please confirm, your new password.");
    pass2.focus();
    return false;
  }
  if(pass1.value != pass2.value){
    window.alert("New Password and Confirmed Password don't match, re-enter");
    pass1.focus();
    return false;
  }
}
