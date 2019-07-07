function existingUsername(){
  var username = document.forms["Signup form"]["username"]
  window.alert("This username exists , please try another one , or leave it blank to auto generate username");
  username.focus();
}
