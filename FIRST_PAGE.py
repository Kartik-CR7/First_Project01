<!DOCTYPE html>
{% load staticfiles %}
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<head>
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<style>
* {
  box-sizing: border-box;
}

.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}

body {
  font-family: Arial;
  padding: 10px;
  background: #f1f1f1;
}

/* Header/Blog Title */
.header {
  padding: 80px;
  text-align: center;
  background: white;
    margin-top: auto;
    font-family: "Curlz MT";
    font-weight: bold;
}

.header h1 {
  font-size: 40px;
  font-family: cursive ;
  font-weight: bolder;
  -moz-text-size-adjust: auto;
}

.icon-bar {
  position: inherit;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.icon-bar a {
  display: block;
  text-align: center;
  padding: 16px;
  transition: all 0.3s ease;
  color: white;
  font-size: 20px;
}

.icon-bar a:hover {
  background-color: #000;
}
	/*=-footer-=*/
			footer {
				color: #fff;
				background-attachment: fixed;
				background-color:#222;
        background-image: url(https://s7.postimg.org/uyf0oioaz/footer-bg.png);
				background-size: cover;
				background-position: bottom;
			}
			footer p {
				color: #ccc;
			}
	   footer a {
				color: #ccc;
			}
			.social-pet li {
				display: inline-block;
				margin-right: 10px;
			}
			.social-pet li a {
				height: 35px;
				width: 35px;
				border-radius: 50%;
				text-align: center;
				display: block;
				line-height: 35px;
				background-color: #3a5a95;
				color: #fff;
			}
			.social-pet li:nth-child(2) a {
				background-color: #57aced;
			}
			.social-pet li:nth-child(3) a {
				background-color: #dd4f43;
			}
			.social-pet li:nth-child(4) a {
				background-color: #6b27b2;
			}
			.social-pet li a:hover {
				background-color: #0141a2;
			}
			.social-pet li a:hover i {
				transform: rotate(360deg);
				-moz-transform: rotate(360deg);
				-webkit-transform: rotate(360deg);
			}
			.recent-post li {
				display: block;
				color: #ccc;
				margin-bottom: 25px;
			}
			.recent-post li label {
				float: left;
				border: 2px solid #ccc;
				padding: 1px 7px;
				text-align: center;
			}
			.recent-post li label span {
				color: #fff;
			}
			footer .input-group-addon {
				background-color: #0141a2;
				padding: 10px;
			}
			.f-address li {
				display: inline-block;
			}
			.f-address li i {
				color: #2995de;
				font-size: 18px;
			}
			.f-address li a {
				color: #ccc;
			}
			/*=-Copyright-=*/
			.copyright {
				background-color: #111;
				padding: 12px 0;
        font-size:14px;
			}

.leftcolumn {
  float: left;
  width: 75%;
}

.fakeimg {
  background-color: #aaa;
  width: 100%;
  padding: 20px;
}

/* Add a card effect for articles */
.card {
  background-color: white;
  padding: 20px;
  margin-top: 20px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Footer */
.footer {
  padding: 20px;
  text-align: center;
  background: #ddd;
  margin-top: 20px;
}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 800px) {
  .leftcolumn, .rightcolumn {
    width: 100%;
    padding: 0;
  }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
@media screen and (max-width: 400px) {
  .topnav a {
    float: none;
    width: 100%;
  }
}
    body {
  font-family: "Lato", sans-serif;
}
.sidebar {
  height: 100%;
  width: 0%;
  position: fixed;
    align-items: stretch;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidebar a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidebar a:hover {
  color: #f1f1f1;
}

.sidebar .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

.openbtn {
  font-size: 20px;
  cursor: pointer;
  background-color: #111;
  color: white;
  padding: 10px 15px;
  border: none;
}

.openbtn:hover {
  background-color: #444;
}

#main {
  transition: margin-left .5s;
  padding: 16px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
}
.footer{
    background-color: black;
}
.imgButton{
  text-align: left;
}
</style>
</head>
<body>
<div class="header">
  <h1>Milieshankhdhar</h1>
  <p>Live. Love. Celebrate</p>
</div>

<div id="mySidebar" class="sidebar">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">�</a>
  <a href="#">About</a>
  <a href="#">Travel</a>
    <a href="#">Photography</a>
  <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Fashion</a>
<ul class="collapse list-unstyled" id="pageSubmenu">
    <li>
        <a href="#">Western</a>
    </li>
    <li>
        <a href="#">Festive</a>
    </li>
</ul>
  <a href="#">Contact Me</a>
</div>

<div id="main">
  <button class="openbtn" onclick="openNav()">? MyBlogMenu</button>
</div>

<script>
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
</script>

<div class="row">
  <div class="leftcolumn">
    <div class="card">
      <h2>TITLE HEADING</h2>
      <h5>Title description, Dec 7, 2017</h5>
      <table>
		<tr>
			<td>
      <div class="imgContainer">
				<div>
					<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPy7ZnI46zizXRVoXLbV4Gl6LamFU6g5pqtJj1ijxnO8i-gJWp" width="100px" height="100px"/>
				</div>
				<div class="imgButton">
					<button value="Like"><p><a class='like-btn' data-href='{{ post.get_api_like_url }}' data-likes='{{ post.likes.count }}'  href='{{ post.get_like_url }}'>
          {{ post.likes.count }} Like</a>{{message}}</p></button>
				</div>
         </div>
			</td>
      <td>
      <div class="imgContainer">
				<div>
					<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPy7ZnI46zizXRVoXLbV4Gl6LamFU6g5pqtJj1ijxnO8i-gJWp" width="100px" height="100px"/>
				</div>
				<div class="imgButton"><form action='' method='GET'>
			<button value="like">Like</button>
            </form>
				</div>
         </div>
			</td>
		</tr>
	</table>
      <p>Some text..</p>
      <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
    </div>
    <div class="card">
      <h2>TITLE HEADING</h2>
      <h5>Title description, Sep 2, 2017</h5>
      <div class="fakeimg" style="height:200px;">Image</div>
      <p>Some text..</p>

    </div>
  </div>

</div>


<link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
<!-- Footer -->
		<footer class="pt-5 pb-4" id="contact" style="text-align: center">
			<div class="container" style="text-align: center" >


                        <h5 class="mb-4 font-weight-bold" style="text-align: center" >CONNECT WITH US :</h5>
						<ul class="social-pet mt-4" style="text-align: center">
                            <li><a href="#" title="instagram"><i class="fab fa-instagram" ></i></a></li>
                            <li><a href="#" title="google-plus"><i class="fab fa-google-plus-g"></i></a></li>
							<li><a href="https://www.google.com/" title="facebook"><i class="fab fa-facebook-f"></i></a></li>
						</ul>
			</div>
		<!-- Copyright -->
		<section class="copyright">
			<div class="container">
				<div class="row">
					<div class="col-md-12 ">
						<div class="text-center text-white">
							&copy; 2018 Your Blog. All Rights Reserved.
						</div>
					</div>
				</div>
			</div>
		</section>
</div>

</body>
</html>
